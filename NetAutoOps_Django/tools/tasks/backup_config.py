from django.core.files.base import ContentFile
from nornir.core.task import Result, Task

from cmdb.models import Device, ConfigBackup
from tools.get_nornir_obj import get_nornir_by_django_queryset

# 支持的平台，其对应的配置备份的命令
PLATFORM_BACKUP_INFO = {
    'huawei': ['display version', 'display current-configuration', 'display ip route-table'],
}


def backup_config(task_context: Task):
    result = '{}配置备份成功'.format(task_context.host.name)
    host_obj = task_context.host
    platform = host_obj.platform
    # 查找网络设备Device
    dev_obj = Device.objects.filter(name=task_context.host.name)[0]

    # 判断当前平台是否在支持的平台解析字典当中
    if platform in PLATFORM_BACKUP_INFO:
        # 获取Netmiko连接
        net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)
        # secret参数可以直接从Netmiko连接中获取
        secret = net_conn.secret
        if secret:
            net_conn.enable()
        # 获取对应平台要执行的配置备份命令
        cmds = PLATFORM_BACKUP_INFO[platform]

        for cmd in cmds:
            output = net_conn.send_command(cmd)
            # 配置备份文本文件名称
            file_name = '{}.config'.format(cmd)
            # 构建一个ContentFile对象用于赋值给配置备份ConfigBackup对象的config_file字段
            config_content = ContentFile(content=output.encode('utf8'), name=file_name)
            # 创建配置备份对象
            config_backup_obj = ConfigBackup(dev=dev_obj, cmd=cmd, config_file=config_content)
            config_backup_obj.save()


    else:
        raise Exception('暂时不支持此平台设备的配置备份')

    return Result(host=task_context.host, result=result)


def batch_backup_config(queryset, num_workers=100):
    # 通过Device的queryset加载nornir对象
    nr = get_nornir_by_django_queryset(queryset, num_workers)
    # 批量配置备份的task函数
    result = nr.run(task=backup_config)
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