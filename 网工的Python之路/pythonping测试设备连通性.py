"""
利用pythonping 测试网段多少交换机管理IP可达，并对可达的交换机查看物理接口情况
172.16.0.x~~172.16.4.x
"""

from pythonping import ping
import os
import re
import time
from datetime import datetime
import socket
import getpass
import paramiko

#ping

if os.path.exists('reachable_ip.txt'):
    os.remove('reachable_ip.txt')

third_octet = range(5)
last_octet =range(1, 255)

for ip3 in third_octet:
    for ip4 in last_octet:
        ip = '172.16.' + str(ip3) + '.' + str(ip4)
        ping_result = ping(ip)
        f = open('reachable_ip.txt', 'a')
        if 'Reply' in str(ping_result):
            print(ip + ' is reachable. ')
            f.write(ip + '\n')
        else:
            print(ip + ' is not reachable. ')

f.close()


#查看端口情况

username = input('Enter your SSH username: ')
password = getpass.getpass('Enter your SSH password: ')
now = datetime.now()
date = "%s-%s-%s" % (now.month, now.day, now.year)
time_now = "%s:%s:%s" % (now.hour, now.minute, now.second)

switch_with_tacacs_issue = []
switch_not_reachable = []
total_number_of_up_port = 0
iplist = open('reachable_ip.txt','r')
number_of_switch = len(iplist.readlines())
total_number_of_ports = number_of_switch * 48

iplist.seek(0)
for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=username, password=password)
        print("\nYou have success connect to ", ip)
        command = ssh_client.invoke_shell()
        command.send("term len 0\n")
        command.send('show ip int b | i ip\n')
        time.sleep(1)
        output = command.recv(65535)
        #print(output.decode("ascii"))
        search_up_port = re.findall(r'GigabitEthernet', output)
        number_of_up_port = len(search_up_port)
        print(ip + " has " + str(number_of_up_port) + " ports up.")
        total_number_of_up_port += number_of_up_port
    except paramiko.ssh_exception.AuthenticationException:
        print("TACACS is not working for " + ip + ".")
        switch_with_tacacs_issue.append(ip)
    except socket.error:
        print(ip + " is not reachable.")
        switch_not_reachable.append(ip)
    iplist.close()

    print("\n")
    print("There are totally " + str(total_number_of_ports) + "ports available in the network")
    print(str(total_number_of_up_port) + " ports are currently up.")
    print("port ip rate is %.2f%%" % (total_number_of_up_port /float(total_number_of_ports) * 100))
    print('\nTACACS is not working for below switchs: ')
    for i in switch_with_tacacs_issue:
        print(i)
    print("\nBelow switches are not reachable: ")
    for i in switch_not_reachable:
        print(i)
    f = open(date + ".txt", "a+")
    f.write('AS of ' + date + " " + time_now)
    f.write("\n\nhere are totally " + str(total_number_of_ports) + "ports available in the network")
    f.write("\n" + str(total_number_of_up_port) + " ports are currently up.")
    f.write("port ip rate is %.2f%%" % (total_number_of_up_port /float(total_number_of_ports) * 100))
    f.write("\n************************************************\n\n")
    f.close()