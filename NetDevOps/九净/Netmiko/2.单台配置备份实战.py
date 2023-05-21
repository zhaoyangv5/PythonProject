'''
配置备份
巡检数据收集
'''

from netmiko import ConnectHandler

#cmd： 要执行的配置备份的命令，
#假如我们的网络环境是以华为设备为主，我们可以给这个参数一个默认值“display current-configuration”，这样调用函数的时候，我们就无需传入cmd参数了
def network_device_backup(dev, cmd='display current-configuration'):
    """
    登录设备执行配置备份的命令，并将设备回显的配置写入一个<设备IP或者host>.txt的文件中，编码格式utf8
    :param dev: 设备的基础信息，类型字典，key与创建netmiko所需的参数对应
    :param cmd: 要执行的配置备份的命令，默认是华为的“display current-configuration”
    :return: None 不返回，只打印
    """
    with ConnectHandler(**dev) as conn:
        conn.enable()
        #函数的代码逻辑中我们执行了enable方法，在华为的驱动中这个方法是空的，所以不影响整体使用。
        #在一些驱动中比如华三的驱动中是进入了system-view模式，但是执行查看配置的命令也是没问题的
        output = conn.send_command(command_string=cmd)
        file_name = '{}.txt'.format(dev['host'])
        with open(file_name, mode='w', encoding='utf8') as f:
            f.write(output)
            print('{}执行备份成功'.format(dev['host']))


if __name__ == '__main__':
    dev = {'device_type': 'huawei',
           'host': '192.168.31.100',
           'username': 'python',
           'password': 'Admin@123',
           'port': 22}

    network_device_backup(dev)