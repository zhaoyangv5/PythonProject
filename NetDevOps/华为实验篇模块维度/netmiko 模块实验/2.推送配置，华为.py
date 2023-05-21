'''
实验目的

（1）send_command()：向设备发送一条命令，通常用于查询、排错、保存等命令。

（2）send_config_set()：向设备发送一条或多条配置命令，会自动适配到配置模式，通常配合指令列表。

（3）send_config_from_file()：如 send_config_set() 指令列表过大，可单独放入文本中配合 send_config_from_file() 调用。

（4）send_command_timing()：主动延迟等待，主要用于应对设备交互管理平台回显量大出现有意延迟或异常卡顿的现象。（初学者少用，本文暂不演示。）



通过 PC（192.168.11.2，Python所在），连接 Layer3Switch-1（192.168.31.100） ，完成如下三个小目标。

（1）调用 send_command() 函数，执行 display interface description 检查接口描述。

（2）调用 send_config_set() 函数，通过列表形式，配置 interface GigabitEthernet 0/0/0 的描述为“descby_send_config_set()”。

（3）调用 send_config_from_file()函数，通过文件形式，配置 interface GigabitEthernet 0/0/1 的描述为“descby_send_config_from_file()”。
'''

from netmiko import ConnectHandler

sw1 = {'device_type': 'huawei_vrpv8',
      'ip': '192.168.31.100',
      'username': 'python',
      'password': 'Admin@123'}

commands = ['interface GE 1/0/0', 'description descby_send_config_set()', 'commit']

with ConnectHandler(**sw1) as connect:
    print("已经成功登陆交换机" + sw1['ip'])

    print('===实验目的（1），交互形式推送一条指令。')
    output = connect.send_command('display interface description | include GE1/0/[012][^0-9]')
    print(output)

    print('===实验目的（2），列表形式推送多条指令。')
    output = connect.send_config_set(commands)
    print(output)

    print('===实验目的（3），文件形式推送多条指令。')
    output = connect.send_config_from_file('netmiko-config-lab.txt')
    print(output)

    print('===最后再检查配置')
    output = connect.send_command('display interface description | include GE1/0/[012][^0-9]')
    print(output)

    # 华为设备的保存配置save后需要输入y进行确认，后面实验再演示。
