'''
布尔（bool）只有真或假两个值，对应True和False，在进行判断的时候非常有用。
数字、字符串、列表、字典等有一些运算是可以得到一个布尔值的。比如比较数字的大小返回的就是布尔值，某成员是否在列表内，
某key是否在字典里出现等等
'''
#布尔运算
# 布尔值可以进行逻辑运算，也称布尔运算。
# 包含三种运算：
# 且 ，and连接左右布尔值，左右布尔值均为真，结果才为真，否则为假。
# 或 ，or连接左右布尔值，左右布尔值有一个为真，结果为真，否则为假。
# 非，not后接布尔值，取反操作，如果布尔值为真则结果为假，如果布尔值为假，则结果为真。
flag1 = True
flag2 = False

flag = flag1 and flag2
print(flag)  # 结果为False

flag = flag1 or flag2
print(flag)  # 结果为True

flag = not flag1
print(flag)  # 结果为False

#数字类的比较运算如下：
# 数字类比较有大于> ,小于< ,等于== ,大于等于>= ,小于等于<= ,不等于!=
#对于两个数字是否相等用的是==，应为一个等于号=代表的是赋值，不等于用的符号是!=
a = 10
b = 12
print(a > b)  # 输出结果是False
print(a < b)  # 输出结果是True
print(a == b)  # 输出结果是False
print(a >= b)  # 输出结果是False
print(a <= b)  # 输出结果是True
print(a != b)  # 输出结果是True

#in 与 not in获得布尔值
intf_show = 'Eth1/1 is up'
up = 'up' in intf_show
print(up)  # 因为字符串中出现过'up',故结果是True

intfs = ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4']
print('Eth1/7' in intfs)  # 由于端口中无Eth1/7,故返回False

dev_info = {'ip': '192.168.1.1',
            'name': 'as01',
            'manufacture': 'huawei',
            'series': 'ce6800',
            'ports_sum': 48}

print('ssh_port' in dev_info)  # 由于此字典中无ssh_port这个key，所以返回False

#not in 进行一个不包含的计算
intf_show = 'Eth1/1 is up'
down = 'down' not in intf_show
print(down)  # 因为字符串'down'不在intf_show中,故结果是True
