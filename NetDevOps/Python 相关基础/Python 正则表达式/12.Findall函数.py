'''
Findall函数概述

用于在字符串中搜索所有不重叠的匹配。
返回
如未设置捕获组，则返回符合正则规则的字符串列表。
如已设置捕获组，且捕获组仅有一个，则依然返回符合正则规则的字符串列表。
如已设置捕获组，且捕获组多于一个，则返回符合正则规则的元组列表。
'''
import re
from pprint import pprint


#编写正则规则及Python脚本执行
mac_table = open("mac_table.txt").read()
result = re.findall(r'\S+ +\d+ +\S+ +\S+ +Eth\S+ +\S+ +\S+', mac_table)
print(result)
pprint(result)          #返回字符串


#调整正则表达式（一个捕获组）
result = re.findall(r'(\S+) +\d+ +\S+ +\S+ +Eth\S+ +\S+ +\S+',mac_table)
pprint(result)      #Findall函数马上调整了策略，转而进行捕获提取，返回的依然是字符串列表


#调整正则表达式（多个捕获组）
result = re.findall(r'(\S+) +(\d+) +\S+ +\S+ +(Eth\S+) +\S+ +\S+',mac_table)
pprint(result)      #把捕获组们精心打包成一个个元组，再放在一个大列表中一并返回


# 温故知新日志例子（用findall函数)
regex = (r'.*VlanId = (\d+), '
         r'MacAddress = \S+, '
         r'Original-Port = (\S+), '
         r'Flapping port = (\S+)\.')

ports = set()

with open('log.txt') as f:
    result = re.findall(regex, f.read())
    # print(result)             #生成一个元组的列表
    for vlan, port1, port2 in result:
        ports.add(port1)
        ports.add(port2)


print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))