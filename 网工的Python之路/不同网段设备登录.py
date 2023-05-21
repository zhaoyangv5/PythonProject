import paramiko
import time
from getpass import getpass

username = input("Username: ")
password = getpass('password: ')


f = open("ip_list.txt", "r")
for line in f.readlines():
    ip = line.strip()
    ssh_clinet = paramiko.SSHClient()
    ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_clinet.connect(hostname=ip, password=password, look_for_keys=True)
    print("Sucessfully connect to ", ip)
    remote_connection = ssh_clinet.invoke_shell()
    remote_connection.send("config t\n")
    remote_connection.send("router eigrp 1\n")
    remote_connection.send("end\n")
    remote_connection.send("wr mem\n")
    time.sleep(3)
    output = remote_connection.recv(65535)
    print(output.decode("ascii"))

f.close()
ssh_clinet.close()



