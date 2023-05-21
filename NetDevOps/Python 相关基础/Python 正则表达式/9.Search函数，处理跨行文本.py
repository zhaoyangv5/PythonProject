'''
报文回显实际是一大串字符串（str）信息，我们简单理解它是“非结构化”数据。我们进行报文解析操作，就是为了让这些信息变成“结构化”数据
我们的实验目的是从这个回显出发，用正则表达式结合python脚本，把相关字段信息提取，整合成键值对。键值对还进行嵌套，即字典中有字典
'''

import re
from pprint import pprint

print('\n'+'*'*20+'版本一:分散正则表达式'+'*'*25)
'''版本一:分散正则表达式'''

# filename = r'display_ospf_peer.txt'
# result = {}
# with open(filename, 'r') as f:
#     for line in f:
#         # print(line)
#         if line.startswith(' Router ID:'):
#             neighbor = re.search(r' Router ID: (\S+)\s+Address: (\S+)', line)
#             neighbor_id = neighbor.group(1)
#             # print(neighbor_id)
#             neighbor_ip = neighbor.group(2)
#             # print(neighbor_ip)
#             result[neighbor_id] = {}
#             result[neighbor_id]['neighbor_int_ip'] = neighbor_ip
#             # print(result)
#         elif line.startswith('   DR: '):
#             dr_bdr = re.search(r'   DR: (\S+)\s+BDR: (\S+)', line)
#             dr = dr_bdr.group(1)
#             result[neighbor_id]['dr'] = dr
#             bdr = dr_bdr.group(2)
#             result[neighbor_id]['bdr'] = bdr
#         elif line.startswith('   Neighbor is up for '):
#             upfor = re.search(r'  Neighbor is up for (\S+)', line).group(1)
#             print(upfor)
#             result[neighbor_id]['upfor'] = upfor
#
# print(result)
# pprint('\n\n')
# pprint(result)


print('\n'+'*'*20+'版本二:集中正则表达式'+'*'*25)
'''版本二:集中正则表达式'''


filename = r'display_ospf_peer.txt'
result = {}

regex = (' Router ID: (?P<neighbor_id>\S+)\s+Address: (?P<neighbor_int_ip>\S+)'
         '|   DR: (?P<dr>\S+)  BDR: (?P<bdr>\S+)'
         '|   Neighbor is up for (?P<upfor>\S+)')

with open(filename) as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            # print(match.groupdict())
            # print(match.groupdict()['neighbor_id'])
            if match.groupdict()['neighbor_id']:
                neighbor_id = match.groupdict()['neighbor_id']      #捕获邻居，neighbor_id
                result[neighbor_id] = {}                            #以邻居为键，创建一个字典
                # print(result)

                for each in match.groupdict():              #处理同行的其他捕获信息，如neighbor_int_ip
                    if match.groupdict()[each] and each != 'neighbor_id':
                        # print(each)
                        result[neighbor_id][each] = match.groupdict()[each]     #嵌套字典，将捕获的neighbor_int_ip赋值
                        # print(result)

            else:           #如果match.groupdict()['neighbor_id']为空值，进行循环
                # print(match.groupdict())
                for each in match.groupdict():
                    if match.groupdict()[each]:         #循环的值键如果有value,进行下一步
                        # print(each)
                        result[neighbor_id][each] = match.groupdict()[each]

# print(result)
print('\n\n')
pprint(result)



