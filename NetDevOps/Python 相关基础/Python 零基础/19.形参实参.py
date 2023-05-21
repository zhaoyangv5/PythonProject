'''
站在类和对象的角度看，创建函数的目的通常是将一段特定任务的代码封装打包起来。这样你就可以多次重复调用它，而非每次使用时重新创建。
通常，函数需要有输入值，执行特定处理，从而带来输出
在函数调用的过程中，实参的具体数据会传递给形参的预设变量
'''


def check_passwd(username, password):
    if len(password) < 8:
        print('Password is too short')
        return False
    elif username in password:
        print('Password contains username')
        return False
    else:
        print(f'Password for user {username} has passed all checks')
        return True

#调用时必须传入两个参数（此时是实参）；如果我们只传输一个参数，则Python会抛出异常
print(check_passwd('wgsy', '123'))
print(check_passwd('wgsy', 'netdevwgsyops2023'))
print(check_passwd('wgsy', 'netdevops2023'))

'''
必须形参（Required parameters）
必须形参决定了哪些实参在函数调用时必须传递，而且传递的实参数量必须刚刚好与必须形参的数量对应（不能多也不能少)
'''

'''
可选形参|默认参数（Optional parameters |default parameters ）
创建函数时，我们可以为参数指定默认值，比如这样：
def check_passwd(username,password,min_length=8)
在这种情况下，min_length选项被指定了默认值，于是在调用该函数时，它可以不传值
'''
# check_passwd('wgsy', 'w1g2s3y45', 3)

'''
实参类型
当调用函数时，实参（arguments）传递有如下两个方式：
按位置 - 以函数定义中对应形参的顺序为序，将对应的值传输函数中。
按关键字 - 按函数定义中形参名赋值传递，无须理会参数传递的具体位置。
传递实参过程中，位置参数和关键字参数是可以混用的，即同时使用，但位置参数必须在关键字参数之前指定传入。
'''
# check_passwd('wgsy', '123w4g5s6y789')  #位置实参
# check_passwd(password='12345', username='wgsy', min_length=4)  #关键字实参
# check_passwd(password='12345', username='wgsy', 4)   #混合使用

print('#'*50)
'''
现实中，一些标志信息（flag）和数值信息，可以采用关键字实参传入。如果定义函数的时候，形参名字起得见名知意的话，那通常就一目了然了
'''
# 我们增加一个标志位，来设置检查时，是否核对“密码含用户名”规则，以便对核查规则进行筛选
def check_passwd(username, password, min_length=8, check_username=True ):  # 增加 check_username 标识
    if len(password) < min_length:
        print('Password is too short')
        return False
    elif check_username and username in password:  # 这行有变化,默认情况下，标识位为真，函数check_passwd会校验密码是否包含用户名
        print('Password contains username')
        return False
    else:
        print(f'Password for user {username} has passed all checks')
        return True

print(check_passwd('wgsy', 'netdevwgsyops2023', min_length=3))
print(check_passwd('wgsy', 'netdevwgsyops2023', min_length=3, check_username=False)) #将check_username的值指定为False的话，则不执行该校验