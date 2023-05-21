'''
f 字符串 - Python 3.6 以上版本新推出，强烈推荐。
format 方法 - 早前比较主流的方法。
%运算符 - 最古老的方法
'''
'''
f 字符串
该方法不仅允许在字符串模板中变量值，还允许加插函数、方法返回值等。
通常，f 字符串会更方便更好理解一些，而且它的执行效率要比其它字符串格式化方法效率更高
'''
#字符串语法（加插变量）
#在字符串中，遇到花括号，则会进行变量等的替换
ip_address = '192.168.11.11'
mask = '255.255.255.0'
inter_ip_cur = f"ip address {ip_address} {mask}"  #变量一定要先定义好了，才能变f字符串所使用，否则会报错
print(inter_ip_cur)

'''
 f 字符串语法（加插函数、方法返回值）
 
'''
print('='*50)
vendors =['huawei','cisco']   # 列表，后面很快会切入，先预热一下哈。
vendor = f"{vendors[0].title()} {vendors[1].title()}"  # 这里用了列表切片，跟我们学过的字符串切片很像。
print(vendor)
print(f"{len(vendors[0])},{len(vendors[1])}")

print('='*50)
'''
 f 字符串位宽控制
 在 f字符串花括号中，我们可以借助冒号，在冒号后面设置该域的宽度，制表显示
'''
ip_1,ip_2,ip_3,ip_4 = [192,168,11,11]
print(f'''
... IP address:
... {ip_1:8} {ip_2:8} {ip_3:8} {ip_4:8}                 # 花括号中的 :8 表示站8个字符宽度。
... {ip_1:b} {ip_2:b} {ip_3:b} {ip_4:b}                 # 花括号中的 :b 表示以二进制形式呈现，位宽按实际。
... {ip_1:8b} {ip_2:8b} {ip_3:8b} {ip_4:8b}             # 花括号中的 :8b 表示以8位二进制形式呈现。
... {ip_1:08b} {ip_2:08b} {ip_3:08b} {ip_4:08b}''')     # 花括号中的 :8b 表示以8位二进制形式呈现，高位0填充。

print('='*50)
'''
小知识点，关于控制位宽后的左右对齐、居中对齐。默认方式有个小细节，即左对齐还是右对齐与对象的类型有关系，其实excel表格中的数据也如此
'''
vlan, mac, intf = ['100', 'aabb-cc80-2022', 'GigabitEthernet0/0/2']
print(f"{vlan:>15} {mac:>15} {intf:>15}")     # 右对齐
print(f"{vlan:15} {mac:15} {intf:15}")        # 左对齐
print(f"{vlan:^15} {mac:^15} {intf:^15}")     # 居中对齐

print('='*50)
pi = 3.14159265
print(f'pi = {pi:.3f}')     # 浮点数，保留 3 位小数。

print('='*50)
'''
方法format()
字符串是一个对象，它有一个叫“format”的方法，专门用来做字符串格式化
这种代替方式支持多种数据类型，如字符串、数字、列表……
'''
int_ip_cur = "ip address {} {}".format('192.168.11.11','255.255.255.255')
print(int_ip_cur)

int_ip_cur = "ip address {} {}".format(ip_address,mask)
print(int_ip_cur)

'''
字符串取模运算符%（String Modulo Operator %）
不推荐
'''
print("今天是%d年%d月%d日,星期%s" % (2022,3,27,'日'))
print("圆周率为%10.5f" % (3.14159265))