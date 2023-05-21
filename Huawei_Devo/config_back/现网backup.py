# coding: utf-8
import paramiko
import time



#参数区域
# Devcies = {"172.16.24.57": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY")}
Devcies = {"172.16.24.49": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.50": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.51": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.52": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.53": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.54": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.55": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.56": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.57": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),
           "172.16.24.58": ("yingjiweihu", "C=4rc3AVr&xwFb9@drTvX%7wY"),}
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
    command.send("more off\n")
    # command.send('dis ip int brie\n')
    command.send('show running-config\n')
    # command.send("dis logbuffer\n")
    time.sleep(1)
    output = command.recv(65535)
    # print(output.decode('ascii'))
    print(type(output))
    config = output.decode(errors='replace')
    # print(output.decode())
    # config = configs.split("<HUAWEI>dis cu\r\n")[1].split("<HUAWEI>")[0] #去除头部尾部不需要的内容
    print(config)
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

