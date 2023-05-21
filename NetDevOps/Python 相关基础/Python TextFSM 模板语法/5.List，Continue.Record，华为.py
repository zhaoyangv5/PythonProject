

'''
如果规则中我们书写了动作，比如Record，则同时会执行Next默认动作。
Next默认动作是啥？当前带动作的规则执行后（比如执行Record记录），这行输入文本随之结束，TextFSM引擎读取下一行输入文本（待匹配文本），重新开始匹配。

我们可以人为地将Next默认动作修改掉，改成Continue动作。Continue动作是啥？
当前带动作的规则执行后（比如执行Record记录），TextFSM引擎不读取下一行输入文本（待匹配文本），而继续匹配下一行规则。

Record动作不明确指出Continue，则默认就是Next——Next.Record!
'''

import sys
import textfsm
from tabulate import tabulate

'''Value Tru_INT (Eth-Trunk\d+)
Value PHY (up|down|\*down)
Value Protocol (up|down)
Value Phy_INT (GigabitEthernet\d+/\d+/\d+)

Start
  ^${Tru_INT}\s+${PHY}\s+${Protocol}\s -> Record
'''

# with open('display_interface_brief_template') as f, open('display_interface_brief.txt') as output:
#     re_table = textfsm.TextFSM(f)
#     header = re_table.header
#     result = re_table.ParseText(output.read())
#     print(tabulate(result, headers=header))

# Tru_INT      PHY    Protocol    Phy_INT
# -----------  -----  ----------  ---------
# Eth-Trunk3   up     down
# Eth-Trunk4   up     down
# Eth-Trunk5   up     down
# Eth-Trunk6   up     down
# Eth-Trunk8   *down  down
# Eth-Trunk11  up     down
# Eth-Trunk13  up     up
# Eth-Trunk14  up     up
# Eth-Trunk17  up     down
# Eth-Trunk18  up     down
# Eth-Trunk20  up     up
# Eth-Trunk22  up     down
# Eth-Trunk23  up     up

'''
Value Tru_INT (Eth-Trunk\d+)
Value PHY (up|down|\*down)
Value Protocol (up|down)
Value Phy_INT (GigabitEthernet\d+/\d+/\d+)

Start
  ^${Tru_INT}\s+${PHY}\s+${Protocol}\s -> Record
  ^\s+${Phy_INT} -> Record
'''

# with open('display_interface_brief_template') as f, open('display_interface_brief.txt') as output:
#     re_table = textfsm.TextFSM(f)
#     header = re_table.header
#     result = re_table.ParseText(output.read())
#     print(tabulate(result, headers=header))

# Tru_INT      PHY    Protocol    Phy_INT
# -----------  -----  ----------  ---------------------
# Eth-Trunk3   up     down
#                                 GigabitEthernet8/1/2
#                                 GigabitEthernet10/0/4
# Eth-Trunk4   up     down
#                                 GigabitEthernet8/1/0
#                                 GigabitEthernet10/0/3
# Eth-Trunk5   up     down
#                                 GigabitEthernet6/0/3
#                                 GigabitEthernet8/1/6
#...

'''
Value Filldown Tru_INT (Eth-Trunk\d+)
Value Filldown PHY (up|down|\*down)
Value Filldown Protocol (up|down)
Value Required Phy_INT (GigabitEthernet\d+/\d+/\d+)

Start
  ^${Tru_INT}\s+${PHY}\s+${Protocol}\s -> Record
  ^\s+${Phy_INT} -> Record
'''
# with open('display_interface_brief_template') as f, open('display_interface_brief.txt') as output:
#     re_table = textfsm.TextFSM(f)
#     header = re_table.header
#     result = re_table.ParseText(output.read())
#     print(tabulate(result, headers=header))


'''list'''
'''
Value Tru_INT (Eth-Trunk\d+)
Value PHY (up|down|\*down)
Value Protocol (up|down)
Value List Phy_INT (GigabitEthernet\d+/\d+/\d+)

Start
  ^${Tru_INT}\s+${PHY}\s+${Protocol}\s -> Record
  ^\s+${Phy_INT} -> Record
'''
# with open('display_interface_brief_template') as f, open('display_interface_brief.txt') as output:
#     re_table = textfsm.TextFSM(f)
#     header = re_table.header
#     result = re_table.ParseText(output.read())
#     print(tabulate(result, headers=header))

# Tru_INT      PHY    Protocol    Phy_INT
# -----------  -----  ----------  -------------------------
# Eth-Trunk3   up     down        []
#                                 ['GigabitEthernet8/1/2']
#                                 ['GigabitEthernet10/0/4']
# Eth-Trunk4   up     down        []
#                                 ['GigabitEthernet8/1/0']
#                                 ['GigabitEthernet10/0/3']
'''
Value Tru_INT (Eth-Trunk\d+)
Value PHY (up|down|\*down)
Value Protocol (up|down)
Value List Phy_INT (GigabitEthernet\d+/\d+/\d+)

Start
  ^${Tru_INT}\s+${PHY}\s+${Protocol}\s -> Record
  ^\s+${Phy_INT}
'''
# with open('display_interface_brief_template') as f, open('display_interface_brief.txt') as output:
#     re_table = textfsm.TextFSM(f)
#     header = re_table.header
#     result = re_table.ParseText(output.read())
#     print(tabulate(result, headers=header))     #结果错位

# Tru_INT      PHY    Protocol    Phy_INT
# -----------  -----  ----------  ----------------------------------------------------------------------------------------------------
# Eth-Trunk3   up     down        []
# Eth-Trunk4   up     down        ['GigabitEthernet8/1/2', 'GigabitEthernet10/0/4']
# Eth-Trunk5   up     down        ['GigabitEthernet8/1/0', 'GigabitEthernet10/0/3']
# Eth-Trunk6   up     down        ['GigabitEthernet6/0/3', 'GigabitEthernet8/1/6']

'''Continue.Record'''

'''
Value Tru_INT (Eth-Trunk\d+)
Value PHY (up|down|\*down)
Value Protocol (up|down)
Value List Phy_INT (GigabitEthernet\d+/\d+/\d+)

Start
  ^Eth-Trunk\d+ -> Continue.Record
  ^${Tru_INT}\s+${PHY}\s+${Protocol}\s
  ^\s+${Phy_INT}
'''

with open('display_interface_brief_template') as f, open('display_interface_brief.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))

# Tru_INT      PHY    Protocol    Phy_INT
# -----------  -----  ----------  ----------------------------------------------------------------------------------------------------
# Eth-Trunk3   up     down        ['GigabitEthernet8/1/2', 'GigabitEthernet10/0/4']
# Eth-Trunk4   up     down        ['GigabitEthernet8/1/0', 'GigabitEthernet10/0/3']
# Eth-Trunk5   up     down        ['GigabitEthernet6/0/3', 'GigabitEthernet8/1/6']
# Eth-Trunk6   up     down        ['GigabitEthernet2/1/10']
# Eth-Trunk8   *down  down        []
# Eth-Trunk11  up     down        ['GigabitEthernet2/1/20', 'GigabitEthernet2/1/21', 'GigabitEthernet2/1/22', 'GigabitEthernet2/1/23']
# Eth-Trunk13  up     up          ['GigabitEthernet2/0/1', 'GigabitEthernet6/0/0']
# Eth-Trunk14  up     up          ['GigabitEthernet2/0/0', 'GigabitEthernet6/1/0']
# Eth-Trunk17  up     down        ['GigabitEthernet4/1/15']
# Eth-Trunk18  up     down        ['GigabitEthernet4/0/6', 'GigabitEthernet4/1/14']
# Eth-Trunk20  up     up          ['GigabitEthernet8/1/9']
# Eth-Trunk22  up     down        ['GigabitEthernet10/0/5', 'GigabitEthernet10/1/0']
# Eth-Trunk23  up     up          ['GigabitEthernet6/0/1', 'GigabitEthernet10/0/1']