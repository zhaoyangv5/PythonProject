'''
光模块回显信息中有个告警项目，其规律不是很好拿捏！
换句话说，有些模块完好，没告警；有些模块有一条告警；
有些模块有多条。本文通过使用子状态跳转，配合List变量，重点解决这一问题
'''


import textfsm
from tabulate import tabulate

# Value Int (GigabitEthernet\S+)
# Value Date (\S+)
# Value List Alarm (.+)
#
# Start
#   ^.*transceiver information: -> Continue.Record
#   ^${Int}\s
#   ^\s+Manufacturing.+:${Date}
#   ^Alarm information: -> ALARM
#
# ALARM
#   ^\s+${Alarm}
#   ^- -> Start


with open('display_transceiver_ver_template') as f , open('display_transceiver_ver.txt',encoding='utf-8') as output:
    read_table = textfsm.TextFSM(f)
    header = read_table.header
    result = read_table.ParseText(output.read())
    print(tabulate(result, headers=header))



