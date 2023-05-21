'''
分组重复概述
'''
import re

'''捕获结果重复'''
with open('ipv6.txt') as data:
    for line in data:
        print(line.strip())



regex0 = r'ipv6 address (\d+)'          #捕获组（子组）是\d+，即是数字的就能被捕获。这种情况下，只要配了ipv6地址，就会被匹配。
regex1 = r'ipv6 address (\d+):\1'
regex2 = r'ipv6 address (\d+):\1:\1'
regex3 = r'ipv6 address (\d+):\1:\1:\1'
regex4 = r'ipv6 address (\d+):\1:\1:\1:\1'
regex5 = r'ipv6 address (\d+):\1:\1:\1:\1:\1'
#捕获组（子组）是\d+，即是数字的就能被捕获。关键是\1是啥，它表示的就是前面捕获组的完全匹配，即前面小括号里是啥，这里就重复啥，
#regex5中有5个\1，加上前面的(\d+)，一共6个
regex6 = r'ipv6 address (\d+):\1:\1:\1:\1:\1:\1'
regex7 = r'ipv6 address (\d+):\1:\1:\1:\1:\1:\1:\1'
#正则表达式中，如果有捕获组（子组），我们用\1 可以对第一个子组捕获的结果进行重复匹配，就是要跟第一次捕获项完全一样才行
#正则表达式中，如果前面有一个捕获组（子组），后面我们可以用\1来完全重复匹配，即前面子组匹配了啥，\1也匹配了啥。这种情况下，捕获组也就只有一个了

with open(r'ipv6.txt') as data:
    for line in data:
        # match = re.search(regex0, line)
        # match = re.search(regex1, line)
        # match = re.search(regex2, line)
        # match = re.search(regex3, line)
        # match = re.search(regex4, line)
        # match = re.search(regex5, line)
        # match = re.search(regex6, line)
        match = re.search(regex7, line)

        if match:
            print(line.strip())
            print(match.groups())

print("#"*50)

'''重复捕获结果测试（按名）'''
regex10 = r'ipv6 address (?P<ipv6>\d+)'
regex11 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6)'
regex12 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6)'
regex13 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex14 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex15 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex16 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex17 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'

#同样，即便重复了7个，8个，方法groups依然只能捕获成一个
with open(r'ipv6.txt') as data:
    for line in data:
        match = re.search(regex16, line)
        if match:
            print(line.strip())
            print(match.groups())       #('2004',)
            print(match.groupdict())

print("#"*50)
'''重复捕获结果测试（{n}优化）'''
# 在正则表达式重复写\1或者(?P=ipv6)，重复次数一多，自然就繁琐。我们完全可以用{n}来设定重复次数
regex20 = r'ipv6 address (?P<ipv6>\d+)'
regex24 = r'ipv6 address (?P<ipv6>\d+)(:(?P=ipv6)){4}'
regex25 = r'ipv6 address (?P<ipv6>\d+)(:(?P=ipv6)){5}'
regex26 = r'ipv6 address (?P<ipv6>\d+)(:\1){6}'
regex27 = r'ipv6 address (?P<ipv6>\d+)(:\1){7}'

with open(r'ipv6.txt') as data:
    for line in data:
        match = re.search(regex26, line)
        if match:
            print(line.strip())
            print(match.groups())   #('2004', ':2004')
# 从运行结果可以看出来，虽然正则表达式被我们优化了，但又惹来另一个问题。方法groups带多出来了一个元素（如:2004），这是捕获多余项，我们并不需要它

print("#"*50)

'''非捕获组'''
#在正则匹配的过程中，如果我们只是想对规则进行小括号分组，但不想捕获它，怎么办？比如前述的('2004',':2004')中的':2004'
# 在正则表达式中，我们可以在分组中加入?:来取消分组的捕获功能

regex30 = r'ipv6 address (?P<ipv6>\d+)'
regex35 = r'ipv6 address (?P<ipv6>\d+)(?::(?P=ipv6)){5}'
regex36 = r'ipv6 address (\d+)(?::\1){6}'

with open(r'ipv6.txt') as data:
    for line in data:
        match = re.search(regex36, line)
        if match:
            print(line.strip())
            print(match.groups())