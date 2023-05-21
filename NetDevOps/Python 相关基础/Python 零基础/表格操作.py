
import pandas as pd

#Excel表格读取
devs_df = pd.read_excel('inventory.xlsx')
devs = devs_df.to_dict(orient='records')
print(devs)

#表格写入
'''
pandas进行数据写入的操作，我们也基于字典的列表这种形式，因为我们提取信息时，一般都是将一个对象的多个字段信息放在一个字典中，
实际pandas支持多种方式的加载。
首先我们通过字典的列表创建一个Dataframe的数据对象，然后调用这个对象的to_excel函数即可写入到Excel文件中
'''
raw_data = [{'name': 'Eth1/1', 'desc': 'netdevops1'},
            {'name': 'Eth1/2', 'desc': 'netdevops2'}]
intf_df = pd.DataFrame(raw_data)
print(intf_df)
''' Dataframe从打印的结果可以看到 是一种二维矩阵的数据，非常符合我们的使用习惯
     name        desc
0  Eth1/1  netdevops1
1  Eth1/2  netdevops2
'''
intf_df.to_excel('as01_info.xlsx',
                 sheet_name='interfaces',
                 index=False,
                 columns=['name','desc']
                 )


#根据上读取的Excel写入CSV
intf_df1 = pd.DataFrame(devs)
print(intf_df1)
intf_df1.to_csv('as02_info.csv',
                index=False,
                columns=['name','hostname','platform','port','username','password',
                         'city','model','netmiko_timeout','netmiko_secret']
                )

