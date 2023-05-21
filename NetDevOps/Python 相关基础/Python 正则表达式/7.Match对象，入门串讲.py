'''
Python中与正则表达式相关的通常是re模块，其主要的方法有：

match - 从头开始找
search - 根据正则模板查找到第一匹配处
findall - 根据正则模板查找全部，组成列表返回
finditer - 根据正则模板查找全部，组成迭代器返回
compile - 对正则表达式进行编译，此后可再用re模块的其它方法（无它，就是多次查询的场景下，效率高些）
fullmatch - 整行匹配
除了搜索匹配外，还有2个其它功能：

re.sub - 替换字符串
re.split - 分列
'''

import re

'''Match对象实战'''
# 在re模块中，一旦搜索匹配命中了，如下的几个方法就返回一个叫“Match”的对象。
# search
# match
# finditer

#第 1 步，创建一个Match对象实例

log = 'Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, ' \
      'VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. ' \
      'Please check the network accessed to flapping port.'
template = r'.* VlanId = (\d+), MacAddress = (\S+), Original-Port = (\S+), Flapping port = (.*)\.\s'
match = re.search(template, log)
print(match)

#第 2 步，练习group方法
#group方法，如果不加参数，返回匹配到的字符串，匹配了多少就返回了多少
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(4))

#第 3 步，练习groups方法
#把您正则表达式中的小括号分组后的“子组”，都给捕获提取了，按顺序组成一个元组
print(match.groups())


#增加第5个小括号。看看这条日志是不是以“Please check the network accessed to flapping port.”结尾？
#如果是就返回None，如果不是就还能匹配到实际东西
template1 = r'.* VlanId = (\d+), MacAddress = (\S+), Original-Port = (\S+), Flapping port = (.*)\.\s.* port.(\w+)?'
print(re.search(template1, log).groups())

#可以通过修改groups方法的参数default来设置如果匹配不中要填入啥
print(re.search(template1, log).groups('后面没有东西了'))

#第 4 步，练习groupdict方法
template3 = r'.* VlanId = (?P<vlan>\d+), MacAddress = (?P<mac>\S+), Original-Port = (?P<originalport>\S+), Flapping port = (?P<flappingport>.*)\.\s'
print(re.search(template3, log).groupdict())

match = re.search(template3, log)

#第 5 步，练习start、end方法
#这两个方法返回匹配项在原字符串中的索引位置
print(len(log))
print(match.start())
print(match.end())

print(match.start(2))       #145
print(match.end(2))         #159
print(match.group(2))       #0000-5e00-0136  正好159-145=14

print(match.start('mac'))   #145
print(match.end('mac'))     #159

# 第 6 步，练习span方法
#span方法返回整个正则表达式匹配在原字符串的范围索引。
print(match.span())             #(0, 211)
print(match.span('mac'))        #(145, 159)
print(match.span('vlan'))       #(128, 130)
print(match.span(1))            #(128, 130)

