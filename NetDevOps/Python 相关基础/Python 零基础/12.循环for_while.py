#for
#Python的for循环可以不通过索引非常方便的遍历访问序列（包含但不局限于字符串、列表、元组、集合、字典）
# for i in <序列>:
#     <代码块>
# 其中每次循环i会被自动赋值此次访问的成员（字典的遍历i每次是key），
# 并且i是一个局部的变量，严格意义上只有在此代码块内才可以被访问使用，否则容易引起程序报错，或者程序未按预期执行
print('*'*20+'列表遍历'+'*'*25)
a = [1, 2, 3]
# a = (1, 2, 3)
# a = {1, 2, 3}
for i in a:
    print(i)
'''列表的输出结果如下：
1
2
3
'''
devs = ['huawei','cisco','juniper']
devs_titles = []
for  dev in devs:
    devs_titles.append(dev.title())
print(devs_titles)

print('*'*20+'元组遍历'+'*'*25)

'''元组遍历'''
vlans = (100, 200, 300, 400, 500)
for vlan in vlans:
    print(f'vlan{vlan}')
    print(f' description Vlan_{vlan}')

print('*'*20+'字符串遍历'+'*'*25)

'''字符串遍历'''
for each_letter in 'switch':
    print(each_letter)

print('*'*20+'数字遍历'+'*'*25)

'''数字遍历'''
for  i in range(8):
    print(f'interface GE1/0/{i}')

print('*'*20+'字典遍历'+'*'*25)

'''字典遍历'''
#字典的for循环比较特殊，它访问的是key。如果要取对应的value，需要通过key去访问
dev_info = {'ip': '192.168.1.1', 'name': 'as01'}
for i in dev_info:
    print(i)
    print(dev_info[i])  # 将对应i作为key传入，取出对应的value。
# '''输出结果如下：
# ip
# 192.168.1.1
# name
# as01'''

dev_info = {'ip': '172.29.50.150', 'mac': '4c1f-ccb4-5157', 'port': 'Vlanif41'}
for key in dev_info:
    print(key + ' => ' + dev_info[key])

print('*'*20+'字典遍历items'+'*'*25)
#我们也可以通过字典的一个特殊方法items，它会返回一个元组的列表（这个描述并不准确，但是方便理解），
#这个列表的成员是一个元组，key与value，我们通过非常方便的赋值方法给k,v这两个局部变量
dev_info = {'ip': '192.168.1.1', 'name': 'as01'}
for k, v in dev_info.items():
    print(k)
    print(v)
'''输出结果如下：
ip
192.168.1.1
name
as01'''
print(dev_info.items(),type(dev_info.items()))

# '''输出结果如下，其实返回的是一个特殊的数据结构dict_items，但是我们可以简单理解为返回了元组的列表
# dict_items([('ip', '192.168.1.1'), ('name', 'as01')]) <class 'dict_items'>
# '''

print('*'*20+' While方法 '+'*'*25+'\n'+'*'*56)

'''while'''
# while <条件表达式>:
#     <代码块>
#只要条件满足（条件表达式为True），就不断循环，条件不满足时退出循环
i = 1
end = 100
sum = 0
while i <= end:
    sum = sum + i
    i = i + 1
print(sum)  # 输出结果5050
print('*'*50)

a = 5
while a > 0:
    print(a)
    a -= 1
    # a = a - 1

# 循环中经常还会用到两个关键字continue与break（二者只出现在循环中）：
# continue代表结束此次循环，既continue后的代码块不再执行。比如某些条目我们不关注，无需继续处理此条目，则跳过这次循环，进入下一个条目的处理。
# break代表结束本次所有的循环，跳出当前循环。比如我们已经找到了要提取的信息，无需再继续执行下面的循环，则可以使用此关键字。

#练习：要查询某交换机up的端口及其信息
intfs = [{'name': 'Eth1/1', 'status': 'up'},
         {'name': 'Eth1/2', 'status': 'up'},
         {'name': 'Eth1/3', 'status': 'down'},
         {'name': 'Eth1/4', 'status': 'up'},
         ]
# 计数器i
i = 0
# 端口数目
intfs_num = len(intfs)
print(intfs_num)
# up的端口列表初始化值为空列表
up_intfs = []
# 进行循环，当计数器小于端口数目时可以循环
while i < intfs_num:
    intf = intfs[i]
    if intf['status'] == 'up':
        # up端口追加成员
        up_intfs.append(intf)
    # 对计数器进行累加
    i = i + 1  # 等同于 i += 1 ,这是一种简便写法，python中不同其他语言，无i++这种写法。
print(up_intfs)  # 输出结果为[{'name': 'Eth1/1', 'status': 'up'}, {'name': 'Eth1/2', 'status': 'up'}, {'name': 'Eth1/4', 'status': 'up'}]


print('*'*20+'while实例演示'+'*'*25)

'''实例演示'''
username = input('Enter usernmame: ')
password = input('Enter password: ')

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('password is too short\n')
        password = input('Enter password again:  ')
    elif username in password:
        print('password contains username')
        password = input('Enter password again:  ')
    else:
        print(f'password for user {username} is set')
        password_correct = True