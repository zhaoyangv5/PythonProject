"""
TextFSM识别的Value实际的值绝大多数为字符串，有一小部分是字符串的列表，需要结合List可选项来使用。
这也和网络配置的实际情况比较相符，比如我们的路由表中存在多个下一跳，Vlan的放行端口等，都可能是多个，也就是列表
"""

from textfsm import TextFSM


"""简单版本List示例"""

# Value Protocol (\S)
# Value Type (\S\S)
# Value Prefix (\S+)
# Value List Gateway (\S+)
# Value Distance (\d+)
# Value Metric (\d+)
# Value LastChange (\S+)
#
# Start
#  ^       -----------        -------                      ----------- ----------- -> Routes
#
# Routes
#  ^  \S \S\S -> Continue.Record
#  ^  ${Protocol} ${Type} ${Prefix}\s+via ${Gateway}\s+${Distance}/${Metric}\s+${LastChange}
#  ^\s+via ${Gateway}

with open('display_router.textfsm') as f, open('display_router.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)
# 其中Gateway的值为列表，且均识别准确无误。从这个示例中我们体会到了List的可选项，它可以将一个Value每识别一次，追加到这个字段的列表中去。
# 如果记录间间隔明确，我们直接在结尾处使用Record即可，如果结尾处Record不妥当，我们就可以适当考虑使用Continue.Record，在文本特征的开始处进行Record

"""复杂版本List示例"""
# Value VLAN_ID (\d+)
# Value NAME (\S+)
# Value STATUS (\S+)
# Value List INTERFACES ([a-zA-Z/\d]+)
#
# Start
#   ^---- -------------------------------- --------- ------------------------------- -> Vlans
#
# Vlans
#  # vlan id处进行记录
#  ^\d+\s+ -> Continue.Record
#  # vlan信息中无相关端口信息的情况，无需继续使用当前文本行
#  ^${VLAN_ID}\s+${NAME}\s+${STATUS}$$
#  # vlan信息中有一个端口的情况，继续使用当前行
#  ^${VLAN_ID}\s+${NAME}\s+${STATUS}\s+${INTERFACES} -> Continue
#  # vlan信息中依次有2、3个端口的情况，继续使用当前行
#  ^(\S+\s+){4}${INTERFACES} -> Continue
#  ^(\S+\s+){5}${INTERFACES} -> Continue
#  # vlan信息中有4个端口的情况，从文本特征而言，已经可以使用下一行文本了
#  ^(\S+\s+){6}${INTERFACES}
#  # 空白符开头，代表这行中仍有端口信息，继续使用当前行识别提取，端口数量可能有3-4个
#  ^\s+ -> Continue
#  # 此行有1个端口的情况，继续使用当前行
#  ^\s+${INTERFACES} -> Continue
#  # 此行有2，3,4个端口的情况，继续使用当前行
#  ^\s+(\S+\s+){1}${INTERFACES} -> Continue
#  ^\s+(\S+\s+){2}${INTERFACES} -> Continue
#  ^\s+(\S+\s+){3}${INTERFACES} -> Continue
#  ^$$ -> EOF

with open('show_vlan.textfsm') as f, open('show_vlan.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)