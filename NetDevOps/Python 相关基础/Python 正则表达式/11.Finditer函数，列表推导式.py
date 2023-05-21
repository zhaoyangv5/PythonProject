'''
Finditer函数，列表推导式
finditer函数。这个函数非常适合用来解析行列报文回显，如“display interface interface brief”、“display ip interface brief”之类的

Finditer函数会根据正则规则，匹配后返回一个有match对象组成的可迭代对象(iter)。
啥是可迭代对象呢？我自己的理解是你可以从某范围内，一个一个地把里面的东西给喊出来，这个范围就是一个可迭代对象

# >>> help(re.finditer)
re模块中finditer函数的帮助

finditer(pattern, string, flags=0)
    函数返回一个迭代器，这迭代器内容为字符串经正则规则处理命中的全部匹配项。匹配项与匹配项是不能重叠的。
    每个匹配项都是一个Match对象。

    如全部没匹配中，也是会返回迭代器。（只不过这个迭代器为空而已。）
'''

import re
from pprint import pprint

with open('output_from_cli.txt') as output:
    # 整个文本读进来
    output_text = output.read()

# 如必要可看一下读取的内容，格式是str
#print(output_text)

result = re.finditer(r'(\S+) +'
                     r'([\d./]+) +'
                     r'(up|down|\*down) +'
                     r'(up|down)',
                     output_text)

#如果写成一行可以这么写，上面分行的写法是为了更简洁好看一点而已，实际是等效的。
#result = re.finditer(r'(\S+) +([\d./]+) +(up|down|\*down) +(up|down)',output_text)

print(result)
print(type(result))

for match in result:
    print(match.groups())


'''第 2 步，解析display ip interface brief回显（列表推导式）'''

with open('output_from_cli.txt') as output:
    regex = r'(\S+) +([\d./]+) +(up|down|\*down) +(up|down)'
    result = [match.groups() for match in re.finditer(regex, output.read())]

# 1、re.finditer(regex, output.read())，这里返回了迭代器（上一步的内容）；
# 2、for match in ……，变量match在迭代其中挨个迭代，借助了for循环；
# 3、每次迭代，变量match又调用了方法groups()；
# 4、处理后结果被中括号[]括起来，形成列表赋值给变量result.

pprint(result)


'''第 3 步，温故知新日志例子（用finditer函数)'''

regex = (r'.*VlanId = (\d+), '
         r'MacAddress = \S+, '
         r'Original-Port = (\S+), '
         r'Flapping port = (\S+)\.')

ports = set()

with open('log.txt') as f:
    for each_match in re.finditer(regex, f.read()):
        vlan = each_match.group(1)
        ports.add(each_match.group(2))
        ports.add(each_match.group(3))

print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))