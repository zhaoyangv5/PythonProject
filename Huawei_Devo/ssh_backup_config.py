"""
这个是自动化登录设备配置备份的脚本
备份单独设备的代码
"""
import paramiko
import time

#参数区域
Devcies = {"192.168.31.100": ("huawei", "Admin@123")}
# Devcies = {"192.168.31.100": ("huawei", "aDmin@123"),
#            "192.168.31.101": ("huawei", "aDmin@1231")}
Ips = list(Devcies.keys())
usernames = [one[0] for one in list(Devcies.values())]
passwords = [one[1] for one in list(Devcies.values())]

#备份单独设备的代码
def save_config(ip, config):
    with open("{}.txt".format(ip), "w") as file :
        file.write(config)

def run_backup(ip,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)

    print('《=====您已成功登陆=====》', ip)
    command = ssh_client.invoke_shell()
    command.send("screen-length 0 temporary\n")
    # command.send('dis ip int brie\n')
    command.send('dis cu\n')
    # command.send("dis logbuffer\n")
    time.sleep(1)
    output = command.recv(65535)
    # print(output.decode('ascii'))
    # config = output.decode()
    configs = output.decode()
    config = configs.split("<HUAWEI>dis cu\r\n")[1].split("<HUAWEI>")[0] #去除头部尾部不需要的内容
    # print(config)
    print("-----------正在备份 {} 的配置-----------OK！！".format(ip))
    save_config(ip, config)

    ssh_client.close()
    print("-----------{} 的配置备份完成------------OK！！".format(ip))

#主进程
if __name__ == "__main__":
    for index in range(len(Ips)):
        # print(index)
        ip = Ips[index]
        username = usernames[index]
        password = passwords[index]
        run_backup(ip,username,password)


