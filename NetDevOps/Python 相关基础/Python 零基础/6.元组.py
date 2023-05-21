'''
整体用小括号括起来，各个元素用逗号隔开的有序序列组合。
这个序列是不可变的，一旦生成了就固定下来了。
'''
'''创建元组'''
tuple1 = tuple()
print(tuple1)       #空元组
print(type(tuple1))

tuple2 = ('router')
print(tuple2)       # 看好了，是字符串类型
print(type(tuple2))

tuple2 = ('router',)
print(tuple2)       # 仔细看，这里加了个逗号,元组类型
print(type(tuple2))

tuple3 = (2023)
print(tuple3)       #看好了，是数字整型类型哦
print(type(tuple3))

tuple3 = (2023,)
print(tuple3)       # 仔细看，这里加了个逗号,元组类型
print(type(tuple3))


print('='*25+'列表转换元组'+'='*25)

'''列表转换元组'''
list_sw1_keys = ['vendor','model','local','ports']
tuple_sw1_keys = tuple(list_sw1_keys)
print(tuple_sw1_keys)

print('='*25+'元组索引'+'='*25)

'''
元组索引
元组操作与列表操作类似
'''
print(tuple_sw1_keys)
print(tuple_sw1_keys[0])
print(tuple_sw1_keys[1])

print('='*25+'元组切片'+'='*25)

'''
元组切片
元组操作与列表操作类似
'''
print(tuple_sw1_keys)
print(tuple_sw1_keys[1:3])


print('='*25+'元素修改（报错)'+'='*25)

'''元素修改（报错）'''
# tuple_sw1_keys[3] = 'wgsy'

print('''有一种爱叫“硬爱”，如果真的要怎么搞''')
tuple_sw1_keys = tuple(list(tuple_sw1_keys[0:3])+['wgsy'])
print(tuple_sw1_keys)


print('='*25+'Python内置函数 sorted()'+'='*25)

'''
Python内置函数 sorted()
元组是不支持排序修改的。但用Python内置函数sorted()可以操作它。我盲猜可能复制到另一处，转列表，然后按列表的套路去排序，最后返回这个列表
'''
tuple_sw1_keys = ('vendor', 'model', 'local', 'ports')
print(sorted(tuple_sw1_keys))

'''
总结一下，
凡是能操作后对本身有影响的列表对象方法或Python列表相关内置函数，元组都不能进行迁移使用；
凡是操作后是返回一个新的对象（与原先的元组没关系的）的，都可以迁移使用！大家日常真的还是把元组当成一个“不能更改的列表”就好啦
'''