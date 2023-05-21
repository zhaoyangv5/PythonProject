'''
<Layer3Switch-1>
[Layer3Switch-1]
许多实际场景中，我们需要把网元名称Layer3Switch-1提取出来。但设备不同，这个名称不一定有规律可循。
仔细观察，聪明的你一定能想到，我们可以通过查找<>或[]符号内的字符串来达到目的。
但是，我们却不要<>或[]这两个符号。这需求虽然简洁清晰，但怎么用正则表达式来表述呢？
答案是正向预查（Positive Lookbehind）、负向预查（Positive Lookahead）
'''
import re
'''
正向预查（Positive Lookbehind）
语法： (?<=pattern)
语法意思大概为：待匹配字符串中的一个位置，紧贴该位置之前的字符序列能够匹配pattern，并且这位置不占宽度（zero-width，所谓“零宽”）
'''
# 例：(?<=<).*
# 表达式中，语法pattern部分为<，因符号<有特殊，我们也可以用\<，确保它就是<字符，而无其它特殊含义。我们写成如下表达式：
# (?<=\<).*
# 在带匹配字符串中找以<符号开始，后面的任意字符，匹配结果删掉最开始的<符号。
print(re.search(r'(?<=<).*','qitazifu<swname').group())


'''
负向预查（Positive Lookahead）
语法：(?=pattern)
语法意思大概为：待匹配字符串中的一个位置，紧贴该位置之后的字符序列能够匹配pattern，并且这位置不占宽度（zero-width，所谓“零宽”）
'''
# 例：(?<=<).*
print(re.search(r'.*(?=>)','swname>qitazifu').group())



'''
综合使用正向和负向预查
(?<=\<).*(?=\>)
'''
print(re.search(r'(?<=\<).*(?=\>)','qitazifu<swname>qitazifu').group())
print(re.search(r'(?<=\<).*?(?=\>)','qitazifu<swname>qitazifu').group())



'''同时适配用户视图和系统视图'''


# 第一种写法     a|b	    或 方法
print(re.search(r'(?<=\<).*?(?=\>)|(?<=\[).*?(?=\])','qitazifu<Layer3Switch-1>qitazifu').group())
# Layer3Switch-1
print(re.search(r'(?<=\<).*?(?=\>)|(?<=\[).*?(?=\])','qitazifu[Layer3Switch-1]qitazifu').group())
# Layer3Switch-1

#第二种写法      [abc]	匹配方括号内的任意符号
print(re.search(r'(?<=[\<\[]).*?(?=[\>\]])','qitazifu<Router-200>qitazifu').group())
# Router-200
print(re.search(r'(?<=[\<\[]).*?(?=[\>\]])', 'qitazifu[Router-200]qitazifu').group())
# Router-200


#读取交换机名称
sw_name1 = 'HRP_M<GDGZ-PB-CA-FW01-Eudemon1000E-501B01>'
sw_name2 = 'NFJD-CEQ-XZ-BOSS-SW01-L4-9650#show log '
print(re.search(r'(?<=[\<\[]).*?(?=[\>\]])',sw_name1).group())
print(re.search(r'.*(?=#)',sw_name2).group())
