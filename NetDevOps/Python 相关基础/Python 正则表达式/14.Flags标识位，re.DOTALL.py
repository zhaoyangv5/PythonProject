'''
Python中普通查找函数也好，预编译函数也好，我们都可以通过一些附加标识位来影响正则匹配过程。本实验主要介绍re.DOTALL
正则表达式增加Flags标识位是为了让匹配适应力更强，比如IGNORECASE可以忽略大小写，这在处理一些驼峰标识的文本材料时就非常有用。大体上有这么写标识位。

re.ASCII	re.A	只考虑ASCII
re.IGNORECASE	re.I	忽略大小写
re.MULTILINE	re.M	多行模式
re.DOTALL	re.S	匹配所有
re.VERBOSE	re.X	忽略空白，提增可读性
re.LOCALE	re.L	跟随本地设置（极少用，不推荐）
re.DEBUG	--	显示调试

'''
import re

#re.DOTALL
#如不设置re.DOTALL这个Flag标识位，符号“.”匹配除换行符外的一切。而一旦设置了这个标识位，符号“.”将啥都匹配

#第 1 步，解析非重复结构文本
regex = r'Router ID: (\S+) +Address: (\S+).+Neighbor is up for (\S+)'

with open('ospf_peer.txt') as f:
    ospf_peer = f.read()

#不使用Flag标识位
print(re.search(regex, ospf_peer))          #None

#使用Flag标识位
#这里用我用到了.+配合了re.DOTALL标识位，实际可以理解成把多行文本看成一行，然后进行全匹配
#但是.+会带来一个贪婪和非贪婪的问题
print(re.search(regex, ospf_peer, re.DOTALL).groups())      #('4.4.4.4', '47.1.1.4', '00:00:51')


##但是.+会带来一个贪婪和非贪婪的问题
with open('ospf_peer1.txt') as f:
    ospf_peer1 = f.read()

print(re.search(regex, ospf_peer1, re.DOTALL).groups())      #('4.4.4.4', '47.1.1.4', '00:00:50') 结果不对

'''正则规则中有一组.+符号，还觉得吧，默认情况下+是贪婪模式，也即尽可能多的匹配'''
'''因为我们开启了re.DOTALL标识。如果re.DOTALL标识不设置，那就没有这个问题，因为匹配规则的作用域就在一行里面而已，不会跨行'''

#这种情况下，我们必须把贪婪模式给它禁用了，再配合一下finditer函数，才有可能匹配出我们想要的

regex = r'Router ID: (\S+) +Address: (\S+).+?Neighbor is up for (\S+)'     # .*? 非贪婪模式

with open('ospf_peer1.txt') as f:
    ospf_peer1 = f.read()

match = re.finditer(regex, ospf_peer1, re.DOTALL)
# print(match)
for m in match:
    # print(m.group(1))
    # print(m.group(2))
    # print(m.group(3))
    print(m.groups())