'''
实验目的

Python 脚本 paramiko 登录一台交换机（如Layer3Switch-1），设置回显分页，参数为10。
回显信息如出现分页 more 字样，paramiko 继续送空格，直到结束。
处理回显信息，将分页字符等处理掉。
'''
import paramiko
import time
import re

ip = "192.168.31.100"
username = "python"
password = "Admin@123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
print("Successfully connected to ", ip)

command = ssh_client.invoke_shell()
command.send("screen-length 10 temporary \n")
command.send("disp cur \n")
time.sleep(0.5)

# 以上代码是现成的“套路”，直接用上即可，关键看下面。


# 定义一个字符串变量来装分页回显，每次拼接后就再赋值给它。
output = ""

# 这个 while 循环体很关键，为的是出现分页符就继续送指令（这里是送空格），然后分页结束后，它也能正常结束。
while True:
    page = command.recv(65535)
    # print(page)
    page = page.decode("ASCII")
    output += page
    time.sleep(0.1)
    if page.endswith('>') or page.endswith(']'):
        # 用这个判断也可以，标识应回到了系统视图或者用户视图（指令执行回显完毕的意思），不用再送空格了，跳出 while 循环。
        # if page[-1] in ['>',']']:
        break
    if "  ---- More ----" in page:
        command.send(" ")

# 优化回显（字符串方法)
# output = output.replace("  ---- More ----[16D                [16D",'')
# 优化回显（编解码辅助)
# output = output.replace("  ---- More ----\x1b[16D                \x1b[16D",'')
#正则表达式优化
# sub 此时要替换的内容可以是正则表达式，我们用 .* 把那方框位置给匹配掉了
output = re.sub(r"  ---- More ----.*16D", "", output)

print(output)
ssh_client.close()
