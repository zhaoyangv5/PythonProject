'''
Compile函数概述
正则表达式好比一个设计图纸，使用过程好比做了个样品，用完了这个样品就扔掉了，下次要用还得再根据设计图纸重头来过。
正则表达式预编译好比根据图纸做了一个生产模具，这次可以用，下次也可以用，而且不再需要从设计图纸开始了，直接用模具一压一成型.
除提高效率以外，Compile的另一个作用就是隔离了正则表达式的撰写和使用。比如工厂，设计产品一拨人，生产产品一拨人，严格分工后各干各的。
我们知道撰写正则表达式“本身就是个难题”了，如果能把撰写和使用分离，是不是能更好地聚焦关注点呢？答案自然是肯定的
'''

import re

regex = re.compile(r'\S+ +\d+ +\S+ +\S+ + \S+ +\w+ +\S+')
print(regex, type(regex))        #<class 're.Pattern'>   #regex变量指向一个正则表达式经编译后的对象，是Pattern类型

#查看Pattern对象常用方法
#无论用regex还是用re.Pattern传输dir函数，其结果都是一样的
print([method for method in dir(regex) if not method.startswith('_')])
print([method for method in dir(re.Pattern) if not method.startswith('_')])

#这里有类和对象的概念，re.Pattern是一个类，regex是这个类的实例，我们叫它对象吧

regex = re.compile(r'\S+ +\d+ +\S+ +\S+ + \S+ +\w+ +\S+')
line = '4c1f-ccd0-2d35 1           -      -      Eth0/0/5        dynamic   0/-      '
match = regex.search(line)                  #search方法需要被对象regex调用才能使用
print(match.group())

#对象regex中涉及的正则表达式已经被编译完成了，后面可直接多次调用其search方法处理其它的文本
line2 = '4c1f-ccb5-2a33 105           -      -      Eth0/0/2        dynamic   0/-   '
match2 = regex.search(line2)
print(match2.group())


#日志解析实战案例

regex = re.compile(r'.*VlanId = (\d+), '
                   r'MacAddress = \S+, '
                   r'Original-Port = (\S+), '
                   r'Flapping port = (\S+)\.')

ports = set()

with open('log.txt') as f:
    for m in regex.finditer(f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))

print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))


#re.compile两特性小选项
# pos	指定匹配开始位置
# endpos	指定匹配结尾位置

regex = re.compile(r'\S+ +\d+ +\S+ +\S+ + \S+ +\w+ +\S+')
line = '4c1f-ccd0-2d35 1           -      -      Eth0/0/5        dynamic   0/-      '
print(regex.search(line).group())
print(regex.search(line, 3).group())        #设置pos单个索引的情况，pos=3，即regex.search(line,3)
print(regex.search(line[3:]).group())       #处理结果等效于regex.search(line[3:])

# 同时设置pos和endpos两个索引的情况，pos=3，endpos=68，即regex.search(line,3,68)，其处理结果等效于regex.search(line[3:68])
print(len(line))
print(regex.search(line, 3, 68).group())
print(regex.search(line[3:68]).group())

#强烈建议用re.compile进行预编译，这样效率会大为提升
