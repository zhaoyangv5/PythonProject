'''
YAML是一个可读性高，用来表达数据序列化的格式
基本语法：
类似Python，YAML也用缩进方式来布局它的文本结构，区别在于Python用制表符，
而YAML用空格符。另一个与Python类似的则是注释符#，从#开始到该行结束均为注释内容
'''
'''
列表
[port link-type access,port default vlan 110,port discard tagged-packet,port link-flap protection enable]

当列表为一项一行时，每项需以``- ``（减号、空格）开头。减号前也是可以有空格的，但同一个列表中，每一项减号前的空格都要在同个缩进级别
- port link-type access
- port default vlan 110
- port discard tagged-packet
- port link-flap protection enable
'''

'''
字典
{link-type: access, vlan: 110}

也可以写成块状表单。
link-type: access
vlan: 110
'''

'''
字符串（Strings）
YAML中的字符串可以不用引号括起来，但如果遇到对YAML来说是特殊字符的，则需要加引号
command: "display  interface | include rate:"
|	保留每行尾部的换行符\n。
>	删除每行尾部的换行符\n。
'''

'''
组合使用（字典值为列表）
access:
- port link-type access
- port default vlan 110
- port discard tagged-packet
- port link-flap protection enable

trunk:
- port priority 5
- port link-type trunk
- port trunk allow-pass vlan 100
- port link-flap interval 50
- port type uni

如果是JSON的就是这样
{
  "access": [
    "port link-type access",
    "port default vlan 110",
    "port discard tagged-packet",
    "port link-flap protection enable"
  ],
  "trunk": [
    "port priority 5",
    "port link-type trunk",
    "port trunk allow-pass vlan 100",
    "port link-flap interval 50",
    "port type uni"
  ]
}

如果在Python结构中，是这样的
{'access': ['port link-type access', 'port default vlan 110', 'port discard tagged-packet', 'port link-flap protection enable'], 'trunk': ['port priority 5', 'port link-type trunk', 'port trunk allow-pass vlan 100', 'port link-flap interval 50', 'port type uni']}
'''

'''
组合使用（列表元素为字典）
- Portid: 1
  type: access
  vlan: 101
  desc: Ut2CR
  to_id: 1
  to_name: RT01
- Portid: 2
  type: access
  vlan: 105
  desc: Dt2SW
  to_id: 1
  to_name: SW01
- Portid: 3
  type: access
  vlan: 120
  desc: Pt2PE
  to_id: 13
  to_name: PE03
'''

'''PyYAML模块'''
import yaml

print('*'*20+'PyYAML模块读取'+'*'*25)
print('\n'+'*'*20+' yaml.safe_load'+'*'*25)

'''PyYAML模块读取'''
from pprint import pprint

with open('info.yaml', 'r') as f:
    templates = yaml.safe_load(f)

print(templates)
print('\n')
pprint(templates)
#YAML文件用来存放一些设备运行参数，尤其是在需要经常手工修改的场景。所以，nornir用它来做设备清单资源管理


'''YAML文件写入'''
print('*'*20+'PyYAML模块写入'+'*'*25)
print('\n'+'*'*20+'yaml.dump'+'*'*25)

access_template = [
    "port link-type access", "port default vlan 110",
    "port discard tagged-packet", "port link-flap protection enable"
]

trunk_template = [
    "port priority 5", "port link-type trunk",
    "port trunk allow-pass vlan 100", "port link-flap interval 50",
    "port type uni"
]

to_yaml = {'trunk': trunk_template, 'access': access_template}

# print(type(to_yaml))
# print(to_yaml)

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)

with open('sw_templates.yaml') as f:
    print(f.read())
