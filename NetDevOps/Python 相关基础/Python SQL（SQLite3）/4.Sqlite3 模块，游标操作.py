'''
一、获取查询结果的方法

获取查询结果的方法还挺多的，大体上可以归纳成如下两种思路。

使用 fetchone、fetchmany、fetchall，这些是以行的形式进行捕获返回。
使用游标作为迭代器，返回的是一个迭代器（iterator）
'''

import sqlite3
from pprint import pprint

'''二、方法 fetchone、fetchmany、fetchall'''

'''
方法 fetchone
方法 fetchone 返回一行数据
'''

connection = sqlite3.connect('netdev_db.db')
cursor = connection.cursor()
cursor.execute('select * from switch2')
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

'''
方法 fetchmany
返回的是列表
cursor.fetchmany([size=cursor.arraysize]) # 只有一个参数，在结果集中要返回多少行
'''
# print(cursor.fetchmany(3))   # 3代表返回几行

#配合while
# 这个方法返回传输参数 size（默认是1） 的行数，如果剩余不够 size 大小了，则全部返回.
# 如果都没有了，就返回空。因此，我们在上面用 three_rows 做判断条件，为真就再读，为假就跳出循环
# while True:
#     three_rows = cursor.fetchmany(3)
#     if three_rows:
#         pprint(three_rows)
#     else:
#         break

'''
 方法 fetchall
 一次把数据都“撸”出来
'''
#值得注意的是手册中 remaining 字眼，也就是如果前面被 fetchone 或 fetchmany 执行过的话，fetchall 只返回剩下的部分
# print(cursor.fetchall())
pprint(cursor.fetchall())           #结果为元组的列表

print('#'*50)
'''
游标迭代器
我们其实也可以把整个游标当成一个迭代器来对待。所谓的“迭代”就是“挨个撸出来”，其实也叫“遍历”
'''
#游标（cursor）的方法 execute 执行后，返回的值放在变量 result ，此时 result 本身就是一个迭代器
result = cursor.execute('select * from switch2')
for row in result:
    print(row)  #结果为元组

connection.close()

#跳过变量名的烦恼
# for row in cursor.execute('select * from switch2'):
#     print(row)



