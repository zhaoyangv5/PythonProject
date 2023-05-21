'''
if后面进阶条件判断表达式和冒号，条件表达式是能得到布尔值的一段表达式，符合条件则进入对应的代码块（注意缩进，相对if缩进4个空格）。
elif是在条件表达式不满足后继续进行一种判断。
else是用于以上条件均不满足的情况。
在判断中，if必须有，elif和else根据实际需要添加，且else一般在最后。
其形式如：
if <条件表达式1>:
    <代码块1>
elif <条件表达式2>:
    <代码块2>
elif <条件表达式3>:
    <代码块3>
else:
    <代码块4>
'''
intf_status = 'Error'
if intf_status == 'up':
    print('端口up，正常')
elif intf_status == 'down':
    print('端口up，异常')
else:
    print('未知端口状态')  # 写两行，缩进体现出这两行是一段代码块
    print('端口状态: {}'.format(intf_status))   # 此处特意写两行代码，缩进体现出这两行是一段代码块

if intf_status == 'up':
    print('端口up，正常')
else:
    print('端口up，正常')



line = '''Eth1/1          1       eth  trunk  up      none                     1000(D) 11'''
if line.startswith('Eth'):
    intf_info = line.split()
    print(intf_info)
    intf_name = intf_info[0]
    intf_stauts = intf_info[4]
    # 在以下行输出端口名称和状态
    print('intf_name:{},satus:{}'.format(intf_name, intf_stauts))
else:
    print('此行，未发现端口信息')
# 这段代码中，我们通过对一行show命令的回显进行了信息的提取，通过字符串的startswith方法判断是否为端口的回显，
# 再用split方法切割字符串，将返回的字符串列表赋值给一个新的列表变量intf_info，然后通过列表的索引获取端口中的信息，
# 将端口名称和状态打印出来，实际可以在后续输出到表格中，同时对状态进行一些判断实现类似巡检的功能

'''实例练习'''
# username = input('Enter usernmame: ')
# password = input('Enter password: ')
# if len(password) < 8:
#     print('password is too short')
# elif username in password:
#     print('password contains username')
# else:
#     print(f'password for user {username} is set')


'''
三元操作
三元运算符可以把好几行的if/elif/else结构缩小成一行，大幅减少程序的篇幅，还支持嵌套，这样可能还让代码更加结构化
'''
dev_list = ['switch', 'router']
result = len(dev_list) if len(dev_list) > 1 else 'error'
print(result)

dev_list = ['switch', 'router','hub']
result = len(dev_list) if len(dev_list) > 1 else 'error'
print(result)

dev_list = []
result = len(dev_list) if len(dev_list) > 1 else 'error'
print(result)