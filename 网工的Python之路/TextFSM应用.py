'''
TextFSM模板创建
show vlan 例子
命名show_vlan.template
'''
'''Value VLAN_ID(\d+)
Value NAME(\w+)
Value STATUS(\w+)

Start
    ^${VLAN_ID}\s+${NAME}\s+${STATUS}\s+ -> Record'''

from textfsm import TextFSM

#将show vlan的回显以三点形式赋值给output.
output = '''       
N7K# show vlan

VLAN NAME                                    Status         Port
1    defaut                                  active         Eth1
2    VLAN0002                                active         Po100,Eth1/49  
3 
'''

f = open('show_vlan.template')     #调用写好的textfsm模板
template = TextFSM(f)              #调用函数

print(template.ParseText(output))  #进行解析

