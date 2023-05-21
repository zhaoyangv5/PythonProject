"""
我们完全基于nornir_netmiko包去完成了与网络设备的CLI交互，在一些比较复杂的场景之下，
频繁与网络设备交互，需要调用一些特殊的模式，使用原生的Netmiko可能会更加灵活便捷。
另外还有一个重要的原因，我们执行之前的runbook，所有task任务的执行结果都会保存在Nornir对象的相关属性之中，而这些数据都会临时放在内存中，
即每台设备的回显都会放在内存中，假如我们对大批量设备执行的是show running-configuration类似的命令，
则其回显文本比较大，且都会放置在内存中，设备数量一多，会对我们执行脚本的服务器资源有一定浪费。当然目前而言，这些对于几千台设备而言，
这些回显文本还撑不爆内存，但也会拖慢执行效率
"""

import logging

from nornir.core.task import Result, Task
from nornir_utils.plugins.tasks.files import write_file
from datetime import date
from pathlib import Path
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result



def write_content2file(filename, content, dirs):
    # 通过pathlib模块的Path对象 拼接一个路径
    dir_path = Path(*dirs)
    # parents，exist_ok一定都置为True，这样父目录未创建则自动创建，目录存在不做任何动作也不会报错
    dir_path.mkdir(parents=True, exist_ok=True)
    # 拼接完整文件的路径，使用不定参数的赋值方式。
    filepath = Path(*dirs, filename)
    with filepath.open('w', encoding='utf8') as f:
        f.write(content)
    return str(filepath)


def config_backup(task_context: Task):
    # 返回结果，key为对应的cmd，value是对应备份文件的路径。
    result = {}

    cmds = task_context.host.data['cmds']
    cmds = cmds.split(',')
    date_str = date.today().strftime('%Y%m%d')
    ip = task_context.host.hostname
    # 通过task上下文获取Host对象，然后调用其get_connection方法获取Netmiko的连接
    net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)
    # secret参数可以直接从Netmiko连接中获取
    secret = net_conn.secret

    # 有secret参数，不为空，则调用enable方法
    if secret:
        net_conn.enable()
    for cmd in cmds:
        output = net_conn.send_command(cmd)
        filename = '{}.txt'.format(cmd)
        filepath = write_content2file(filename=filename,content=output,dirs=[date_str, ip])
        result[cmd] = {'filepath': filepath}
    # 将结果封装到Result对象中，由于配置备份成功，
    # 生成了新的配置备份文件，按照自动化框架的一些约定俗成的规定，则将changed改为True，
    return Result(host=task_context.host, result=result, changed=True)

if __name__ == '__main__':
    runner = {
        "plugin": "threaded",
        "options": {
            "num_workers": 100,
        },
    }
    inventory = {
        "plugin": "ExcelInventory",
        "options": {
            "excel_file": "inventory.xlsx",
        },
    }

    nr = InitNornir(runner=runner, inventory=inventory)
    result = nr.run(task=config_backup)
    print_result(result)