

list_A = ['192.168.11.11','192.168.11.12','192.168.11.13','192.168.11.14','192.168.11.15']
list_B = ['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4','5.5.5.5']
zip_ab = zip(list_A, list_B)
print(type(zip_ab))

for each_a,each_B in zip_ab:
    print(each_a,each_B,sep='  -->  ')

for each_a,each_B in zip_ab:            #第二次for的时候，居然居然居然打印不出东西来了
    print(each_a, each_B, sep='  -->  ')

'''
为了让zip后能按我们常规思路来，有这么两种解决方法：1、不要将zip结果赋值到变量中，每次用都zip一下；2、在赋值之前，用list函数处理一下
'''
print('#'*50)

list_zip_AB = list(zip(list_A,list_B))
print(list_zip_AB)
for each_a,each_B in list_zip_AB:
    print(each_a, each_B, sep='  -->  ')

for each_a,each_B in list_zip_AB:           #用listf方法之后，第二次也可以打印出来
    print(each_a, each_B, sep='  -->  ')