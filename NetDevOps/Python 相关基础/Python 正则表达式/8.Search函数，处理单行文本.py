'''
Search函数概述

search()函数的主要功能：

在字符串中，查找与模板规则匹配的子字符串。
如果找到子字符串，则返回 Match 对象。
如果未能找到，则返回 None。
如果你只想在字符串中找一个匹配项，而非多个（规则匹配字符串全部或一部分），那使用search()函数就再合适不过了
'''
'''
实验目的

（1）正则表达式匹配单行日志。

（2）在（1）的基础上，读取日志文件，逐行匹配
'''

import re

# data = '''Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.
# Sep 26 2021 23:11:08-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.
# Sep 26 2021 23:11:10-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/2, Flapping port = GE0/0/3. Please check the network accessed to flapping port.
# Sep 26 2021 23:11:15-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/3, Flapping port = GE0/0/1. Please check the network accessed to flapping port.
# '''

# 第 1 步，正则处理一行日志
# (\d+)	提取vlan号
# \S+	仅匹配mac地址，不不提取
# (\S+)	提取mac漂移的端口

log = 'Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.'
match = re.search(r'VlanId = (\d+), '
                  r'MacAddress = (\S+), '
                  r'Original-Port = (\S+), '
                  r'Flapping port = (\S+)\.', log)
print(match.groups())

# 第 2 步，正则逐行处理日志
regex = (r'VlanId = (\d+), '
                  r'MacAddress = (\S+), '
                  r'Original-Port = (\S+), '
                  r'Flapping port = (\S+)\.')

ports = set()       #把数据装入集合set去重

with open('log.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(3))
            ports.add(match.group(4))
print(ports)
# print(', '.join(ports)) #.join()表示将port里字符串以， 分开，再拼接为一个新的字符串
# print(type(', '.join(ports)))

print('Loop between ports {} in vlan {}'.format(ports, vlan))
print('Loop between ports {} in vlan {}'.format(', '.join(ports), vlan))

