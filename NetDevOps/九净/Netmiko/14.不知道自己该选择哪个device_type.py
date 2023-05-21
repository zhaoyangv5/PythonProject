'''
在Netmiko章节之初我们讲过它支持众多的设备类型，也罗列出了一部分常见的device_type。
但是Netmiko支持的平台众多，我们写给大家一段代码，它可以输出当前版本netmiko所支持的所有平台
'''

# from netmiko import platforms
#
# # 列表推导式，把所有的ssh驱动取出
# ssh_platforms = [i for i in platforms if 'telnet' not in i and 'serial' not in i and 'ssh' not in i]
#
# # 去除一些厂商平台的device_type
# if 'abc' in ssh_platforms:
#     ssh_platforms.remove('abc')
# if 'autodetect' in ssh_platforms:
#     ssh_platforms.remove('autodetect')
# if 'terminal_server' in ssh_platforms:
#     ssh_platforms.remove('terminal_server')
#
# # 列表推导式取出telnet驱动
# telnet_platforms = [i for i in platforms if 'telnet' in i]
# # 列表推导式取出serial驱动
# serial_platforms = [i for i in platforms if 'serial' in i]

# print(ssh_platforms)
# print(len(ssh_platforms))
# print(telnet_platforms)
# print(len(telnet_platforms))
# print(serial_platforms)


'''
在我们日常使用中，可能情况会比较复杂，对于新手不清楚自己手中的设备应该选择哪个device_type，或者设备众多，单靠经验一台台判断，成本比较高。
这个时候我们可以调用netmiko的device_type自动检测机制，其代码示例如下：
'''
from netmiko import SSHDetect, Netmiko, ConnectHandler
# Netmiko等同于ConnectHanler
import logging

logging.basicConfig(
    level=logging.DEBUG,
)
dev = {
    'device_type': 'autodetect',
    'host': '192.168.31.100',
    'username': 'python',
    'password': 'Admin@123',
    'port': 22,
    'secret': 'Admin@123',
    'session_log':'session.log'
}

# 创建一个Detect的对象，将参数赋值
guesser = SSHDetect(**dev)

# 调用autodetect ，进行device_type的自动判断，返回结果是一个最佳结果的字符串，这个字符串就是netmiko自动判断的device_type
# 无法判断的时候返回的是None
best_match = guesser.autodetect()
print('best_match is:{}'.format(best_match))