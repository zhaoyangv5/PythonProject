import paramiko
import time
import getpass


username = input('Username: ')
password = getpass.getpass('Password: ')

for i in range(11, 16):
    ip = "192.168.2." + str(i)
    ssh_clinet = paramiko.SSHClient()
    ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_clinet.connect(hostname=ip, username=username, password=password, look_for_keys=True)
    print("Sucessfully connect to ", ip)
    command = ssh_clinet.invoke_shell()
    command.send("configure terminal\n")
    for n in range(10, 21):
        print("Creating VLAN " + str(n))
        command.send("vlan " + str(n) + "\n")
        command.send("name Python_VLan " + str(n) + "\n")
        time.sleep(3)

    command.send("end\n")
    command.send("wr mem\n")
    output = command.recv(65535)
    print(output.decode("ascii"))

    ssh_clinet.close()