'''
实验目的

登录设备，执行dis int bri收集设备端口概要信息，保存至本地目录。
处理回显保存的文本，规范化显示
'''

import paramiko
import time

username = 'python'
password = 'Admin@123'

for i in range(100,103):
    ip = '192.168.31.' + str(i)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,
                       password=password,look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 Layer3Switch-' + str(i) + ' ' + ip)
    # 关闭分屏功能
    command.send('screen-length 0 temporary\n')
    # 进入系统视图
    command.send('dis int bri\n')
    time.sleep(2)

    #抓取回显，放入output变量
    output = command.recv(65535).decode('ASCII')
    print(output)

    #保存结果到python脚本同目录下的result文件夹中
    # 注意，Windows的目录写法与Linux不同，遇到了需灵活调整
    f1 = open(f"result/{ip}_dis_int_bri.txt","w")
    f1.write(output)
    f1.close()

    #规范数据  用记事本打开，发现有很多空行，做如下操作
    with open(f"result/{ip}_dis_int_bri.txt", 'r') as f:
        with open(f"result/规范1_{ip}_dis_int_bri.txt", 'w') as f1:
            for line in f.readlines():
                if line.split():
                    f1.write(line)

    ssh_client.close()

'''规范数据（二）'''

#解决空行编码问题
for i in range(100, 103):
    ip = '192.168.31.' + str(i)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username,
                       password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 Layer3Switch-' + str(i) + ' ' + ip)
    # 关闭分屏功能
    command.send('screen-length 0 temporary\n')
    # 进入系统视图
    command.send('dis int bri\n')
    time.sleep(2)
    output = command.recv(65535).decode('ASCII').replace('\r', '')
    print(output)

    # 保存结果到python脚本同目录下的result文件夹中
    f1 = open(f"result/规范2_{ip}_dis_int_bri.txt","w")
    f1.write(output)
    f1.close()

    ssh_client.close()



