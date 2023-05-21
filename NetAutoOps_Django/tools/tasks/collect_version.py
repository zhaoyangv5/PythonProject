# tools\tasks\collect_version.py
from pathlib import Path

from nornir.core.task import Result, Task
from textfsm import TextFSM
from nornir import InitNornir
from netmiko import ConnectHandler
from nornir_netmiko import netmiko_send_command



# from cmdb.models import Device, Version
# from tools.get_nornir_obj import get_nornir_by_django_queryset
from tools.get_nornir_obj import get_nornir_by_django_queryset
from cmdb.models import Device, Version

# 静态变量，指向解析模板的目录
TEXTFSM_TEMPLATE_DIR = 'textfsm_templates'
# 支持的平台，其对应的执行的命令及解析模板
PLATFORM_PARSE_INFO = {
    'huawei': {'cmd': 'display version', 'textfsm': 'huawei_display_version.textfsm'},
}


def collect_version(task_context: Task):
    result = '{}软件版本更新成功'.format(task_context.host.name)
    host_obj = task_context.host
    # print(host_obj)
    platform = host_obj.platform
    # print(platform)

    # 判断当前平台是否在支持的平台解析字典当中
    if platform in PLATFORM_PARSE_INFO:
        # 获取Netmiko连接
        net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)
        # secret参数可以直接从Netmiko连接中获取
        secret = net_conn.secret
        #通过对Host对象的connection_options属性进行相关操作，获取netmiko参数中的secret
        # secret = task_context.host.connection_options.get('netmiko').extras.get('secret')
        if secret:
            net_conn.enable()
        # 获取执行的命令和对应的解析模板
        cmd = PLATFORM_PARSE_INFO[platform]['cmd']
        textfsm_template = str(Path('tools', TEXTFSM_TEMPLATE_DIR, PLATFORM_PARSE_INFO[platform]['textfsm']))
        print(textfsm_template)
        # 执行命令，并进行解析
        data = net_conn.send_command(cmd, use_textfsm=True, textfsm_template=textfsm_template)
        print("======")
        print(data, type(data))

        # 如果返回的数据是字符串，证明解析失败，返回的是回显文本
        if isinstance(data, str):
            # 抛出异常，进而关注解析模板的准确性和兼容性
            raise Exception('解析数据失败,未获取到有效数据，请确认解析模板是否编写正确')
        data = data[0]
        # 解析成功后，将数据写入数据库
        # 查找网络设备Device
        dev_obj = Device.objects.filter(name=task_context.host.name)[0]
        # 查找对应设备是否有软件版本记录，有则更新最新的数据，无则创建
        version_q = Version.objects.filter(dev=dev_obj)
        if version_q:
            version = version_q[0]
            version.version= data['version']
            version.patch = data['patch']
            version.series = data['series']
            version.uptime = data['uptime']
            version.save()
        else:
            version = Version(dev=dev_obj,
                              version=data['version'],
                              patch=data['patch'],
                              series=data['series'],
                              uptime=data['uptime'],
                              )
            version.save()


    else:
        raise Exception('暂时不支持此平台设备的软件版本信息采集')

    return Result(host=task_context.host, result=result)


def batch_collect_version(queryset, num_workers=100):
    # 通过Device的queryset加载nornir对象
    nr = get_nornir_by_django_queryset(queryset, num_workers)
    # 批量执行收集并更新软件版本的task函数
    result = nr.run(task=collect_version)
    # 初始化失败设备的列表
    fail_dev = []
    # 失败的设备会被Nornir捕获异常，将网络设备追加到Nornir Result的failed_hosts字段
    # 这是一个类似于字典的数据结构，可以进行for循环，key为Nornir网络对象的name属性，即设备名
    for fail_host_name in result.failed_hosts:
        fail_dev.append(fail_host_name)
    # 通过内置函数len计算失败网络设备的数量
    fail_num = len(fail_dev)
    # 通过本次执行任务设备总量减去失败的设备总量获取成功设备的总量
    success_num = len(queryset) - fail_num
    result_detail = {'success_num': success_num, 'fail_num': fail_num, 'fail_dev': fail_dev}
    return result_detail