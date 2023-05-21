
from textfsm import TextFSM
from tabulate import tabulate
from pprint import pprint



with open('read_policy.textfsm') as f, open('华三M9008.log','r') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    pprint(result)