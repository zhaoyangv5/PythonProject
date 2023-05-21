

import sys
import textfsm
from tabulate import tabulate

with open('display_ospf_peer_template') as f, open('display_ospf_peer.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))         #只有最后一个信息匹配，因为模板最后没有加 -> Record
# LOCAL_RouterID      PROCESS  AREA     LOCAL_INT_IP    LOCAL_INT      DEST_RouterID    DEST_INT_IP
# ----------------  ---------  -------  --------------  -------------  ---------------  -------------
# R1                        1  0.0.0.0  17.1.1.1        Ethernet0/0/7  7.7.7.7          17.1.1.7


'''Record'''

with open('display_ospf_peer_template-Record') as f, open('display_ospf_peer.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    # print(result)
    print(tabulate(result, headers=header))             #模板最后增加  -> Record  ，但是LOCAL_RouterID和Process只有第一个记录有信息

# LOCAL_RouterID    PROCESS    AREA     LOCAL_INT_IP    LOCAL_INT      DEST_RouterID    DEST_INT_IP
# ----------------  ---------  -------  --------------  -------------  ---------------  -------------
# R1                1          0.0.0.0  12.1.1.1        Ethernet0/0/0  2.2.2.2          12.1.1.2
#                              0.0.0.0  14.1.1.1        Ethernet0/0/1  4.4.4.4          14.1.1.4
#                              0.0.0.0  17.1.1.1        Ethernet0/0/7  7.7.7.7          17.1.1.7

'''Filldown'''
'''
因为在默认情况下，规则完整匹配一次后进行了Record动作记录（如果用数据库说法：此时解析入库），记录完成后，所有变量都变清空了。
此后继续执行匹配，往后的回显信息又没有再次有LOCAL_RouterID、PROCESS这些相关信息可被规则匹配到，因此就留空了
我们借助关键字Filldown对LOCAL_RouterID、PROCESS这两个变量进行一波操作。我们修改一下TextFSM模板文件template
'''
with open('display_ospf_peer_template-Filldown') as f, open('display_ospf_peer.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))             #无缘无故又多出一行记录来了呢？这记录就只有前2项目呢

# LOCAL_RouterID      PROCESS  AREA     LOCAL_INT_IP    LOCAL_INT      DEST_RouterID    DEST_INT_IP
# ----------------  ---------  -------  --------------  -------------  ---------------  -------------
# R1                        1  0.0.0.0  12.1.1.1        Ethernet0/0/0  2.2.2.2          12.1.1.2
# R1                        1  0.0.0.0  14.1.1.1        Ethernet0/0/1  4.4.4.4          14.1.1.4
# R1                        1  0.0.0.0  17.1.1.1        Ethernet0/0/7  7.7.7.7          17.1.1.7
# R1                        1

'''Required'''
'''
因为Filldown关键字让LOCAL_RouterID、PROCESS两个变量一路保持，没被重置清空，导致多了一行。
我们找一个变量（如DEST_RouterID，本例子用其它变量也行）配合Required关键字，来作为必选项吧
'''
with open('display_ospf_peer_template-Required') as f, open('display_ospf_peer.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))

# LOCAL_RouterID      PROCESS  AREA     LOCAL_INT_IP    LOCAL_INT      DEST_RouterID    DEST_INT_IP
# ----------------  ---------  -------  --------------  -------------  ---------------  -------------
# R1                        1  0.0.0.0  12.1.1.1        Ethernet0/0/0  2.2.2.2          12.1.1.2
# R1                        1  0.0.0.0  14.1.1.1        Ethernet0/0/1  4.4.4.4          14.1.1.4
# R1                        1  0.0.0.0  17.1.1.1        Ethernet0/0/7  7.7.7.7          17.1.1.7