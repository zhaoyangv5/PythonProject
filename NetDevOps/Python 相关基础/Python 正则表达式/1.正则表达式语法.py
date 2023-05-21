'''
正则表达式是由普通字符和特殊字符组成的序列，可以称之为“模板”。凭借它，我们在文本中查找、搜索甚至替换特定信息，便有章可循了
正则表达式作用：
（1）在CLI命令回显中，提取我们想要的信息，检查配置设置是否准确。
（2）按照我们制定的模板规则，解析大篇幅命令回显或配置。
（1）从报文回显中提取或过滤出设备版本、运行时间、端口up/down等信息。
（2）在老长老长的LOG日志中捕捉你想要的，在老长老长的配置中检查接口配置是否符合规范等。
'''
import re

print('\n'+'*'*20+'方法search()'+'*'*25)

'''
方法search() 

match = re.search(pattern, string, flags=0)    # 语法规则！
pattern	正则表达式内容，可以叫“匹配模板”
string	待匹配字符串，如指令回显，或配置。
flags	更改正则行为，初学先忽略，后面再介绍。
1、以pattern作用于string，若匹配中，则返回一个Match对象（仅第一处匹配）；若匹配不中，则返回None
2、方法search()有个特性：如果有好几处能匹配中，方法search()返回的Match对象只包含第1处匹配中的信息
'''
int_line  = 'Route Port,The Maximum Transmit Unit is 1500'
match = re.search('The Maximum Transmit', int_line)
print(match)    #<re.Match object; span=(11, 31), match='The Maximum Transmit'>
#报文回显放入变量int_line中。在该变量中查找子字符串The Maximum Transmit。如果找得到，方法search()会将其打包成一个Match对象。该对象赋值给变量match
'''Match对象有一些方法，比如我们调用方法group()，即可得到匹配文本'''
'''如果没有匹配到，方法search()返回None，则变量match也就只是None了'''
print(match.group())


print('\n'+'*'*20+'特殊字符匹配'+'*'*25)

'''
包含特殊字符匹配
\d	匹配任何十进制数字；相当于类 [0-9]
+	前一个字符匹配一次或者多次
\d+	匹配一个或多个任何十进制数字
\S+	匹配一个或多个任何非空白字符
\.	.点为特殊字符，可匹配任意字符；加\转义，去除特殊，\.只匹配字符点.
()	小括号，表示分组/子组，这个有妙用
'''
int_line  = 'Route Port,The Maximum Transmit Unit is 1500'
match = re.search('The Maximum Transmit Unit is \d+', int_line)
print(match.group())


print('\n'+'*'*20+'分组（子组、捕获组）'+'*'*25)

'''分组（子组、捕获组）'''
log = 'Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.'
log2 = 'VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. '

#写一个正则表达式
re_template = r'VlanId = (\d+), MacAddress = (\S+), Original-Port = (\S+), Flapping port = (\S+)\.'
match = re.search(re_template, log2)
print(match)        #<re.Match object; span=(0, 91), match='VlanId = 54, MacAddress = 0000-5e00-0136, Origina>
print(match.group())

#用上了小括号()，进行了分组，所以有了子组概念。子组概念就是由小括号括起来的那一部分，一个小括号就叫一个子组，也叫捕获组
print(match.group(0))       # 此时拿到匹配中的字符串，match.group(0)和match.group()此处并无差异！
print(match.group(1))       # 54
print(match.group(2))       # 0000-5e00-0136
print(match.group(3))       # GE0/0/1
print(match.group(4))       # GE0/0/2
# print(match.group(5))       # IndexError: no such group
print(match.groups())       # ('54', '0000-5e00-0136', 'GE0/0/1', 'GE0/0/2') 按子组（捕获组）顺序开展编排，返回一个元组
