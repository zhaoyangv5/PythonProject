import paramiko
import time
import getpass
import sys
import re
import socket

username = input('Enter your SSH username: ')
password = getpass.getpass('Enter your SSH password: ')

iplist = open('ip_list.txt', 'r+')


switch_upgraded = []
switch_not_upgraded = []
switch_with_tacacs_issue = []
switch_not_reachable = []

for line in iplist.readlines():
    try:
        ip_address = line.strip()
        ssh_clinet = paramiko.SSHClient()
        ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_clinet.connect(hostname=ip_address, username=username, password=password)
        print("Sucess to connect to " + ip_address)
        command = ssh_clinet.invoke_shell(width=300)
        command.send("show inventory | i PID: WS\n")
        time.sleep(1)
        command.send("show flash: | i c2960\n")
        time.sleep(1)
        command.send("show boot | i BOOT path\n")
        time.sleep(1)
        output = command.recv(65535)
        command.send("wr mem\n")
        switch_modle = re.search(r'WS-C2960\w?-\w{4,5}-L', output)
        ios_version = re.search(r'c2960\w?-\w{8,10}\d?-mz.\d{3}-\d{1,2}.\w{2,4}(.bin)?', output)
        boot_system = re.search(r'flash:.+mz.\d{3}-\d{1,2}\.\w{2,4}\.bin', output)
        if switch_modle.group() == "WS-C2960-24PC-L" and ios_version.group() == "c2960-lanbasek9-mz.122-55.SE.bin" \
                and boot_system.group() == "flash:c2960-lanbasek9-mz.122.55.SE12.bin" \
                or boot_system.group() == "flash:/c2960-lanbasek9-mz.122-55.SE12.bin":
            switch_upgraded.append(ip_address)
        elif switch_modle.group() == "WS-C2960S-F24PS-L" and ios_version.group() == "c2960s-universalk9-mz.150-2.SEll.bin" \
                and boot_system.group() == "flash:c2960s-universalk9-mz.150-2.SEll.bin" \
                or boot_system.group() == "flash:/c2960s-universalk9-mz.150-2.SEll.bin":
            switch_upgraded.append(ip_address)
        elif switch_modle.group() == "WS-C2960X-F24PS-L" and ios_version.group() == "c2960x-universalk9-mz.152-2.E8.bin" \
                and boot_system.group() == "flash:c2960x-universalk9-mz.152-2.E8.bin" \
                or boot_system.group() == "flash:/c2960x-universalk9-mz.152-2.E8.bin":
            switch_upgraded.append(ip_address)
        else:
            switch_not_upgraded.append(ip_address)
    except paramiko.ssh_exception.AuthenticationException:
        print("TACACS is not working for " + ip_address + ".")
        switch_with_tacacs_issue.append(ip_address)
    except socket.error:
        print(ip_address + "is not reachable.")
        switch_not_reachable.append(ip_address)

iplist.close()
ssh_clinet.close()

print('\nTACACS is not working for below switches: ')
for i in switch_with_tacacs_issue:
    print(i)

print('\nbelow switches are not reachable: ')
for i in switch_not_reachable:
    print(i)

print('\nbelow switches IOS version are up_to_date: ')
for i in switch_upgraded:
    print(i)

print('\nbelow switches IOS version are not uodated yet: ')
for i in switch_not_upgraded:
    print(i)



