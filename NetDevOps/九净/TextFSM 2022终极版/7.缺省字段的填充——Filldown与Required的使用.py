"""
Value Slot (\d)
Value State (\w+)
Value Temperature (\d+)
Value DRAM (\d+)
Value Buffer (\d+)

Start
 ^\s+${Slot}\s+${State}\s+${Temperature}\s+\d+\s+\d+\s+${DRAM}\s+\d+\s+${Buffer} -> Record
 ^\s+${Slot}\s+${State} -> Record
"""

from textfsm import TextFSM

with open('filldown_Required.textfsm') as f, open('filldown_Required.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)

#上述缺少机框信息

# Value Filldown Chassis (\S+)
# Value Slot (\d)
# Value State (\w+)
# Value Temperature (\d+)
# Value DRAM (\d+)
# Value Buffer (\d+)
#
# Start
#  ^${Chassis}:
#  ^\s+${Slot}\s+${State}\s+${Temperature}\s+\d+\s+\d+\s+${DRAM}\s+\d+\s+${Buffer} -> Record
#  ^\s+${Slot}\s+${State} -> Record

with open('filldown_Required.textfsm') as f, open('filldown_Required.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)
# 总体符合预期，但是发生了一点小意外，最后莫名其妙多了一条数据{'Chassis': 'lcc1-re1', 'Slot': '', 'State': '', 'Temperature': '', 'DRAM': '', 'Buffer': ''}
# 是由于Filldown可选项和TextFSM机制导致的：在每次Record一条记录之后，TextFSM都会创建一条空的记录，TextFSM最终不会保留空记录到待返回数据中心。
# 而加入了Filldown之后，在最后一条信息识别提取并记录后，TextFSM立刻创建了一条空记录，并同时把之前的Chassis字段填充到了这个空记录的对应位置，
# TextFSM判定自己进入了EOF状态（文本已经读取结束），发现有一条非空记录（由于Filldown引起的），所以默认会执行Record操作，将这条非空记录追加到结果中去。
# 为了避免这种问题，我们可以使用可选项”Required“，配置了此可选项的字段必须非空，才会被追加到结果数据中去。
# 观察上述网络配置为文本，我们发现槽位编号和状态是非空的，我们选择其一添加”Required“可选项，
# 它会告诉TextFSM，定义了此可选项的Value必须非空才能被追加到待返回数据结果中，否则进行丢弃处理

# Value Filldown Chassis (\S+)
# Value Required Slot (\d)
# Value State (\w+)
# Value Temperature (\d+)
# Value DRAM (\d+)
# Value Buffer (\d+)
#
# Start
#  ^${Chassis}:
#  ^\s+${Slot}\s+${State}\s+${Temperature}\s+\d+\s+\d+\s+${DRAM}\s+\d+\s+${Buffer} -> Record
#  ^\s+${Slot}\s+${State} -> Record
with open('filldown_Required.textfsm') as f, open('filldown_Required.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)