import paramiko
import time
import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')

f = open("ip_list.txt")

for line in f.readlines():
    ip_addr = line.strip()
    ssh_clinet = paramiko.SSHClient()
    ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_clinet.connect(hostname=ip_addr, username=username, password=password)
    print("Succ connect to ", ip_addr)
    command = ssh_clinet.invoke_shell()
    command.send("config t\n")
    command.send("ip ftp username python\n")
    command.send("ip ftp password python\n")
    command.send("file prompt quiet\n")
    command.send("end\n")
    command.send("copy running-config ftp://192.168.2.1\n")
    time.sleep(2)
    output = command.recv(65535)
    print(output.decode("ascii"))

f.close()
ssh_clinet.close()