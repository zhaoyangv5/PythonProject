"""
配置备份需要与网络设备进行交互，我们先写一个完全基于nornir_netmiko与设备进行CLI的交互的版本，要用到的插件包涉及：

nornir_table_inventory，使用表格来加载网络设备。
nornir_netmiko，实现与网络设备的CLI交互。
nornir_utils，将配置备份结果写入文件，以及结果的打印。

"""
import logging
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from datetime import date
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file

def config_backup(task_context: Task):
    # 返回结果，key为对应的cmd，value是对应备份文件的路径。
    result = {}

    cmds = task_context.host.data['cmds']
    cmds = cmds.split(',')
    date_str = date.today().strftime('%Y%m%d')
    ip = task_context.host.hostname
    # 通过对Host对象的connection_options属性进行相关操作，获取netmiko参数中的secret
    secret = task_context.host.connection_options.get('netmiko').extras.get('secret')
    # 有secret参数，则enable为True，再调用netmiko_send_command时传入
    if secret:
        enable = True
    else:
        enable = False
    for cmd in cmds:
        cmd_multi_result_objs = task_context.run(task=netmiko_send_command,
                                                 command_string=cmd,
                                                 enable=enable,
                                                 severity_level=logging.DEBUG)
        output = cmd_multi_result_objs[0].result
        filepath = '{}_{}_{}.txt'.format(date_str, ip, cmd)
        file_multi_result_objs = task_context.run(task=write_file,
                                                  filename=filepath,
                                                  content=output,
                                                  severity_level=logging.DEBUG)

        # 返回结果，key为对应的cmd，value是文件的路径。
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