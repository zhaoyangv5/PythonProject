'''
分组概述（Grouping）
正则表达式中，我们用一个小括号括起来的部分，简单理解就是一个分组。
正则“模板”在处理原始文本时，除了会把整个小括号括起来的部分看成一个整体外，还有“提取”、“捕获”的功能

Python有两种分组形式：
按序分组（Numbered groups）
按名分组（Named groups
'''
import re
import json

print('\n'+'*'*20+'按序分组（Numbered groups）'+'*'*25)

''' 按序分组（Numbered groups）'''
line = 'Vlanif1          192.168.11.11/24     up         up'
print(re.search(r'(\S+)\s+([\w.]+)/', line).group())
# (\S+)	第1组，匹配非空字符
# ([\w.]+)	第2组，匹配数字或字母或点(.)

'''按序常规操作'''
match = re.search(r'(\S+)\s+([\w.]+)/', line)
print(match.group(0))       #Vlanif1          192.168.11.11/
print(match.group(1))       #Vlanif1
print(match.group(2))       #192.168.11.11
# group(1)、group(2)按组捕获，group(0)则返回整个匹配文本

'''灵活编排'''
print(match.group(1,2))         #('Vlanif1', '192.168.11.11')
print(type(match.group(1,2)))   #<class 'tuple'>
print(match.group(1,2,1))       #('Vlanif1', '192.168.11.11', 'Vlanif1')

'''按索引捕获'''
#在Python 3.6以后，我们还可通过类似列表的索引方式，来提取值
print(match[0])     #Vlanif1          192.168.11.11/
print(match[1])     #Vlanif1

'''方法groups()全量捕获'''
print(match.groups())           #('Vlanif1', '192.168.11.11')


print('\n'+'*'*20+'按名分组（Named groups）'+'*'*25)

'''按名分组（Named groups）'''

'''命名基础语法'''
# 给分组进行命名的语法是这样的：
# (?P<name>regex)
# ?P  固定套路
# <name>  组名，字典的键
# regex   常规正则规则，捕获后即字典该键对应的值

line = 'Vlanif1          192.168.11.11/24     up         up'
match = re.search('(?P<interface>\S+)\s+(?P<ipaddress>[\w.]+)/', line)  #通常，一开始我们可以不要取名字，先把正则表达式都写好了匹配中了，再来把名字“安插”进去
print(match.group('interface'))     #Vlanif1
print(match.group('ipaddress'))     #192.168.11.11
print(match.group('interface', 'ipaddress', 'ipaddress'))       #('Vlanif1', '192.168.11.11', '192.168.11.11')


'''按名字典捕获 groupdict()'''
line = 'Vlanif1          192.168.11.11/24     up         up'
match = re.search('(?P<interface>\S+)\s+(?P<ipaddress>[\w.]+)/', line)  #通常，一开始我们可以不要取名字，先把正则表达式都写好了匹配中了，再来把名字“安插”进去
print(match.groupdict())       # {'interface': 'Vlanif1', 'ipaddress': '192.168.11.11'}

match = re.search('(?P<interface>\S+)\s+(?P<ipaddress>[\w.]+)/.*(?P<status>up|down)\s+(?P<protocol>up|down)', line)
print(match.groupdict())        # {'interface': 'Vlanif1', 'ipaddress': '192.168.11.11', 'status': 'up', 'protocol': 'up'}

match = re.search('(?P<interface>\S+)\s+(?P<ipaddress>[\w.]+/+\d+).*(?P<status>up|down)\s+(?P<protocol>up|down)', line)
print(match.groupdict())        # {'interface': 'Vlanif1', 'ipaddress': '192.168.11.11/24', 'status': 'up', 'protocol': 'up'}


'''读出的字典类型转为json类型'''
d = match.groupdict()

with open('test.json', 'w') as f:
    json.dump(d, f, sort_keys=True, indent=2)