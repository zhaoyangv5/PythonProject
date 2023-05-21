'''
首先设计一个函数，实现单设备的配置推送，这个函数接受三个参数：创建netmiko连接的基本信息、配置存放的文件、是否进行提权。
设计一个表格承载每台网络设备进行批量配置推送所需的表头，上述函数可以对接。
读取表格信息，循环调用1中所述的函数。
'''
from netmiko import ConnectHandler
import pandas as pd


def network_device_config_push_by_config_file(dev, config_file=None, enable=False):
    """
    使用netmiko登录设备,通过config_file中的调用netmiko连接类中的send_config_from_file方法，
    将配置推送到设备并保存，整个配置推送的过程保存到日志文件当中。
    :param dev: 设备的基础信息，类型字典，key与创建netmiko所需的参数对应
    :param config_file: 存放预下发配置的文本文件，utf8格式。如果为None，则以{dev[host]}.txt作为配置文件
    :param enable: 是否提权当前用户，默认值为False不进行提权。
    :return: {'push_sucess':True or Fasle # 配置推送是否成功
              'session_log':配置推送过程的日志文件 # 配置推送的日志文件
             }
    """
    # 如果config_file传入的值为空，则根据规则读取默认的配置文件
    if not config_file:
        config_file = '{}.txt'.format(dev['host'])
    # 添加配置推送的日志文件
    session_log = '{}.log'.format(dev['host'])
    dev['session_log'] = session_log
    # 初始化返回结果
    push_result = {
        'push_sucess': True,
        'session_log': session_log
    }
    try:
        with ConnectHandler(**dev) as conn:
            # 如果用户选择开启enable模式 则调用enable方法
            if enable:
                conn.enable()
            push_output = conn.send_config_from_file(config_file)
            save_output = conn.save_config()

    except Exception as e:
        push_result['push_sucess'] = False
        print('{}配置推送发生异常，使用的配置文件为:{}，异常信息:{}'.format(dev['host'], config_file, e))

    return push_result


def get_batch_config_push_dev_infos(filename='config_inventory.xlsx'):
    '''
    读取Excel表格加载网络设备基本信息和配置文件，结果返回一个用于批量配置推送的元组的列表
    :param filename: 表格名称，默认值是inventory.xlsx
    :return: [(<netmiko连接设备所需基本信息的字典>,<配置文件>,<是否提权>)]
    示例：
    [({'host': '192.168.137.201',
       'device_type': 'huawei',
       'username': 'netdevops',
       'password': 'Admin123~',
       'secret': nan,
       'timeout': 180,
       'conn_timeout': 20},
       '192.168,137.201.config',
       False),
    ]
    '''
    # 读取并将表格加载成字典的列表
    df = pd.read_excel(filename)
    # 表格中的部分未填充值的单元格加载到pandas中会是一种特殊的空值nan，为了方便后续处理我们一律填充为空字符串
    df = df.fillna('')
    items = df.to_dict(orient='records')
    # 构建返回的结果，dev_infos是一个元组的列表。
    dev_infos = []
    for i in items:
        # 取出相关配置推送的参数，并用del将其从字典中删除
        config_file = i['config_file']
        del i['config_file']
        # pandas无法保存布尔值，故简单对其进行一个判断
        # 对表中的数据转为小写，方便比对判断
        enable = i['enable']
        del i['enable']

        # 删除配置备份命令后的字典就是netmiko登录设备所需的信息
        dev = i
        dev_infos.append((dev, config_file, enable))
    return dev_infos


def batch_config_push(inventory_file='config_inventory.xlsx'):
    push_results = []
    dev_infos = get_batch_config_push_dev_infos(inventory_file)
    for dev_info in dev_infos:
        # 我们使用一个星号* 后接一个元组或列表，就可以按顺序依次传入参数到函数中
        # 以下书写方式等同于network_device_config_push_by_config_file(dev_info[0],dev_info[1],dev_info[2])
        result = network_device_config_push_by_config_file(*dev_info)
        push_results.append(result)
    # print(push_results)
    return push_results


if __name__ == '__main__':
    results = batch_config_push()
    for i in results:
        print(i)


'''
配置推送小结

1.netmiko的两个配置推送方法适合推送配置过程中无交互的场景。如果涉及到复杂交互，建议使用send_command。
2.这两个方法在开始的时候会自动进入配置模式，在输入完最后一条命令确认设备收到后会自动退出配置模式。
3.部分设备需要提权才可以进入配置模式，我们要根据情况合理调用enable方法或者使用send_command方法进行提权。
4.这两个方法只负责发送配置到设备，如果要生效，需要结合具体设备型号而言，有的在命令行中调用commit（比如华为的设备）,有的可以调用commit方法。
5.配置的保存需要单独调用save_config方法。（极个别设备没有保存配置这一逻辑，或者是通过commit来实现配置生效，所以此方法调用的时候会报错）
6.配置推送相关脚本建议初始化连接的时候赋值session_log，用于了解和设备的整个交互过程，在程序失败的时候，可以查看log文件了解推送的情况，用于善后或者修正程序。
7.对待配置推送一定要有敬畏之心，建议从风险小，机械性高的场景开始。
8.配置推送一定要保证ssh隧道通常，如果是类似修改设备管理IP且立即生效，可能会导致程序失败。
'''
