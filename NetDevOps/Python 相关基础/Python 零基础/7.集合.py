'''
集合（set）是无序的、不可重复的一组数据，与列表类似，但是它的特点是成员不重复，
我们在初始化的时候传入多个值相等的成员时，集合会自动去重保留一个。
其创建方法是使用花括号{}创建，成员中间用逗号隔开。对于初学者而言，成员的数据类型建议初学阶段锁定在数字和字符串。不建议使用其他数据类型，
比如集合的成员不能是字典，会报TypeError: unhashable type: 'dict'的错误，
集合是通过哈希了成员之后，根据哈希值去重，字典无法哈希，进而报错
'''
'''元素唯一性'''
vlans = [2022,2022,2022,4,4,1,1]
set_vlans = set(vlans)      #去重
print(type(set_vlans))
print(set_vlans)
print(vlans)

print('='*25+'元素添加 add()'+'='*25+'\n')

'''元素添加 add()'''
print(set_vlans)
set_vlans.add('2022')
print(set_vlans)

set_vlans.add(('router','switch'))      # 元组，没问题！
print(set_vlans)

# set_vlans.add(['huawei','cisco'])   ## 列表，就会报错，集合中元素必须唯一。不能添加可变容器序列。列表、字典和集合都有可能破坏了元素的唯一性。
print(set_vlans)


print('='*25+'元素删除 discard()'+'='*25+'\n')

'''元素删除 discard()'''
set_vlans.discard(2022)
print(set_vlans)
set_vlans.discard('2022')
print(set_vlans)


print('='*25+'清空集合 clear()'+'='*25+'\n')

'''清空集合 clear()'''
set1 = {1, '2022', 4, ('router', 'switch')}
set1.clear()
print(set1)     ## 清空集合，但没有删除掉整个集合对象
#set ()    # 为什么不是{}，因为{}表示空字典。为了区别，所以空集合呈现为set()


print('='*25+'集合并集 union() |'+'='*25+'\n')

'''
集合并集 union() |
两个集合合并，不同的合并，相同的去重，有一个术语叫“并集”
'''
vlans1 = {100,150,200,250,300}
vlans2 = {200,250,300,250,300,350,400}

print(vlans1.union(vlans2))     # 相同的去重，集合是无序的，此时，你看400 跑到最中间去了
print(vlans1 | vlans2)      # 我们也可以用这个管道符进行处理，效果一致。


print('='*25+'集合交集 intersection() &'+'='*25+'\n')

'''
集合交集 intersection() &
两个集合合并，不同的删掉，相同的去重，有一个术语叫“交集”
'''
print(vlans1.intersection(vlans2))