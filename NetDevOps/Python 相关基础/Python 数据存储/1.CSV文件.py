


import csv
import os

print('*'*20+'读取CSV'+'*'*25)
'''
读取CSV
'''


print(os.path.dirname('cvs_lab1.csv'))
csv_path = r'/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python 数据存储/cvs_lab1.csv'
with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    print(reader)           #csv.reader返回的是一个迭代器（iterator）
    for row in reader:
        print(row)

print('*'*50)

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    print(reader)           # csv.reader返回的是一个迭代器（iterator）
    print(list(reader))     # 用list函数将这个迭代器处理成列表

print('*'*50)
#通常情况下，表头需单独使用，因而我们可以特殊处理一下
with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Headers: ', header)
    for row in reader:
        print(row)

print('*'*50)
#有时候我们还需要表头那一行跟每一行的数据打配合，那此时需要字典形式
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    print(reader)           #OrderedDict类，叫有序字典，是字典的一个变种
    for row in reader:
        # print(row)          #例：{'hostname': 'sw1', 'vendor': 'Huawei', 'model': '5700', 'location': 'Beijing'}
        print(row['hostname'], row['model'])


print('*'*20+'写入CSV（writerow）'+'*'*25)
'''
写入CSV（writerow）
'''
data = [['hostname','vendor','model','location'],
	    ['sw1','Huawei','5700','Beijing'],
	    ['sw2','Huawei','3700','Shanghai'],
	    ['sw3','Huawei','9300','Guangzhou'],
	    ['sw4','Huawei','9306','Shenzhen'],
	    ['sw5','Huawei','12800','Hangzhou']]

csv_path = r'/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python 数据存储/csv-lab1-writing.csv'
with open(csv_path,'w',newline='') as f:            #newline=''，不加这个参数的话，每行会增加一行空行
    writer = csv.writer(f)                          #如果有中文等，可能还要留意编解码问题，否则可能会有乱码
    for row in data:
        writer.writerow(row)

with open(csv_path, 'r') as f:
    print(f.read())


print('*'*20+'写入CSV（文本带逗号）'+'*'*25)
'''写入CSV（文本带逗号）'''

data = [['hostname','vendor','model','location'],
	    ['sw1','Huawei','5700','Beijing,Sijiazhuang'],      #'Beijing,Sijiazhuang'
	    ['sw2','Huawei','3700','Shanghai'],
	    ['sw3','Huawei','9300','Guangzhou'],
	    ['sw4','Huawei','9306','Shenzhen'],
	    ['sw5','Huawei','12800','Hangzhou,Suzhou']]

csv_path = r'/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python 数据存储/csv-lab1-writing.csv'
with open(csv_path,'w',newline='') as f:            #newline=''，不加这个参数的话，每行会增加一行空行
    writer = csv.writer(f)                          #如果有中文等，可能还要留意编解码问题，否则可能会有乱码
    for row in data:
        writer.writerow(row)

with open(csv_path, 'r') as f:          #字符串里面有个逗号，为了避免歧义被当做分割符了，所以csv模块做了特殊处理
    print(f.read())         #"Beijing,Sijiazhuang"   "Hangzhou,Suzhou"


print('*'*50)

'''文本全部打上""号'''
with open(csv_path,'w',newline='') as f:            #newline=''，不加这个参数的话，每行会增加一行空行
    writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)                          #如果有中文等，可能还要留意编解码问题，否则可能会有乱码
    for row in data:
        writer.writerow(row)

with open(csv_path, 'r') as f:
    print(f.read())

print('*'*20+'写入CSV（writerows）'+'*'*25)
'''写入CSV（writerows)'''
data = [['hostname','vendor','model','location'],
	    ['sw1','Huawei','5700','Beijing,Sijiazhuang'],
	    ['sw2','Huawei','3700','Shanghai'],
	    ['sw3','Huawei','9300','Guangzhou'],
	    ['sw4','Huawei','9306','Shenzhen'],
	    ['sw5','Huawei','12800','Hangzhou,Suzhou']]

csv_path = r'/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python 数据存储/csv-lab1.1-writing.csv'
with open(csv_path,'w',newline='') as f:            #newline=''，不加这个参数的话，每行会增加一行空行
    writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)                          #如果有中文等，可能还要留意编解码问题，否则可能会有乱码
    writer.writerows(data)

with open(csv_path, 'r') as f:
    print(f.read())


print('*'*20+'写入CSV（DictWriter）'+'*'*25)
'''写入CSV（DictWriter）'''
data = [{
    'hostname': 'sw1',
    'location': 'Beijing,Xicheng',
    'model': '5700',
    'vendor': 'Huawei'
    }, {
    'hostname': 'sw2',
    'location': 'Shanghai',
    'model': '3700',
    'vendor': 'Huawei'
    }, {
    'hostname': 'sw3',
    'location': 'Guangzhou,Tianhe',
    'model': '9300',
    'vendor': 'Huawei'
    }, {
    'hostname': 'sw4',
    'location': 'Shenzhen',
    'model': '9306',
    'vendor': 'Huawei'
    }, {
    'hostname': 'sw5',
    'location': 'Hangzhou',
    'model': '12800',
    'vendor': 'Huawei'
    }]
csv_path = r'/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python 数据存储/csv-lab1.2-writing.csv'

with open(csv_path,'w',newline='') as f:            #newline=''，不加这个参数的话，每行会增加一行空行
    # print(data[0].keys())
    # print(list(data[0].keys()))
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

with open(csv_path, 'r') as f:
    print(f.read())


print('*'*20+'自定义分割符（delimiter)'+'*'*25)
'''自定义分割符（delimiter）'''

csv_path = r'/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python 数据存储/cvs_lab1.1.csv'


with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    # print(reader)           #csv.reader返回的是一个迭代器（iterator）
    for row in reader:
        print(row)

print('='*50)

with open(csv_path, 'r') as f:
    reader = csv.reader(f, delimiter=':')   #如果不指定delimiter，那么默认的分割符是逗号，本实验我们改成了冒号作为分割符
    # print(reader)           #csv.reader返回的是一个迭代器（iterator）
    for row in reader:
        print(row)



