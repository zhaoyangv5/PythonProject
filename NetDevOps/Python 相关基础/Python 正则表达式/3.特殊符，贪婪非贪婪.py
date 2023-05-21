'''
.	匹配除换行符外的任意符号
^	匹配行首
$	匹配行末
[abc]	匹配方括号内的任意符号
[^abc]	匹配不为方括号内的任意符号
a|b	    或
(regex)	表达式会被认为是一个整体元素，被匹配的子组还会被记忆起来。
'''
import re

'''特殊符号'''

'''.符号'''
disp_int = '''
<Layer3Switch-1>display interface
GigabitEthernet0/0/1 current state : UP
Line protocol current state : UP
Description:
Switch Port, PVID :    1, TPID : 8100(Hex), The Maximum Frame Length is 9216
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 4c1f-cc92-675c
Last physical up time   : 2021-10-25 15:22:35 UTC-08:00
Last physical down time : 2021-10-25 15:22:33 UTC-08:00
......'''
print(re.search(r'Switch.+TPID.+Length.+', disp_int).group())
#因为默认情况下点.代表匹配除换行符外的任意符号，匹配过程一旦遇到了换行符，就停下来了。另外，重复符+或*则默认是尽可能的多匹配，即所谓的“贪婪”模式


'''
^符号,
字符^表示行首
'''
mac = '2, Hardware address is 4c1f-cc92-675c'
print(re.search(r'^\d+', mac).group())

prompt = '<Layer3Switch-1>display interface'
print(re.search(r'^.+>', prompt).group())

'''$符号,与托字符^相反，字符$表示行末'''
line = 'Hardware address is 4c1f-cc92-675c'
print(re.search(r'\S+$', line).group())     #表达式\S+$匹配最后一截非空项

'''
[]符号
Python中用方括号[]表示列表；在正则表达式中，我们也可以把它理解成列表
在[]中的符号可以看成列表的元素，全过程只要匹配任何一个列表元素即可
'''
line = 'Hardware address is 4c1f-cc92-675c'
print(re.search(r'[Hh]ard[Ww]are', line).group())

#如果不知道交换机路由器是在用户视图，还是系统视图的话。我们可以用[>\]]来同时匹配两种情况。
#说明一下，[]中要匹配]时引起了歧义，所以要\]转义一下，正则表达式烦就烦在这些上。

commands = ['<Layer3Switch-1>display interface','[Layer3Switch-2]display interface']
for command in commands:
    match = re.search(r'^.+[>\]]', command)
    if match:
        print(match.group())


#[0-9a-zA-Z]形式，即[0123456789]可以写成[0-9]，同样a到z和A到Z也类似，而且他们还可以叠加后扔在同一个[]中'''
line = 'Hardware address is 4c1f-cc92-675c'
print(re.search(r'[0-9a-zA-Z]+-[0-9a-zA-Z]+-[0-9a-zA-Z]+', line).group())

# []还能配合^字符，表示不要匹配中[]中的字符，即取反。不想要匹配到数字，我们可以这么做
print(re.search(r'[^0-9]', line).group())
print(re.search(r'[^0-9]+', line).group())


'''
|符号 
字符|表示前后两个表达式是“或”关系
'''

line = 'Hardware address is 4c1f-cc92-675c'
print(re.search(r'Hardware|address', line).group())

'''
符号()
符号()用来对表达式进行分组。在数学概念上，被()打包在一起的，就认为是一个元素。这样会不会好理解呢？！
'''
line = 'Hardware address is 4c1f-cc92-675c'
print(re.search(r'[0-9a-zA-Z]+-[0-9a-zA-Z]+-[0-9a-zA-Z]+', line).group())
print(re.search(r'([0-9a-zA-Z]+-)+[0-9a-zA-Z]+', line).group())     #([0-9a-zA-Z]+-)打包一个组，后面+表示这个组重复一次或多次


'''贪婪限定'''

'''贪婪模式'''
#默认情况下，*+都是贪婪的，即能匹配多的话就不匹配少，能匹配越多就匹配越多！
line = '<text line> huawei text>'
match = re.search(r'<.*>', line)
print(match.group())    # <text line> huawei text> 正则表达式<.*>并没有在line后的>没有停下来，而是在text后的>才停下来

'''
非贪婪模式
如果我们把<.*>改成<.*?>的话，则从贪婪变成非贪婪'''
match = re.search(r'<.*?>', line)       # 如果要去除掉重复符号的贪婪特性，可以在重复符号的后面加上一个问号?即可！
print(match.group())                    # <text line>


'''贪婪与非贪婪比较'''
# >>> line = 'Hardware address is 4c1f-cc92-675c'
# >>> re.search(r'([0-9a-zA-Z]+-)+[0-9a-zA-Z]+', line).group()
# '4c1f-cc92-675c'
# >>> re.search(r'([0-9a-zA-Z]+-)+?[0-9a-zA-Z]+?', line).group()
# '4c1f-c'
# >>> re.search(r'([0-9a-zA-Z]+-)+?[0-9a-zA-Z]+', line).group()
# '4c1f-cc92'
# >>> re.search(r'([0-9a-zA-Z]+-)+[0-9a-zA-Z]+?', line).group()
# '4c1f-cc92-6'
# >>>