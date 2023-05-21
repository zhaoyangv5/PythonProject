'''
实验目的

结合 Netmiko 官方 API ，配合 help、dir 等内置方法，探索华为enable相关方法。
参考 paramiko 方式，使用 netmiko 的 send_command 方法来实施提权操作。
提权操作能实施，通用性的指令逐条推送，指令交互则也可以用 send_command 方法实施。
'''



'''
Paramiko 实现
'''
# import paramiko    # 引入 paramiko 模块，用于联机操作。
# import time        # 引入 time 模块，用于延时。
#
# # 资源信息
# username = "python"
# password = "1234abcd"
# ip = '172.25.1.234'
# secret = "abcd1234"
#
# # paramiko 联机“套路”
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=ip, username=username,  \
#                    password=password, look_for_keys=False)
# print("Successfully connected to ",ip)
#
# # 注：这些代码中间，我们可以随时加插 print(xx) 进行测试，术语叫“调试”。
#
# command = ssh_client.invoke_shell()
# command.send("sys\n")
# output = command.recv(65535)
# print(output.decode("ascii"))   # 回显信息涉及到编解码。
#
# time.sleep(1)
# command.send("su\n")            # 进行提权 su。
# command.send(secret+"\n")       # 送入提权密码。
# output = command.recv(65535)
# print(output.decode("ascii"))   # 回显信息涉及到编解码。
#
# time.sleep(1)
# command.send("sys\n")
# output = command.recv(65535)
# print(output.decode("ascii"))   # 回显信息涉及到编解码。
# ssh_client.close()


# import netmiko
from netmiko import ConnectHandler

sw2 = {'device_type': 'huawei',
       'ip': '172.25.1.234',
       'username': 'python',
       'password': '1234abcd',
       # 'secret': r'1234abcd', # 提权密码也可以在这里存入，本例直接在 command_string 写入。
       'session_log': 'netmikowgsy.log'}

with ConnectHandler(**sw2) as connect:
    print("已经成功登陆交换机" + sw2['ip'])
    # output = connect.enable()
    # output = connect.send_command(command_string='sys')
    output = connect.send_command(command_string='su',expect_string = 'Password:')
    print(111)   # 增加点调测
    output += connect.send_command(command_string=r'1234abcd',expect_string = '>',cmd_verify = False)
    print(222)
    output += connect.send_command(command_string='sys',expect_string = ']')
    output += connect.send_command(command_string='disp cur',expect_string = ']')
    output += connect.send_command(command_string='quit',expect_string = '>')
    # 还可以在这里进入接口，给接口配置信息，然后退出！大家试试看！
    print(output)