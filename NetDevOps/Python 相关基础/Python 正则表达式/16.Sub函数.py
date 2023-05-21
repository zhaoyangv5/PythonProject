'''
Sub函数概述

字符串有个叫replace的方法，re模块的sub函数与之类似。更牛的是，sub函数可以根据正则表达式进行匹配替换，因此也将适配更多条件的场景

'''
import re
# 第 1 步，体验字符串sub与正则replace函数的相似之处
arp_record = '172.29.50.150   4c1f-ccb4-5157            I -  Vlanif41'

print(arp_record.replace(' ',','))
print(re.sub(r' ', ',', arp_record))

#第 2 步，sub函数项正则化替换
print(re.sub(r'( +I - +| +)', ',', arp_record))
print(type(re.sub(r'( +I - +| +)', ',', arp_record)))       #<class 'str'>

# 第 3 步，mac地址表解析实战

mac_table = open("mac_table_Sub.txt").read()
print(re.sub(r'(\S+-\S+) +'
             r'(\d+) +'
             r'.*'
             r'(Eth\S+) +'
             r'(\S+) +'
             r'\S+ +',
             r'\1,\2,\3,\4', mac_table))