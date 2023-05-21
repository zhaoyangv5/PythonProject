'''
正则字符集
\d	匹配任何十进制数字，相当于 [0-9]
\D	与 \d 相反
\s	匹配任何空白字符，相当于 [ \t\n\r\f\v]
\S	与 \s 相反
\w	匹配任何单词字符（字母，数字，下划线）
\W	于 \w 相反

正则重复符
+	重复前面元素一次或多次，{1,}
*	重复前面元素零次或多次，{0,}
?	重复前面元素零次或一次，{0,1}
{n}	重复前面元素n次
{n,m}	重复前面元素n次到m次（m的数字大于n）
{n,}	重复前面元素n次或更多次
'''
import re

'''示例1，获取日志时间'''

log3 = 'Sep 26 2021 23:11:02-08:00'
# [0-9][0-9]:[0-9][0-9]:[0-9][0-9]	长
# \d\d:\d\d:\d\d	短,简洁
re_search = re.search(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9]', log3)
print(re_search.group())
print(re.search(r'\d\d:\d\d:\d\d', log3).group())

'''示例2，获取日志MAC地址'''

log4 = 'MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136,'
# [a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]
# \w\w\w\w-\w\w\w\w-\w\w\w\w	其实\w相当于 [a-zA-Z0-9_]，也就是这里写得更粗一些.
print(re.search(r'[a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]', log4).group())
print(re.search(r'\w\w\w\w-\w\w\w\w-\w\w\w\w', log4).group())


'''重复符 +'''
# 加号+表示前面的表达式可以重复任意多次，但至少一次。前面的表达式的表达式如果用括号()括起来的话，则表示这个分组（子组）内的内容都要重复

log5 = 'MacAddress = 00000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2.'
print(re.search(r'0+', log5).group())   #方法search只会匹配到第一项，从左到右匹配，0000先中了，所以后面的00，0就没有匹配中，即便它们也是符合规则的
print(re.search(r'(00)+', log5).group()) #00被括号括起来了，它们就被正则规则打包成一组，被认为是一个整体,因为00是一个整体，只会倍数倍数匹配

# [a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]	最原始的写法
# \w\w\w\w-\w\w\w\w-\w\w\w\w	简化，规则更“粗”
# \w+-\w+-\w+	更简化，规则更“粗”
# (\w+-)+\w+	再简化，规则更"粗"
log6 = 'MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2.'
print(re.search(r'\w+-\w+-\w+', log6).group())
print(re.search(r'(\w+-)+\w+', log6).group())


'''重复符 *'''
#星号*表示前面的表达式可以重复任意多次，甚至是0次
print(re.search(r'\w+-(\w+-*)+', log6).group()) #0000-5e00-0136的第一组横杆一定得匹配中，后面两组的横杆就任意了


email1 = 'zhujiasheng@abc.com'
email2 = 'zhujiasheng@gd.abc.com'
email3 = 'zhujiasheng@st.gd.abc.com'

print(re.search(r'\S+@(\w+\.)*com', email1).group())
print(re.search(r'\S+@\S+com',email1).group())
print(re.search(r'\S+@(\w+\.)*com', email2).group())
print(re.search(r'\S+@\S+com',email2).group())
print(re.search(r'\S+@(\w+\.)*com', email3).group())
print(re.search(r'\S+@\S+com',email3).group())

'''重复符 ?'''
#问号?表示前面的表达式可以0次或1次。依然用上面*使用的邮箱提取例子，如果你能看出问题点，就证明已经基本掌握了

# >>> re.search(r'\S+@(\w+\.)?com', email1).group()
# 'zhujiasheng@abc.com'
# >>> re.search(r'\S+@(\w+\.)?com', email2).group()
# Traceback (most recent call last):
#   File "<pyshell#255>", line 1, in <module>
#     re.search(r'\S+@(\w+\.)?com', email2).group()
# AttributeError: 'NoneType' object has no attribute 'group'
# >>> re.search(r'\S+@(\w+\.)?com', email3).group()
# Traceback (most recent call last):
#   File "<pyshell#256>", line 1, in <module>
#     re.search(r'\S+@(\w+\.)?com', email3).group()
# AttributeError: 'NoneType' object has no attribute 'group'
# 为什么zhujiasheng@gd.abc.com、zhujiasheng@st.gd.abc.com匹配不中？因为规则的匹配分组只能命中0次或1次，而2次及以上的就不符合规则了

'''{n}，{n,m}，{n,}'''

# \d\d:\d\d:\d\d	\d{2}:\d{2}:\d{2}
# \w\w\w\w-\w\w\w\w-\w\w\w\w	\w{4}-\w{4}-\w{4}
print(re.search(r'\d{2}:\d{2}:\d{2}', log3).group())

log7 = 'MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136,'
print(re.search(r'\w{4}-\w{4}-\w{4}', log7).group())
