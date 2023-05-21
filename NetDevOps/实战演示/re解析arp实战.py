'''
实验目的
我们把通过指令获取来的回显半结构化信息，通过正则表达式，解析（Parsing）成Python的标准数据类型。
（1）读取回显文件disp_arp.txt，测试读取是否正常。
（2）提取ARP表项中的IP、接口、VLAN信息（非接口本身的ARP表项，vlan会跨行）。
'''
import re
import pandas as pd
"""
#python读取回显文件
with open('display_arp.txt','r') as data:
    for line in data:
        print(line.strip())

测试正则
#先拷贝一行测试正则表达式
line = '172.29.50.150   4c1f-ccb4-5157            I -  Vlanif41'
match = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)', line)
# print(match.groups())
print(match.groupdict())

#还有另一个单行文本形式，他就是一个数字
#仔细观察，前面一堆空格，紧接着以一个数字结束
line = '                                          41'
match = re.search(' +(?P<vlan>\d+)$', line)
print(match.groupdict())
"""

result = []

regex1 = r'(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)'
regex2 = r' +(?P<vlan>\d+)\D+$'

with open('display_arp.txt') as data:
    for line in data:
        #如果为vlan字段，则追加到result的最后一个元素，然后解析下一行
        match = re.search(regex2, line)
        if match:
            # print(match.groupdict())
            result[-1].update((match.groupdict()))
            # print(result)
            continue
        #如果不为vlan字段，则正常查找arp表项
        match = re.search(regex1, line)
        if match:
            result.append(match.groupdict())

# print(result)
# 补齐上面没有解析出vlan的，让解析更规整
for each_arp_record in result:
    if 'vlan' not in each_arp_record.keys():
        each_arp_record.update(({'vlan':'-'}))

#把结果打印出来展示,可以输出到文件或者导入数据库
print(f'{len(result)} records on arp table :')
# print(result)         #回显是列表类型的字典
arp = pd.DataFrame(result)
# print(arp)
# 写入Excel
arp.to_excel('display_arp.xlsx',
                 sheet_name='ARP',
                 index=False,
                 columns=['ip','mac', 'port', 'vlan']
                 )


#结果打印并保存
with open('display_arp_result.txt', 'w') as f:
    for i, each_arp_record in enumerate(result, 1):  ## (result, 1)中的1让i可以从1开始，而非从默认的0开始。
        print(f'\ndetails of arp table {i}"')
        f.write(f'\ndetails of arp table {i}:'+'\n')
        for key in each_arp_record:
            # print(f'{key:10} : {each_arp_record[key]:10}')
            last_result = f'{key:10} : {each_arp_record[key]:10}'
            print(last_result)
            f.write(last_result.title()+'\n')


