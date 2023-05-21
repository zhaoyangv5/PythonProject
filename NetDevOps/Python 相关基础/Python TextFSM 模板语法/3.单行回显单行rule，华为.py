import textfsm
from tabulate import tabulate

with open('display_clock_template') as f, open('display_clock.txt') as output:
    re_table = textfsm.TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    header = re_table.header            #提取FSM关键字段（表头）
    result = re_table.ParseText(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)
    print(tabulate(result, headers=header))
