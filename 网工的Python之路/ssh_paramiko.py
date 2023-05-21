import paramiko
import time

ip = "10.211.55.100"
username = "huawei"
password = "huawei@123"

ssh_clinet = paramiko.SSHClient()    #调用paramiko的SSH方法
ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #让prarmiko接受SSH服务端提供的公钥，任何时候都需要
ssh_clinet.connect(hostname=ip, username=username, password=password, look_for_keys= True) #进行登录操作,默认是True,如果遇到公钥不对登录失败，
                                                                                           # 可以改为False

print("Sucessfully connect to ", ip)    #告知用户登录成功
command = ssh_clinet.invoke_shell()     # 唤醒思科思科IOS命令行shell
command.send("screen-length 0 temporary\n")
command.send("dis cu\n")



time.sleep(2)                         #由于Python一次性执行脚本，中间没有间隔时间，会导致某些命令遗留和回显不完成，调用time函数
output = command.recv(65535)          # 截取最大数回显65535字符的内容
print(output.decode("ascii"))         #回显内容格式为字节型字符串，打印出来的内容格式很难看，需要用decode解析为ASCII编码

ssh_clinet.close()





