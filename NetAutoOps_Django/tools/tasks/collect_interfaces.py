from pathlib import Path

from nornir.core.task import Result, Task

from cmdb.models import Device, Interface
from tools.get_nornir_obj import get_nornir_by_django_queryset

# 静态变量，指向解析模板的目录
TEXTFSM_TEMPLATE_DIR = 'textfsm_templates'
# 支持的平台，其对应的执行的命令及解析模板
PLATFORM_PARSE_INFO = {
    'huawei': {'cmd': 'display interface', 'textfsm': 'huawei_display_interface.textfsm'},
}


def collect_interfaces(task_context: Task):
    result = '{}端口更新成功'.format(task_context.host.name)
    host_obj = task_context.host
    platform = host_obj.platform

    # 判断当前平台是否在支持的平台解析字典当中
    if platform in PLATFORM_PARSE_INFO:
        # 获取Netmiko连接
        net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)
        # secret参数可以直接从Netmiko连接中获取
        secret = net_conn.secret
        if secret:
            net_conn.enable()
        # 获取执行的命令和对应的解析模板
        cmd = PLATFORM_PARSE_INFO[platform]['cmd']
        textfsm_template = str(Path('tools', TEXTFSM_TEMPLATE_DIR, PLATFORM_PARSE_INFO[platform]['textfsm']))
        # 执行命令，并进行解析
        data = net_conn.send_command(cmd, use_textfsm=True, textfsm_template=textfsm_template)
        print(data)

        # 如果返回的数据是字符串，证明解析失败，返回的是回显文本
        if isinstance(data, str):
            # 抛出异常，进而关注解析模板的准确性和兼容性
            raise Exception('解析数据失败,未获取到有效数据，请确认解析模板是否编写正确')
        # 解析成功后，将数据写入数据库
        # 查找网络设备Device
        dev_obj = Device.objects.filter(name=task_context.host.name)[0]
        for i in data:
            i['dev'] = dev_obj
            # 查找对应设备是否有端口，有则更新最新的数据，无则创建
            # 我们使用了管理器objects的update_or_create方法，defaults变量以外的是查找端口的依据
            # 如果查到了端口，则使用defaults中的数据更新查到的数据对应字段
            # 如果未查到端口，则使用defauls中的数据创建一条数据
            interface_obj,created = Interface.objects.update_or_create(defaults=i, dev=dev_obj, name=i['name'])

    else:
        raise Exception('暂时不支持此平台设备的端口信息采集')

    return Result(host=task_context.host, result=result)


def batch_collect_interfaces(queryset, num_workers=100):
    # 通过Device的queryset加载nornir对象
    nr = get_nornir_by_django_queryset(queryset, num_workers)
    # 批量执行收集并更新软件版本的task函数
    result = nr.run(task=collect_interfaces)
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
