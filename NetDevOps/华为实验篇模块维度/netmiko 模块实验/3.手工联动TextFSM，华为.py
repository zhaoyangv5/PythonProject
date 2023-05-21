'''
实验目的

虽然有些解析模块用不了，咱 Windows 多年习惯了。它还是能完成挺多的，继续挖一挖，实验还是能继续做的。这次我们让 netmiko 返回的信息，联动 Textfsm 做解析。本次实验目的如下：

（1）调用 send_command() 函数，执行 display vlan 检查交换机VLAN。

（2）制作 Textfsm 模板 display_vlan.template ，解析（1）的返回信息，把字符串格式化为咱们更容易操控的其它 Python 数据模型。

'''

from netmiko import ConnectHandler
from textfsm import TextFSM
from tabulate import tabulate

connection_info = {'device_type':'huawei',
      'ip':'192.168.31.100',
      'username':'python',
      'password':'Admin@123'}

with ConnectHandler(**connection_info) as conn:
    output = conn.send_command("display vlan")
print(output)
print(type(output))

with open('display_vlan.template') as f:
    template = TextFSM(f)
    # header = template.header
    demo_output = template.ParseText(output)
    # print(tabulate(demo_output, headers=header))
print(demo_output)

for each in demo_output:
    # print(each)
    print(each[0],each[-1])