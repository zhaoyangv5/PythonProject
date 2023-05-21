'''
我们的目标是把这些回显数据加工成一个目标网段一行的形式
'''

'''
模板解释

实验目的是实现了，下面我们来重点解释模板。

Value Dest (\S+/\S+)
Value List NextHop (\S+\.\S+\.\S+\.\S+)

Start
  ^\s+\S+/\S+\s+ -> Continue.Record
  ^\s+${Dest}\s+.+\s+${NextHop}\s+
  ^\s.+\s${NextHop}\s+
先定义两个变量。变量的正则表达式完全可以用别是写法，并不需要特别精准，结合回显报文内容找到特征匹配即可。这就是TextFSM相对于纯正则表达式的优势吧。

变量名	带关键字	正则表达式	备注
Dest	无	\S+/\S+	匹配目的网段
关注“/”
NextHop	List	\S+\.\S+\.\S+\.\S+	匹配下一跳IP地址
关注3个“.”
我们来看一下规则

规则	序号
^\s+\S+/\S+\s+ -> Continue.Record	1
^\s+${Dest}\s+.+\s+${NextHop}\s+	2
^\s.+\s${NextHop}\s+	3

'''

import sys
import textfsm
from tabulate import tabulate

with open('display_ip_routing-table—template') as f, open('display_ip_routing-table.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))