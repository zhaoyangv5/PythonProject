'''
一、隐式游标

方法Execute 在Connection 和Cursor 对象中均有效可用，但是，方法fetch仅针对Cursor 对象有效。
当Connection对象中调用execute方法时，其执行结果会返回一个游标（cursor）。
这个游标本身就是一个迭代器，因此我们可以在不使用fetch的情况下来获取查询结果。参考Sqlite3 模块的这一特性，我们甚至可以在不显式创建一个游标
'''

import sqlite3

data = [('4c1f-cc1b-2942', 'sw1', 'Huawei 5700', 'Shantou'),
        ('4c1f-cc1b-29f3', 'sw2', 'Huawei 5300', 'Chaozhou'),
        ('4c1f-cc1b-2947', 'sw3', 'Huawei 5700', 'Jieyang')]

con = sqlite3.connect('netdev_db2.db')

# con.execute('''create table switch
#             (mac text not NULL primary key, hostname text, model text, location text)'''
#             )
#
# query = 'INSERT into switch values (?, ?, ?, ?)'
# con.executemany(query, data)
# con.commit()

# for row in con.execute('select * from switch'):
#     print(row)

# con.close()

print(type(con.execute('select * from switch')))   #<class 'sqlite3.Cursor'> 这玩意儿叫“非显式游标”，也叫“隐式游标”


'''异常处理'''

query = "INSERT into switch values ('4c1f-cc1b-2942', 'sw4', 'Huawei 5700', 'Shantou')"
# con.execute(query)


# Traceback (most recent call last):
#   File "/Users/domic/PycharmProjects/PythonProject/NetDevOps/Python 相关基础/Python SQL（SQLite3）/5.Sqlite3 模块，非游标操作，异常处理.py", line 36, in <module>
#     con.execute(query)
# sqlite3.IntegrityError: UNIQUE constraint failed: switch.mac
try:
    con.execute(query)
except sqlite3.IntegrityError as e:
    print("出错啦~  ",e)

