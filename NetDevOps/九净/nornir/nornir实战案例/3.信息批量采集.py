


from nornir.core.task import Result, Task
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from pathlib import Path
import pandas as pd
# from tasks.collection_interfaces import collection_interfaces


# 静态变量，指向解析模板的目录
TEXTFSM_TEMPLATE_DIR = 'textfsm_templates'
# 支持的平台，其对应的执行的命令及解析模板
PLATFORM_PARSE_INFO = {
    'huawei': {'cmd': 'display interface brief', 'textfsm': 'huawei_display_interface_brief.textfsm'},
    'cisco_ios': {'cmd': 'show interface brief', 'textfsm': 'cisco_ios_show_interface_brief.textfsm'},
}


def data2excel(data, filename, dirs):
    """
    将指定字典的列表数据写入Excel表格的函数
    Args:
        data: 字典的列表数据
        filename: Excel文件名称
        dirs: 表格所处的目录，列表格式

    Returns:
        Excel文件路径

    """
    # 创建对应的目录层级
    dir_path = Path(*dirs)
    # parents，exist_ok一定都置为True，这样父目录未创建则自动创建，目录存在不做任何动作也不会报错
    dir_path.mkdir(parents=True, exist_ok=True)
    # 拼接完整文件的路径
    filepath = str(Path(*dirs, filename))
    # 通过pandas写入数据
    df = pd.DataFrame(data)
    df.to_excel(filepath, sheet_name='interfaces', index=False)
    return filepath


def collect_interfaces(task_context: Task):
    """
    收集网络设备的端口信息数据，并写入到Excel表格中
    返回结果result 为字典，包含表格文件路径，与端口总数
    {’filepath':'XX','interface_total':100}
    """

    result = {'interface_total': None, 'filepath': None}

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
        textfsm_template = str(Path(TEXTFSM_TEMPLATE_DIR, PLATFORM_PARSE_INFO[platform]['textfsm']))
        # 执行命令，并进行解析
        data = net_conn.send_command(cmd, use_textfsm=True, textfsm_template=textfsm_template)

        # 如果返回的数据是字符串，证明解析失败，返回的是回显文本
        if isinstance(data, str):
            # 抛出异常，进而关注解析模板的准确性和兼容性
            raise Exception('解析数据失败,未获取到有效数据，请确认解析模板是否编写正确')
        # 计算返回数据的长度，即端口数量
        interface_total = len(data)
        # 更新数据到返回结果中
        result['interface_total'] = interface_total
        # 暂时将端口列表返回到结果，方便中间调试查看，后期可以去除
        # result['data'] = data
        filepath = data2excel(data=data, filename='interfaces.xlsx', dirs=['data', host_obj.hostname])
        result['filepath'] = filepath

    else:
        raise Exception('暂时不支持此平台设备的端口信息采集')

    return Result(host=task_context.host, result=result)



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
    result = nr.run(task=collect_interfaces)
    print_result(result)

