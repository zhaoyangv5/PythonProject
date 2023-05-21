"""
实验目的

（1）多线程paramiko登陆Layer3Switch-1到Layer3Switch-5，执行如下命令。

sys
user-interface vty 0 4
 protocol inbound ssh
# 注，原先是 protocol inbound all 调整为 protocol inbound ssh
# 即只允许ssh链接
（2）多线程netmiko登陆Layer3Switch-1到Layer3Switch-5，执行同样的命令。

（3）观察python脚本执行的耗时情况。

"""
import threading
from queue import Queue
import time
import paramiko

""" paramiko """
def ssh_session(ip, output_q):   #output_q  设置一个参数，用来和Queue来握手
    username = 'python'
    password = 'Admin@123'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username,
                       password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()
    command.send('screen-length 0 temporary\n')
    command.send('system-view immediately\n')
    command.send('user-interface vty 0 4\n')
    command.send('protocol inbound ssh\n')
    command.send('return\n')
    time.sleep(1)
    output = command.recv(65535).decode('ASCII')
    # print(output)


print(f"程序于 {time.strftime('%X')} 开始执行\n")

threads = []

ip_list = ['192.168.31.100', '192.168.31.101', '192.168.31.102']

for ips in ip_list:
    t = threading.Thread(target=ssh_session, args=(ips.strip(), Queue()))
    t.start()
    threads.append(t)       #任务打包，即登录一台设备执行命令做出一个任务

for i in threads:
    i.join()        #上述任务间同时执行，都执行完后，在接着执行下面的print

print(f"\n程序于 {time.strftime('%X')} 执行结束")



"""netmiko"""

import threading
from queue import Queue
import time
from netmiko import ConnectHandler


def ssh_session(ip, output_q):      #output_q  设置一个参数，用来和Queue来握手
    commands = ["user-interface vty 0 4", "protocol inbound ssh"]
    SW = {'device_type': 'huawei', 'ip': ip, 'username': 'python', 'password': 'Admin@123'}
    ssh_session = ConnectHandler(**SW)
    output = ssh_session.send_config_set(config_commands=commands)
    save_output = ssh_session.save_config()
    print(output)
    print(save_output)


print(f"程序于 {time.strftime('%X')} 开始执行\n")

threads = []

ip_list = ['192.168.31.100', '192.168.31.101', '192.168.31.102']

for ips in ip_list:
    t = threading.Thread(target=ssh_session, args=(ips.strip(), Queue()))
    t.start()
    threads.append(t)           #任务打包，即登录一台设备执行命令做出一个任务

for i in threads:
    i.join()                #上述任务间同时执行，都执行完后，在接着执行下面的print

print(f"\n程序于 {time.strftime('%X')} 执行结束")