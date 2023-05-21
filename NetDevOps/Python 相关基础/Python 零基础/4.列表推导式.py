'''
列表推导式
'''
'''
一般写法
'''
dev = ['Cisco_Nexus7010', 'Huawei_S7706', 'Huawei_CE12808', 'Cisco_C9300']
for cisco_dev in dev:
    if 'Cisco' in cisco_dev:
        print(cisco_dev)

'''推导式'''
cisco_dev = [cisco for cisco in dev if 'Cisco' in cisco]
print(cisco_dev)

'''
列表生成式除了可以使用迭代类型快速构建列表外，也能根据简单的条件来过滤迭代内容，生成新的列表
'''
num = [x for x in range(1, 10)]         #range迭代类型
print(num)

num = [x for x in range(1, 10) if x%2==0]           #range迭代类型加条件
print(num)

'''列表生成式的迭代嵌套'''
dev_name = ['cisco', 'huawei', 'h3c', 'rejie', 'maipu']
dev_type = ['router', 'switch']

#传统
for name in dev_name:
     for type in dev_type:
        print(name, type)


#可以使用迭代嵌套的方式来创建新的对应关系
dev = [(name, type) for name in dev_name for type in dev_type]
print(dev)

#遍历
for name_type in dev:
    print(name_type)

for name, type in dev:      #生成元组类型的列表，直接用2个值遍历出来
    print(name, type)

'''
列表生成式的作用除了迭代生成列表，还可以把迭代序列中的元素进行过滤或者加工，从而生成一个新的列表。
当然，列表生成式也不能乱用，保持简短为宜，如果列表生成式过长。就要优先考虑for循环
'''