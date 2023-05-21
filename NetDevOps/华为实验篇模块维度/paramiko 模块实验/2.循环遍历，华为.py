'''
实验目的

配合 getpass 模块和 input() 函数实现交互式的 SSH 用户名和密码输入。
配合 for loop 同时给 5 台交换机配置 VLAN 10 至 20
'''

import paramiko
import time
import getpass

username = input('username: ')
password = getpass.getpass('Password: ')

for i in range(100, 103):
    ip = '192.168.31.' + str(i)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('='*50)
    print('已经成功登陆交换机 Layer3Switch-'+ ' ' + ip)
    command.send('screen-length 0 temporary\n')
    command.send("system-view immediately\n")

    for i in range(100, 103):
        print('正在创建 VLAN ：' + str(i))
        command.send('vlan ' + str(i) + '\n')
        time.sleep(1)
        command.send('desc Python_vlan' + str(i) + '\n')
        time.sleep(0.5)
    command.send('return\n')
    command.send('save\n')
    command.send('Y\n')
    time.sleep(2)
    output = command.recv(65535).decode('ASCII')
    print(output)

ssh_client.close()


