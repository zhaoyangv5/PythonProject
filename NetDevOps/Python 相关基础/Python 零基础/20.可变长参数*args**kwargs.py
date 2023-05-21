
# *args来表示可变长位置参数，它其实就是个元组；使用**kwargs来表示可变长关键字参数，它其实就是个字典

'''
*args组合使用

参数a
-如果作为位置参数出入，必须放在第一位
-如果作为关键字传输传入，则位置随意
参数*args ，代表可边长
-以元组形式展示
-有时候可省略，即元组为空
'''

def sum_arg(a, *args):
    print(a,args)           #args以元组形式展示 1 (10, 20, 30)
    return a + sum(args)

print(sum_arg(1, 10, 20, 30))

'''*args单独使用'''
def sum_arg(*args):
    print(args)           #args以元组形式展示 (1, 10, 20, 30)
    return sum(args)

print(sum_arg(1, 10, 20, 30))


# 可变长关键字参数 **kwargs

def sum_arg(a, **kwargs):
    print(a, kwargs)        #**kwargs以字典形式展示 10 {'b': 10, 'c': 20, 'd': 30}
    return a + sum(kwargs.values())

print(sum_arg(a=10, b=10, c=20, d=30))
print(sum_arg(a=10, b=10))
print(sum_arg(b=10, c=20, d=30, a=10))