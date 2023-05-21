'''
实验目的

（1）在Win10上部署FTP服务器，尝试手工登录网元完成一次配置文件推送。

（2）使用paramiko实现自动登录网元（Layer3Switch-x），批量推送配置文件到Win10上。
'''
import paramiko
import time

username = 'python'
password = '123'

iplist = ['192.168.11.11', '192.168.11.12', '192.168.11.13', '192.168.11.14', '192.168.11.15']

for ip in iplist:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username,
                       password=password, look_for_keys=False)

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 ' + ip)
    command = ssh_client.invoke_shell()

    command.send('ftp 192.168.11.2\n')
    time.sleep(0.5)
    command.send('python\n')
    time.sleep(0.5)
    command.send('123456\n')
    time.sleep(0.5)
    command.send('bin\n')
    command.send('put vrpcfg.zip ' + ip + '_vrpcfg.zip' + '\n')
    time.sleep(0.5)
    command.send('quit\n')
    time.sleep(0.5)

    output = command.recv(65535).decode('GB2312')
    print(output)

ssh_client.close()