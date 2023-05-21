'''
切换大小写
upper() - 将字符串中的所有字母变成大写。
lower() - 将字符串中的所有字母变成小写。
swapcase - 将字符串中的所有字母小写的变大写，大写的变小写。
capitalize - 将字符串中的首字母变成大写，其它字母变成小写
'''
intf = 'GigabitEthernet10/0/3'
print(intf.upper())  #变成大写
print(intf.lower())     #变成小写
print(intf.swapcase())      #大小写互换
print(intf.capitalize())        #首字母大写，其他变小写
print(intf.lower().capitalize())        #先变小写，在首字母变大写

print('='*50)

'''
计数 count()
方法count()允许我们以参数形式传入某一字符或字符串，它计算返回原字符串中传入字符或子字符串的重复次数
'''
count_num = 'router,router,router,router,router'
print(count_num.count('router'))
print(count_num.count('outer'))
print(count_num.count('r'))

print('='*50)

'''
查找 find()
方法find()允许我们以参数形式传入某一字符或字符串，它查找返回原字符串中传入字符或子字符串出现的最低索引号
'''
intf = 'interface GigabitEthernet10/0/3'
print(intf.find('GigabitEthernet'))     # 查找子字符串，返回第一次匹配的最低索引值，其实就是G的索引值
print(intf[intf.find('GigabitEthernet'):])   # 综合一下切片，我们可以这来一下
print(intf[10:])    #字符串切片和上面切片一样，因为find返回的是一个最低索引值 10

print('='*50)
'''
开始结束标识
startwith()
endwith()
这两个方法对字符串是否以特定符号开始或者结束做判断，返回布尔值（True或False）
'''
intf = 'GigabitEthernet10/0/3'
print(intf.startswith('Gigabit'))
print(intf.startswith('gigabit'))
print(intf.endswith('10/0/3'))
print(intf.endswith('10/0/1'))

print('='*50)

'''
替换 replace()
在字符串中先查找某一特定符号，然后将其替换成另一特定符号
如果找不到呢？还替换吗？不替换了，原字符串是什么就返回什么
'''
intf = 'GigabitEthernet10/0/3'
print(intf.replace('10/0/3', '10/0/1'))
print(intf)                     # 这里是个坑，一定要记住，它没有修改原来的字符串，是返回一个新的字符串。
intf1 = intf.replace('10/0/3', '10/0/1')   #赋值给新的变量之后，新的变量更改
print(intf1)
print(intf.replace('abc', '123'))       # 在字符串中找abc，要把它替换成123，但结果没找着，于是依然返回原字符串

print('='*50)
'''
清洗 strip
strip() - 两边清洗
lstrip() - 左边清洗
rstrip() - 右边清洗
默认情况下，方法strip()会处理掉字符串两边的\t\n\r\f\v等空白符号。
'''
intf = '\r\ninterface GigabitEthernet10/0/3\n'
print(intf)
print('='*50)
print(intf.strip())
#strip可以传入参数，去掉参数内容
print(intf.strip("interface"))

print('='*50)
'''
分列 split()
方法split()可以把字符串按某符号进行分割，而后返回一个字符串列表
'''
port_vlan = 'port trunk allow-pass vlan 1843 1923 2033 2053 2103 2163 2273 2283'   #原始字符串
print(port_vlan.split())
print(port_vlan.split(' vlan '))    # 以' vlan '这个符号作为分割条件
curs = port_vlan.split(' vlan ')
vlans = curs[-1].split()            # 切片操作后，取vlan信息；之后将vlan信息再次做字符串切片操作，提取单一vlan信息。
print(vlans)


