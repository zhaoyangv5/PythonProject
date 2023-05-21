'''
subprocess
Subprocess模块允许启动一新进程，连接输入/输出/错误管道，获得子进程返回码。这个模块目标是代替一些老模块，比如os.system和os.spawn
'''

import subprocess

# result = subprocess.run(['ping', '-c', '3', '192.168.31.1'],stdout=subprocess.PIPE)
# print(type(result))
# print(result.stdout)
# print(result.stdout.decode('gbk'))
#
# #方法subprocess.run还有一个参数“encoding”
# result_p = subprocess.run(['ping', '-c', '3', '192.168.31.1'], stdout=subprocess.PIPE, encoding='gbk' )
# print(result_p.stdout)      #如调用subprocess.run时加了encoding参数，则结果就自动decode好了，返回str类型。

'''telnetlib'''

import telnetlib
import time

# user = "python"
# password = "123"
#
# tn = telnetlib.Telnet("192.168.11.11")
# tn.read_until(b"Username:")
# tn.write(user.encode('ascii') + b"\n")  #模块中，read_until函数和write函数接收的是bytes类型的参数，所以必须进行编码转换（encode）
# tn.read_until(b"Password:")
# tn.write(password.encode('ascii') + b"\n")
#
# tn.write(b"screen-length 0 temporary\n")
# tn.write(b"display ip int bri\n")
# output = tn.read_very_eager().decode('ascii')   #模块中，read_very_eager方法返回的同样是bytes类型的参数，所以返回值要解码转换（decode）
# print(output)


'''
pexpect
pexpect模块的run函数，参数接收一个str类型，返回值却是一个bytes类型。
'''
import pexpect

output = pexpect.run('ls -ls')
print(output)
print(output.decode('utf-8'))
print(type(output))

output = pexpect.run('ls -ls', encoding='utf-8')
print(output)
print(type(output))             #加了encoding参数，则结果就自动decode好了，返回str类型


'''文件操作'''

import os
print(os.getcwd())

f = open('wgst.txt')
print(f)

with open('wgst.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
