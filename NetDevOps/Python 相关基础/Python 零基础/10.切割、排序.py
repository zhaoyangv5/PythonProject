
'''切割'''

str1 = 'description Method_chaining_test_10.12.23.0/27'
str1_split = str1.split()
desc = str1_split[-1]       #Method_chaining_test_10.12.23.0/27
# print(desc)
desc_split = desc.split('_')        #['Method', 'chaining', 'test', '10.12.23.0/27']
# print(desc_split)
ip = desc_split[-1]
print(ip)

'''第二种方式'''
ip = str1.split()[-1].split('_')[-1]  #首先，处理'description Method_chaining_test_10.12.23.0/27'成列表；接着取字符串；接着再处理成列表，最后取出ip信息来
print(ip)


'''
排序
排序的内容很多，涉及到数据结构和算法层面的就又很深，比如冒泡排序法、选择排序法等等
'''

'''对嵌套列表或元组列表等数据进行排序时，按嵌套列表（元组）的第一个元素排序；如果第一个元素相同，则按第二个元素排序'''
data = [[1, 100, 1000], [2, 2, 2], [1, 2, 3], [4, 100, 3]]
print(sorted(data))

vlans = ['1', '30', '11', '3', '10', '20', '30', '100']
print(sorted(vlans))

ip_list = ["192.168.1.1", "192.168.10.1", "192.168.2.1", "192.168.11.1"]
print(sorted(ip_list))      #IP地址其实也是字符串，与数字字符串的“境遇”是一模一样的