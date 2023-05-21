'''
SQL 基本操作

1.1 CREATE

在创建表之前，需要有个数据库，我们通过 litecli 来新建或者连接一个数据库（即有则连接，无则新建并连接）。

E:\sqlite>litecli netdev_db.db
Version: 1.9.0
Mail: https://groups.google.com/forum/#!forum/litecli-users
GitHub: https://github.com/dbcli/litecli
netdev_db.db> .databases
+-----+------+------------------------+
| seq | name | file                   |
+-----+------+------------------------+
| 0   | main | E:\sqlite\netdev_db.db |
+-----+------+------------------------+
Time: 0.010s
netdev_db.db>

接着，我们来建一个数据表 switch，存放交换机信息。

netdev_db.db> create table switch (mac text not NULL primary key, hostname text, model text,location text);
Query OK, 0 rows affected
Time: 0.106s
netdev_db.db> .tables
+--------+
| name   |
+--------+
| switch |
+--------+
Time: 0.006s
netdev_db.db>

create table switch (mac text not NULL primary key, hostname text, model text,location text);
虽然我们用的是 sqlite 数据库的，但实际上其它数据库也大体如此。

create table - 建表关键字
switch - 表名
(mac text not NULL primary key, hostname text, model text,location text) - 定义这个表
mac - 字段，如 excel 表的表头
text - 文本
not NULL - 非空
primary key -主键
hostname
model
location
; - 冒号术语语法需要，有些数据库系统建表不用冒号，有些要

数据库中有个叫主键的概念，就是用它可以确定是哪一个记录。
我打个比方，好比身份证是居民的主键，你找不到一个人给你是有相同身份证号码的，但我们很有可能跟别人重名。
因此，在户籍管理中，身份证号码就是主键。除了“主键”概念外，还有“外键”等其它概念，我们后面再慢慢了解掌握

mac text not NULL primary key
该字段唯一
这个字段不能为空（在 SQLite 中，这必须声明）
这个时候的 switch 只有申明和定义（“字段”类似于表格中的“列”，表头），还没有记录（“记录”或者“条目”也是数据库的术语，类似于表格中的“行”）

netdev_db.db> .schema switch
+----------------------------------------------------------------------------------------------+
| sql                                                                                          |
+----------------------------------------------------------------------------------------------+
| CREATE TABLE switch (mac text not NULL primary key, hostname text, model text,location text) |
+----------------------------------------------------------------------------------------------+
Time: 0.005s
netdev_db.db>
netdev_db.db>

1.2 DROP

能建表就能删掉，这里我们顺便把 DROP 也带一下。日常做这个要注意哦，表会被删除，记录也会没了的。不过这是删表，还不是删库。编程界有个“删库跑路”的概念，说的是把 netdev_db.db 文件给删掉，不太一样。我们这仅仅是删表而已。

netdev_db.db> DROP table switch
You're about to run a destructive command.
Do you want to proceed? (y/n): y
Your call!
Query OK, 0 rows affected
Time: 0.084s
netdev_db.db>

1.3 INSERT

CREATE 后，得到的是一个空表（已经带了表头了），现在我们可以用 INSERT 来添加记录

INSERT into switch values ('4c1f-cc1b-2942', 'sw1', 'Huawei 5700', 'Shantou');
我们还可以使用另一种方式，不用严格按“定义表格”时的顺序，字段对应上即可。

netdev_db.db> insert into switch (mac, model, location, hostname) values  ('4c1f-cc1b-29f3', 'Huawei 5300', 'Chaozhou', 'sw2');
Query OK, 1 row affected
Time: 0.116s
netdev_db.db>

1.4 SELECT

我个人觉得，这个 SELECT 语句是普通网络工程师最经常使用的。

netdev_db.db> select * from switch
+----------------+----------+-------------+----------+
| mac            | hostname | model       | location |
+----------------+----------+-------------+----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou |
+----------------+----------+-------------+----------+
2 rows in set
这里的 * 表示全部，所有字段都显示。我们自然可以指定要显示的字段。

netdev_db.db> SELECT hostname, mac, model from switch;
+----------+----------------+-------------+
| hostname | mac            | model       |
+----------+----------------+-------------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 |
| sw2      | 4c1f-cc1b-29f3 | Huawei 5300 |
+----------+----------------+-------------+
2 rows in set
Time: 0.006s
netdev_db.db>

1.5 WHERE

SELECT 和 WHERE 是一对好搭档，经常一起使用。我们把地点在汕头的设备筛选出来吧。

netdev_db.db> select hostname, mac, model, location from switch where location = 'Shantou'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
+----------+----------------+-------------+----------+
1 row in set
Time: 0.006s
netdev_db.db> select hostname, mac, model, location from switch where location = 'shantou'
0 rows in set
Time: 0.001s
这里的查询内容就区分大小写了，'Shantou' 和 'shantou' 是不一样的。我们大体可以归纳一下，指令是大小写不敏感，数据是大小写敏感

1.6 LIKE

WHERE 后面字段可以带不同的操作符，前面我们体验了等于号（=），其实还可以带表的，比如 BETWEEN...IN等，日常我们最常用到的是 LIKE，所以我们单独来说一下它。

与 lIKE 一起使用的，通常有

两个通配符
_ 表示一个字符或数字
% 表示任意个字符或数字（可以0个，可以1个，也可以多个）

netdev_db.db> select hostname, mac, model, location from switch where location LIKE 'Shantou'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
+----------+----------------+-------------+----------+
1 row in set
Time: 0.006s
netdev_db.db> select hostname, mac, model, location from switch where location LIKE 'Shanto_'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
+----------+----------------+-------------+----------+
1 row in set
Time: 0.006s
netdev_db.db> select hostname, mac, model, location from switch where location LIKE 'S%'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
+----------+----------------+-------------+----------+
1 row in set
Time: 0.006s
netdev_db.db>

LIKE 的使用非常灵巧，在日常过滤数据方面应用很广，需反复研究掌握，慢慢来。

netdev_db.db> select hostname, mac, model, location from switch where model like 'Huawei'
0 rows in set
Time: 0.001s
netdev_db.db> select hostname, mac, model, location from switch where model like 'Huawei%'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
| sw2      | 4c1f-cc1b-29f3 | Huawei 5300 | Chaozhou |
+----------+----------------+-------------+----------+
2 rows in set
Time: 0.006s
netdev_db.db> select hostname, mac, model, location from switch where model like 'Huawei 5_00'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
| sw2      | 4c1f-cc1b-29f3 | Huawei 5300 | Chaozhou |
+----------+----------------+-------------+----------+
2 rows in set
Time: 0.007s
netdev_db.db> select hostname, mac, model, location from switch where model like 'Huawei 5%00'
+----------+----------------+-------------+----------+
| hostname | mac            | model       | location |
+----------+----------------+-------------+----------+
| sw1      | 4c1f-cc1b-2942 | Huawei 5700 | Shantou  |
| sw2      | 4c1f-cc1b-29f3 | Huawei 5300 | Chaozhou |
+----------+----------------+-------------+----------+
2 rows in set
Time: 0.006s
netdev_db.db>

1.7 ALTER

ALTER 可以给一个现有表改名，或者给一个现有表增加一列。看起来这个操作很重要，但是大家想想，我们普通网络工程师在现网环境下，能随便做这种操作嘛？显然是不可能的。
所以我们当体验下即可。原来的 switch 表，两行数据有点少，我加到 5 行吧

此时我们来讲两列 mngmt_ip 和 mngmt_vid ，分别是管理 IP 和管理 VLAN。

netdev_db.db> ALTER table switch ADD COLUMN mngmt_ip text;
You're about to run a destructive command.
Do you want to proceed? (y/n): y
Your call!
Query OK, 0 rows affected
Time: 0.078s
netdev_db.db>  ALTER table switch ADD COLUMN mngmt_vid integer;
You're about to run a destructive command.
Do you want to proceed? (y/n): y
Your call!
Query OK, 0 rows affected
Time: 0.092s
netdev_db.db>
执行完以后，我们再 SELECT 一下 switch 表。

netdev_db.db> select * from switch
+----------------+----------+-------------+----------+----------+-----------+
| mac            | hostname | model       | location | mngmt_ip | mngmt_vid |
+----------------+----------+-------------+----------+----------+-----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | <null>   | <null>    |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | <null>   | <null>    |
| 4c1f-cc1b-2947 | sw3      | Huawei 5700 | Jieyang  | <null>   | <null>    |
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | <null>   | <null>    |
| 4c1f-cc1b-2949 | sw5      | Huawei 5328 | Shantou  | <null>   | <null>    |
+----------------+----------+-------------+----------+----------+-----------+
5 rows in set
Time: 0.007s
netdev_db.db>

mngmt_ip（数据类型是 text），mngmt_vid（数据类型是 integer），表中这两个字段在各条记录中目前还都是空值

1.8 UPDATE

我们可以用 UPDATE 语句来给数据表中的某个记录的某个字段添加数据，或者修改原值。

netdev_db.db> UPDATE switch set mngmt_ip = '192.168.11.11' WHERE hostname = 'sw1';
Query OK, 1 row affected
Time: 0.091s
netdev_db.db> select * from switch
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | 192.168.11.11 | <null>    |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | <null>        | <null>    |
| 4c1f-cc1b-2947 | sw3      | Huawei 5700 | Jieyang  | <null>        | <null>    |
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | <null>        | <null>    |
| 4c1f-cc1b-2949 | sw5      | Huawei 5328 | Shantou  | <null>        | <null>    |
+----------------+----------+-------------+----------+---------------+-----------+
5 rows in set
Time: 0.006s
netdev_db.db>
记住了，UPDATE 处理给 null 值赋值之外，还能修改原来的数值，所以这种操作其实很“高危”，现网机会不会这么直接使用的，非常“危险”！
再操作一次吧，补个管理 VLAN 信息 mngt_vid

netdev_db.db> UPDATE switch set mngmt_vid = '123' WHERE hostname = 'sw1';
Query OK, 1 row affected
Time: 0.093s
netdev_db.db> select * from switch
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | 192.168.11.11 | 123       |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | <null>        | <null>    |
| 4c1f-cc1b-2947 | sw3      | Huawei 5700 | Jieyang  | <null>        | <null>    |
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | <null>        | <null>    |
| 4c1f-cc1b-2949 | sw5      | Huawei 5328 | Shantou  | <null>        | <null>    |
+----------------+----------+-------------+----------+---------------+-----------+
5 rows in set
Time: 0.005s
netdev_db.db>

1.9 REPLACE

REPLACE 操作有点类似于 INSERT ，如原来没这记录则新增，如原来有这记录则改写。更厉害的是，遇到有主键，且主键重复，也能直接写入。
它可以先删掉原来的记录，再重新新增一条。功能太猛，现网也不大会这么使用。

netdev_db.db> INSERT INTO switch VALUES ('4c1f-cc1b-2949', 'sw5', 'Huawei 5328', 'Shantou', '192.168.11.15', 123);
UNIQUE constraint failed: switch.mac
用 `INSERT INTO 提示冲突，我们执行不了。我们试试 REPLACE INTO（也可以用 INSERT OR REPLACE INTO）。

netdev_db.db> REPLACE INTO switch VALUES ('4c1f-cc1b-2949', 'sw5', 'Huawei 5328', 'Shantou', '192.168.11.15', 123);
Query OK, 1 row affected
Time: 0.082s
netdev_db.db> INSERT OR REPLACE INTO switch VALUES ('4c1f-cc1b-2949', 'sw5', 'Huawei 5328', 'Shantou', '192.168.11.15', 123);
Query OK, 1 row affected
Time: 0.084s
小结一下，我们这么记忆REPLACE的操作规则。数据设置了唯一性（有主键），如果增量与存量发生主键冲突，它会删掉原先的存量，再新增一条记录；
如果没有主键或新增条目的主键与存量不冲突，它与普通INSERT的操作是一模一样的

1.a DELETE

DELETE 操作用来删除条目，比如我们把 sw5 删掉。

netdev_db.db> delete from switch where hostname = 'sw5'
You're about to run a destructive command.
Do you want to proceed? (y/n): y
Your call!
Query OK, 1 row affected
Time: 0.079s
netdev_db.db>
我们在 SELECT 一下这张表。

netdev_db.db> select * from switch
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | 192.168.11.11 | 123       |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | 192.168.11.12 | 123       |
| 4c1f-cc1b-2947 | sw3      | Huawei 5700 | Jieyang  | 192.168.11.13 | 123       |
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | 192.168.11.14 | 123       |
+----------------+----------+-------------+----------+---------------+-----------+
4 rows in set
Time: 0.005s
netdev_db.db>

1.b ORDER BY

ORDER BY 经常配合 SELECT ，对查询结果进行排序。

netdev_db.db> select * from switch order by hostname desc
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | 192.168.11.14 | 123       |
| 4c1f-cc1b-2947 | sw3      | Huawei 5700 | Jieyang  | 192.168.11.13 | 123       |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | 192.168.11.12 | 123       |
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | 192.168.11.11 | 123       |
+----------------+----------+-------------+----------+---------------+-----------+
4 rows in set
Time: 0.006s
netdev_db.db>
上述示例，SELECT 按 hostname 进行排序，但因为 sw 已经是升序了，所以我加了个 DESC 变成降序显示。

ASC 升序（默认）
DESC 降序

1.d OR

netdev_db.db> select * from switch where location like 'Chao%' or location like 'Shan%'
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | 192.168.11.11 | 123       |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | 192.168.11.12 | 123       |
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | 192.168.11.14 | 123       |
+----------------+----------+-------------+----------+---------------+-----------+
3 rows in set
Time: 0.005s
netdev_db.db>
1.e IN

netdev_db.db> select * from switch where location in ('Shantou','Chaozhou')
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2942 | sw1      | Huawei 5700 | Shantou  | 192.168.11.11 | 123       |
| 4c1f-cc1b-29f3 | sw2      | Huawei 5300 | Chaozhou | 192.168.11.12 | 123       |
| 4c1f-cc1b-2948 | sw4      | Huawei 5300 | Chaozhou | 192.168.11.14 | 123       |
+----------------+----------+-------------+----------+---------------+-----------+
3 rows in set
Time: 0.006s
netdev_db.db>
AND 、OR、IN 这几个看起来简单，但往往得掌握细节后才能用得比较顺手，比如是配合 = 呢？还是配合 is 呢？还是配合 LIKE 呢？

1.f NOT

netdev_db.db> select * from switch where location not in ('Shantou','Chaozhou')
+----------------+----------+-------------+----------+---------------+-----------+
| mac            | hostname | model       | location | mngmt_ip      | mngmt_vid |
+----------------+----------+-------------+----------+---------------+-----------+
| 4c1f-cc1b-2947 | sw3      | Huawei 5700 | Jieyang  | 192.168.11.13 | 123       |
+----------------+----------+-------------+----------+---------------+-----------+
1 row in set
Time: 0.005s
netdev_db.db>

'''