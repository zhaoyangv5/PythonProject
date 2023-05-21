'''
整体用方括号括起来，各个元素用逗号隔开的有序序列组合。
这个序列是可变的，元素间的顺序可变，元素内容可变。
'''
'''列表创建 list()'''
Lists = 'switch'
print(list(Lists))       # 在函数 list() 的作用下，字符串被拆解成元素，然后这些“元素”组成了一个列表。这就是字符串列表。

'''列表长度 len()'''
List = list(Lists)
print(len(List))
print(len(Lists))

print('='*25+'sorted()'+'='*25)

'''列表排序 sorted()'''
list5 =  ['huawei','cisco','juniper']
print(sorted(list5))        # 特别注意，此时返回的是一个新的列表对象，并不是在原来的列表基础上修改
print(id(list5))
print(id(sorted(list5)))        #其实是新建了一个对象。我们同样可以通过函数id()查看list5对象在内存中“哪里”。两者不同的.

print('='*25+'索引修改'+'='*25)

'''
列表方法
'''

'''索引修改'''
list1 = [2022,3,27]
print(id(list1))
list1[0] = 2023     # 索引到某个元素上，对该元素进行修改。
print(list1)
print(id(list1))

print('='*25+'列表嵌套'+'='*25)
'''列表嵌套'''
interfaces = [
    ['Vlanif1 ', '192.168.11.11/24', 'up','up'],
    ['Vlanif10', '10.18.123.5/25 ', 'down','down'],
    ['Vlanif12','12.1.1.3/29','*down','down']
    ]
print(interfaces)
interface = interfaces[0][1]
print(interface)

'''
列表中还有列表，这就是列表的“嵌套”，这样的模型可以继续嵌套很多层。这里做两个术语串讲——“迭代”和“递归”。它们有点相似容易混淆，但有本质的差别。

>>> [1,2,3,4] # 从左到右，逐个提取，这过程叫“迭代”。这个对象叫“可迭代对象”。
[1, 2, 3, 4]
>>> 
>>> # 一层一层钻进去（比如通过多层索引信息找到1这个数字），然后再逐层回归到上面来，这个过程就“递归”。
>>> [[[1,2,3],[4,5,6],[7,8,9]],['e','f','g'],['x','y','z']]
[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ['e', 'f', 'g'], ['x', 'y', 'z']]
>>> 
'''
print('='*25+'列表切片'+'='*25)

'''列表切片'''
list3 = [2002, 3, 27, 'switch', 'router', 'mac-address']
print(list3[0])         # 索引定位
print(list3[1:])        # 切片
print(list3[-1])        # 负向切片
print(list3[::-1])      # 负向步进索引，反转。返回的是新列表

'''列表反转 reverse()'''
list3.reverse()     # 看清楚了，这里有差别哦，是原来的列表进行修改哦！不是返回一个新列表
print(list3)

'''列表排序 sort()'''
vlans = [100, 200, 300, 400]
vlans.sort()
print(vlans)        #大家注意比较 sort()方法和python内置函数sorted()的差别，留意其操作对象和返回值
vlans.sort(reverse=True)
print(vlans)

print('='*25+'列表追加append()'+'='*25)

'''列表追加 append()
这个方法会在原列表的最后面增加多一个元素，完成后并不返回具体内容，即返回None
'''
list5 =  ['huawei','cisco','juniper']
print(list5)
list5.append('h3c')
print(list5)
print(list5.append('h3c')) # 追加元素后，append()方法返回 None
for i in list5:    #列表里确实增加了h3c，通过遍历可知
    print(i)

print('='*25+'列表扩展extend()'+'='*25)
'''列表扩展 extend()'''
list5 = ['cisco', 'huawei', 'juniper']
list6 = ['alcatel','nokia']
list5.extend(list6)      # 方法1，在list5的基础上扩展另一个列表，会修改原来的list5
# print(list5.extend(list6))   #extend()方法返回 None
print(list5)
result = list5 + list6      # 方法2，运算符 + 处理list5和list6，组合后返回一个新的列表，赋值给变量result
print(result)

print('='*25+'insert'+'='*25)
'''列表添加 insert ()
方法insert ()可以在原列表的某个位置加插一个元素
'''
vlans = [100,200,300,400]
vlans.insert(1,150)
print(vlans)

vlans_str = ['100','200','300','400']
vlans_str.insert(1,'150')
print(vlans_str)

print('='*25+'列表弹出pop()'+'='*25)
'''列表弹出 pop()
这个方法将列表中的一个元素弹出来，即在列表中删除。具体删除哪个元素，我们可以通过pop()的参数进行控制
'''
print(result)           #['cisco', 'huawei', 'juniper', 'alcatel', 'nokia', 'alcatel', 'nokia', 'alcatel', 'nokia']
result.pop()            #删除 'nokia'
# print(result.pop())
print(result)
result.pop(1)           #删除 'huawei'
# print(result.pop(1))
print(result)


print('='*25+'删除元素remove()'+'='*25)
'''删除元素 remove()
1.元素不再列表中的，试图删除，则报错！
2.不能指定索引值，会被当成元素值；元素不再列表中的，试图删除，则报错！
'''
result = ['cisco', 'huawei', 'juniper', 'alcatel', 'nokia', 'alcatel', 'nokia']
# print(result.remove('huawei'))       # 方法remove()没有返回
result.remove('nokia')          # 如果有重复项的话，请留意它是删除哪个。对的，索引小的。
print(result)

print('='*25+'索引查询index()'+'='*25)
'''索引查询 index()'''
result = ['cisco', 'huawei', 'juniper', 'alcatel', 'nokia', 'alcatel', 'nokia']
print(result.index('nokia'))        # 如果有重复项，会返回最小索引值


print('='*25+'辅助凭借join()'+'='*25)
'''辅助凭借 join()
严格来说，这个join方法并不是列表的方法，它是一个字符串方法
'''
vlans_str = ['100', '150', '200', '300', '400']
print(type(vlans_str))
print(','.join(vlans_str))          # 将 vlans_str 这个列表的元素拼接成字符串，元素中间加插逗号隔开
vlans_str = ','.join(vlans_str)
print(type(vlans_str))
print(vlans_str)

# vlans = [100, 150, 200, 300, 400]             # 这里一定是字符串列表，不可是其它的
# print(','.join(vlans))         # 非str类型，而是数字类型