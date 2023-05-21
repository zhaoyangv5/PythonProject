import paramiko
import time
import getpass
import sys
import socket

usernanme = input("Username: ")
password = getpass.getpass("password: ")
ip_file = sys.argv[1]
cmd_file = sys.argv[2]

switch_with_autentiaction_issue = []
swtich_not_reachabel = []

iplist = open(ip_file, 'r')
for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=usernanme, password=password,look_for_keys=True)
        print ("You have sucss connect to ", ip)
        command = ssh_client.invoke_shell()
        cmdlist =open(cmd_file, 'r')
        cmdlist.seek(0)
        for line in cmdlist.readlines():
            command.send(line + "\n")
        time.sleep(2)
        cmdlist.close()
        output = command.recv(65535)
        print(output.decode("ascii"))
    except paramiko.ssh_exception.AuthenticationException:
        print("user authentication failed for " + ip + ".")
        switch_with_autentiaction_issue.append(ip)
    except socket.error:
        print(ip + " is not reachable")
        swtich_not_reachabel.append(ip)

iplist.close()
ssh_client.close

print('\nUser authentication failed for below switches: ')
for i in switch_with_autentiaction_issue:
    print(i)

print('\nBeblow swtiches are not reachable: ')
for i in swtich_not_reachabel:
    print(i)
