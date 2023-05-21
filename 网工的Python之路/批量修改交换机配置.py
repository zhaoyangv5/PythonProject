import paramiko
import time
import getpass
import sys

usernanme = input("Username: ")
password = getpass.getpass("password: ")
ip_file = sys.argv[1]
cmd_file = sys.argv[2]   # sys.argv[0]一般是被调用的.py的脚本文件名，例：python3.8 lab1.py ip.txt cmd.txt

iplist = open(ip_file, "r")
for line in iplist.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, usernanme=usernanme, password=password)
    print("You are succ connect to " + ip)
    command = ssh_client.invoke_shell()
    cmdlist = open(cmd_file, "r")
    cmdlist.seek(0)
    for line in cmdlist.readlines():
        command.send(line + "\n")
        time.sleep(1)
        cmdlist.close()
        output = command.recv(65534)
        print(output.decode("ascii"))

iplist.close()
ssh_client.close()