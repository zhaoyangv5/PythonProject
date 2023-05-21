"""
关于Rule的编写也比较简单，像我们平时用正则解析网络配置那样即可，同时提醒大家要注意以下几点：

待提取的字段要符合TextFSM的语法规范，用${ValueName}代替。
同一个Value我们可以写多条Rule去匹配，实现不同型号之间的兼容
Rule的先后顺序，笔者建议一定要和其在网络配置中出现的顺序一致，可以保证准确度、提高可读性。
在最后一个字段信息收集完成之后一定要显式地执行Record，根据配置长度，为了节约资源可以进行EOF的状态转移。
"""

from textfsm import TextFSM
from tabulate import tabulate
import pprint
import re

"""单条普通数据提取"""

with open('display_version.textfsm') as f, open('display_version.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    # header = re_table.header            #提取FSM关键字段（表头）
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    # result1 = re_table.ParseText(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)
    # print(tabulate(result1,headers=header))


"""条形表数据提取"""
with open('display_int_brief.textfsm') as f, open('display_int_brief.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)
# 我们发现数据提取出来了，但是有点小问题——我们把表头也提取出来了。这是因为这个Rule写的颗粒度比较粗，而表头恰好符合Rule，从而被识别并提取出来。
# 解决这个问题，方法非常多。笔者给出其中两种方案：
# 细化Value中的正则表达式部分，使干扰项不被匹配到。
# 识别出表头，借助状态转移，在新的端口列表的识别状态中去识别端口.

#解决方法1： Value Name (GE\d\S+|NULL\S+|MEth\S+)
with open('display_int_brief-1.textfsm') as f, open('display_int_brief.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)

#解决方法2： 状态转移
# 在Start状态中不进行信息的提取，我们只在这个状态进行表头的识别，
# 当识别出表头的时候我们立刻进行状态转移的Action，进入我们自己定义的一个新的State——Interface，在这状态中，我们只有一条Rule进行相关信息的提取

# Start
#  ^Interface                  PHY      Protocol  InUti OutUti   inErrors  outErrors -> Interface
#
# Interface
#  ^${Name}\s+${PhyState}\s+${ProtocolState}\s+${InUti}\s+${OutUti}\s+${InErrors}\s+${OutErrors} -> Record
with open('display_int_brief-2.textfsm') as f, open('display_int_brief.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)

"""普通块状表数据提取"""

"""1.以块结尾为块间隔的识别方法"""
# 每块数据的末尾都是一个空白行。我们只需按照普通数据的提取模式进行处理，最后写一个Rule，在分隔点进行记录即可。
# 需要注意的是，代表文本结尾的元字符在TextFSM中是用$$表示的，这是因为，Value在Rule中的引用是${ValueName}，在这个中也出现了$，
# 为了TextFSM识别更方便，不产生冲突，所以文本结尾的元字符必须以$$代替，那一个空白行在Rule中的正则表达式即^$$——一个只有开始和结束的文本
with open('display-interface.textfsm') as f, open('display-interface.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)


"""2.以块开始为块间隔的识别方法"""
# 在实际生产中，网络配置多种多样，比如display interface这种端口配置，有的设备每个端口之间用空白行隔开，
# 如果是display current-configuration这种去查看端口的配置，有的是"!"间隔开。
# 而有的厂商型号的这种块状数据，在末尾没有明显的分隔点，或者分隔点可能是一些不同内容的配置（有些有配置，可以作为分隔点，有些配置项中又无此配置，需以另外一种配置作为分隔点）。
# 这个时候我们就可以反过来考虑，不以块的结尾作为分隔点，而是以块的开始作为分隔点。我们在分隔点的位置一定要进行一次记录（执行Record Action），在块结尾比较好处理。但是在块开始的时候会需要一点点”设计"
with open('display-interface1.textfsm') as f, open('display-interface1.log') as output:
    re_table = TextFSM(f)           #通过模板建立状态机FSM（生产模具）,re_table 代表用template文件内容处理后的一个状态机
    result = re_table.ParseTextToDicts(output.read())      #用状态机FSM处理CLI 回显信息
    print(result)

# “Continue.Record”的精髓在于识别块开始的文本，并不进行信息提取，而是继续使用当前行文本，同时将识别到的上一个数据追加到结果数据列表中。
# 最后利用默认的EOF状态及其默认的记录追加功能实现最后一个数据项的追加