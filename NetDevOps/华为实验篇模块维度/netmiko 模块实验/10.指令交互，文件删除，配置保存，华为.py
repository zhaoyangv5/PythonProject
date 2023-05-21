'''
实验目的

（1）用netmiko将Layer3Switch-2目录flash:/下的text.txt文件删除。

（2）用netmiko在Layer3Switch-2上执行save保存配置操作。
'''

import netmiko
from netmiko import ConnectHandler, file_transfer

sw1 = {'device_type': 'huawei',
       'ip': '192.168.31.101',
       'username': 'python',
       'password': 'Admin@123',
       }

# with ConnectHandler(**sw1) as connect:
#     print("已经成功登陆交换机" + sw1['ip'])
#
#     output = connect.send_command(command_string="delete cfcard:/text.txt",
#                                   expect_string=r"Delete cfcard:/text.txt?",
#                                   strip_prompt=False,
#                                   strip_command=False)
#     output += connect.send_command(command_string="y",
#                                    expect_string=r">",
#                                    strip_prompt=False,
#                                    strip_command=False)
#
#     print(output)


#改造为保存配置
with ConnectHandler(**sw1) as connect:
    print("已经成功登陆交换机" + sw1['ip'])

    output = connect.send_command(command_string="save",
                                  expect_string=r"Continue?",
                                  strip_prompt=False,
                                  strip_command=False)
    output += connect.send_command(command_string="y",
                                   expect_string=r">",
                                   strip_prompt=False,
                                   strip_command=False)

    print(output)