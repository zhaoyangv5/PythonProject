"""
实验目的

用正则表达式，配合python最基础的语法。

（1）读取配置文件中info-center的源IP地址10.10.10.10，放入变量info_center_ip中；

（2）读取配置文件中LoopBack0口的IP地址10.10.10.10，放入变量inter_loop0_ip中；

（3）比较info_center_ip与inter_loop0_ip两变量是否一致。

"""
"""读取info-center源IP地址"""

import re
info_center_ip = ''

f = open('demo.txt')
line = f.readline()
while line:    #把found标志位换成line来控制while循环
    match = re.search('\S+ loghost \S+ source-ip (\S+)',line)
    if match:
        info_center_ip = match.groups()[0]
        #print(match.groups())
        print(info_center_ip)
        #break，如果找到了就直接跳出循环，不往下找了，可用break
    line = f.readline()
f.close()

"""读取LoopBack0口IP地址"""

inter_loop0_ip = ''

f = open('demo.txt')
line = f.readline()
while line:
    if line.startswith('interface LoopBack0'):
        line = f.readline()
        while line.startswith(' '):
            match = re.search(' ip address (\S+)',line)
            if match:
                inter_loop0_ip = match.groups()[0]
                print(inter_loop0_ip)
                #break
            line = f.readline()
    #if inter_loop0_ip:
        #break
    line = f.readline()
f.close()

if info_center_ip==inter_loop0_ip:
    print(f"核查无误，均为{info_center_ip}")
else:print(f"核查有误！！！\
           \ninfo_center_ip：{info_center_ip}\
           \ninter_loop0_ip：{inter_loop0_ip}")