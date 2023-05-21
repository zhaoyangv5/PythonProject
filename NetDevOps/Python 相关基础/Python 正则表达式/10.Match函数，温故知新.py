'''
Match函数概述
在字符串中，查找与模板规则匹配的子字符串。
如果找到子字符串，则返回 Match 对象。
如果未能找到，则返回 None。
我观察的match()函数较search()函数唯一的区别是match()函数只能严格从最开始执行匹配，而search()函数不用这么“死板”
'''
'''
实验目的

参照search()函数的实验目的，我们用match()函数来完成。

（1）正则表达式匹配单行日志。

（2）在（1）的基础上，读取日志文件，逐行匹配。
'''

import re

#第 1 步，体验match()与search()异同
log = 'Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.'
match = re.search(r'VlanId = (\d+), MacAddress = \S+, Original-Port = (\S+), Flapping port = (\S+)\.',log)
print(match.groups())

# match = re.match(r'VlanId = (\d+), MacAddress = \S+, Original-Port = (\S+), Flapping port = (\S+)\.',log)
# print(match.groups())       #AttributeError: 'NoneType' object has no attribute 'groups', match()函数并没有匹配中

#在正则表达式前面加 .* ，即匹配任意，这样就可以满足从最开始匹配的要求了
match = re.match(r'.*VlanId = (\d+), '
                 r'MacAddress = \S+, '
                 r'Original-Port = (\S+), '
                 r'Flapping port = (\S+)\.',log)
print(match.groups())

# '''第 2 步，日志处理（依然是复习）'''

regex = (r'.*VlanId = (\d+), '
         r'MacAddress = \S+, '
         r'Original-Port = (\S+), '
         r'Flapping port = (\S+)\.')

ports = set()

with open('log.txt') as f:
    for line in f:
        match = re.match(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))

print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))


