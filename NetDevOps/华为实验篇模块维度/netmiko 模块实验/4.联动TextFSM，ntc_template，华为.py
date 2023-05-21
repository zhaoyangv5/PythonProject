'''
实验我们探讨在 netmiko 里直接调用 textfsm ，仅需要传入一个参数 use_textfsm=True ，便可以享用 netmiko 模块联动 textfsm 的功能。
但是，目前大量的模板还是思科的，华为只提供了 4 个 demo模板，不过还是那句话，不影响我们学习技能，而且学有余力可以共享模板哈
华为模板提供了vrp模板V8
'''

from netmiko import ConnectHandler
from textfsm import TextFSM
from pprint import pprint

connection_info = {'device_type':'huawei_vrpv8',
      'ip':'192.168.31.100',
      'username':'python',
      'password':'Admin@123'}

with ConnectHandler(**connection_info) as conn:
    output = conn.send_command("display interface brief",use_textfsm=True)

print(output)
pprint(output)
