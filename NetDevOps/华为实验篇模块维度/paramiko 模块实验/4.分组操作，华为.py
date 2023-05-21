'''
实验目的

192.168.31.100、192.168.31.102归类为组1，
模拟华为交换机版本：VRP (R) software, Version 5.110 (S5700 V200R001C00)，进入 vlanif 1 ，执行 description Python_G1。
192.168.31.101、192.168.31.108归类为组2，
模拟华为交换机版本：VRP (R) software, Version 5.110 (S3700 V100R001C00)，进入 vlanif 1 ，执行 description Python_G2。
'''
'''
python temp.py a b c d
说明：命令行运行temp.py模块，同时传入4个参数：a、b、c、d
sys.argv == ["temp.py","a","b","c","d"] #sys.argv是持有5个元素的list对象
sys.argv[0] == "temp.py" #第1个元素为模块名“temp.py”
sys.argv[1] == "a" #第2个元素为"a"
sys.argv[2] == "b" #第3个元素为"b"
sys.argv[3] == "c" #第4个元素为"c"
sys.argv[4] == "d" #第5个元素为"d"
'''

import paramiko
import time
import getpass
import sys

username = input("username: ")
password = getpass.getpass("Password: ")
ip_file = sys.argv[1]
cmd_file = sys.argv[2]

iplist = open(ip_file, 'r')
for line in iplist.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username,
                       password=password, look_for_keys=False)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 ' + ip)
    command = ssh_client.invoke_shell()
    cmdlist = open(cmd_file, 'r')
    cmdlist.seek(0)
    for line in cmdlist.readlines():
        each_command = line.strip()
        command.send(each_command + '\n')
        time.sleep(0.5)
    cmdlist.close()

    output = command.recv(65535).decode('ASCII')
    print(output)

ssh_client.close()