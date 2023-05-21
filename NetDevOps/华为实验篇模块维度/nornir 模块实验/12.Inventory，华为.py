'''
实验目的

通过Nornir的inventory插件，获取hosts.yaml中保存的设备信息，如交换机SW1对应的name, hostname，username，password，platform，groups，data等
'''

import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='nornir.yaml')
# ipdb.set_trace()
print (nr.inventory.hosts['192.168.31.100'].name)
print (nr.inventory.hosts['192.168.31.100'].hostname)
print (nr.inventory.hosts['192.168.31.100'].username)
print (nr.inventory.hosts['192.168.31.100'].password)
print (nr.inventory.hosts['192.168.31.100'].platform)
print (nr.inventory.hosts['192.168.31.100'].groups)
print (nr.inventory.hosts['192.168.31.100'].data)


# # 如果不想看对象的魔法方法
# [method for method in dir(填入一个你不熟悉的对象) if not method.startswith('_')]
#
# # 如果也想看对象的魔法方法
# [method for method in dir(填入一个你不熟悉的对象)]