'''
Sqlite3模块

Python 中有一个内置的模块 sqlite3 ，用于与 SQLite 数据库进行互动。该模块是 Python 自带的，因此无需额外安装。
这也侧面说明了 SQLite 是被 Python 官方纳入其生态的。

Connection - 对象，这个对象可以代表 1 个数据库连接，也可以直接理解成它就是一个数据库对象。
'''

import sqlite3

'''1.1 sqlite3 简单示例'''
# connection = sqlite3.connect('xxx.db')   # xxx.db 即是我们前序文章说的数据库文件。

# 一旦我们成功连接数据库以后，即拿到一个 Connection 对象，该对象有一个方法 cursor() 。
# 实际上 cursor 也是一个对象 Cursor 。我们先叫它做“游标"吧

# cursor = connection.cursor()

'''
二、SQL 执行命令
模块 sqlite3 中包含一些执行 SQL 命令的方法。

execute - 执行单条 SQL 命令。
executemany - 执行一个 SQL 表达式，该表达式可以配合参数（或者迭代器等）实际转化为多条 SQL 命令。
executescript - 允许同时执行多个 SQL 表达式。
'''

'''2.1 方法 execute 执行单条 SQL 命令'''
# connection = sqlite3.connect('netdev_db.db')
# print(connection)
# cursor = connection.cursor()
# print(cursor)
#
# cursor.execute('create table switch2 (mac text not NULL primary key, hostname text, model text, location text)')
#
# data = [('4c1f-cc1b-2942', 'sw1', 'Huawei 5700', 'Shantou'),
#         ('4c1f-cc1b-29f3', 'sw2', 'Huawei 5300', 'Chaozhou'),
#         ('4c1f-cc1b-2947', 'sw3', 'Huawei 5700', 'Jieyang'),
#         ('4c1f-cc1b-2948', 'sw4', 'Huawei 5300', 'Chaozhou'),
#         ('4c1f-cc1b-2949', 'sw5', 'Huawei 5328', 'Shantou')]
#
# query = "INSERT into switch2 values (?, ?, ?, ?)"  #问号相当于占位符，到时候列表中的每个元素（即元组），每个元组中的每个元素（即字符串）会各归各位，进行填充。这种有个叫法——“参数化传递数据”
#
# for row in data:
#     cursor.execute(query, row)  #方法 execute 的第二个参数必须是一个元组，即便你只想传一个元组，也必须组合成一个元组，比如('aaa',)
#
# connection.commit()

'''
2.2 方法 executemany
方法 executemany 允许我们用一个 SQL 表达式，配合参数（如迭代器）来构建多个具体的 SQL 命令
'''
connection = sqlite3.connect('netdev_db.db')

cursor = connection.cursor()

data2 = [
     ('4c1f-cc1b-294a', 'sw6', 'Huawei 5300', 'Shantou'),
     ('4c1f-cc1b-29fb', 'sw7', 'Huawei 5300', 'Chaozhou'),
     ('4c1f-cc1b-294c', 'sw8', 'Huawei 3700', 'Jieyang')]

query = "INSERT into switch2 values (?, ?, ?, ?)"  #问号相当于占位符，到时候列表中的每个元素（即元组），每个元组中的每个元素（即字符串）会各归各位，进行填充。这种有个叫法——“参数化传递数据”

cursor.executemany(query, data2)
#方法 executemany 依然是配合元组类型使用的。
#稍微留意下，你应该可以发现， 方法 executemany 其实就是实现了 execute 和 for 组合使用的功能，但可能在效率方便做了优化
connection.commit()


'''
2.3 方法 executescript
方法 executescript - 允许同时执行多个 SQL 表达式。我认为网工普通场景下较少用，主要用于批量建表，简单演示下
'''

# connection = sqlite3.connect('netdev_db.db')
#
# cursor = connection.cursor()
#
# cursor.executescript('''
#
#     create table switches(
#         hostname     text not NULL primary key,
#         location     text
#         );
#
#     create table dhcp(
#         mac          text not NULL primary key,
#         ip           text,
#         vlan         text,
#         interface    text,
#         switch       text not null references switches(hostname)
#         );
#
#     ''')
