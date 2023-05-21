#coding=utf-8

import threading
from queue import Queue
import time
from netmiko import ConnectHandler

f = open('ip_list.txt')
threads = []

def ssh_session(ip, output_q):
    command = ["line vty 5 15", "login local", "exit"]
    sw = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'python',
        'password': '123'
    }
    ssh_session = ConnectHandler(**sw)
    output = ssh_session.send_config_set(command)
    print(output)

print(f"程序于{time.strftime('%X')} 开始执行\n")
for ips in f.readlines():
    t = threading.Thread(target=ssh_session, args=(ips.strip(), Queue()))  #Queue是线程间最常用的数据交换模式，先进先出规则，Netmiko实现多线程必备
    t.start()
    threads.append(t)

for i in threads:
    i.join()
print(f"\n程序于{time.strftime('%X')}结束")
