'''
实验目的

1、在生产环境中，交换机的管理 IP 基本不可能像实验环境中这样 11 到 15，有些交换机的管理 IP 甚至在不同的网段，
这种情况下，我们就不能简单的用 for loop 来循环 IP 地址的最后一段来登录交换机。这里我们要额外开一个文本文件，把我们需要登录的交换机 IP 全部写进去，
然后用 for loop 配合 open() 函数来批量登录所有交换机
'''

import paramiko
import time
import getpass

username = input('username: ')
password = getpass.getpass('Password: ')

f = open('ip_list.txt')

for line in f.readlines():
    ip = line.strip()
    # print(ip)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('=' * 50)
    print('已经成功登陆交换机 Layer3Switch-' + ip)

    command.send('screen-length 0 temporary\n')
    # 进入系统视图
    command.send("system-view immediately\n")
    # 关闭消息通知（防止log信息刷屏）
    command.send('undo info-center enable\n')

    # 将交换机默认的 mstp 修改为 stp
    command.send('stp mode stp\n')
    time.sleep(2)

    # 返回用户视图
    command.send('return\n')
    # 执行保存
    command.send('save\n')
    command.send('Y\n')
    time.sleep(2)
    output = command.recv(65535).decode('ASCII')
    print(output)

f.close()
ssh_client.close()


