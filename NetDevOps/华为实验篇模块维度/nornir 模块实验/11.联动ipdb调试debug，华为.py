'''
对于一些返回值比较复杂的，比如列表套字典，字典套列表，字典套字典，列表套字典套列表套元组……，
如果单用print、type等可能比较难定位目标资源。我们这时候就可以考虑考虑用ipdb来帮忙进行调测了。关于什么是ipdb？这里我直接引用 @弈心 大神文章的介绍哈。

Ipdb全称为IPython pdb，IPython是一种基于Python的交互式解释器，相较于本地的Python解释器（比如IDLE），IPython提供了更为强大的编辑和交互功能。
知道了ipdb中的i是什么意思后，我们再来看pdb。Pdb是Python内置的排错器（debug）模块，pdb提供交互式的界面让用户对代码进行验证和排错，
它支持在源码行间设置（有条件的）断点和单步执行，检视堆栈帧，列出源码列表，以及在任何堆栈帧的上下文中运行任意 Python 代码。它还支持事后调试，可以在程序控制下调用。
所以综上来看，ipdb是基于pdb开发出来的一个针对IPython的第三方排错模块，ipdb之于IPython也就是pdb之于本地的Python解释器，本文将介绍ipdb在Nornir3中的用法。
'''
'''
实验目的

（1）nornir_netmiko，调用参数use_textfsm=True，执行 display interface brief 命令（复习实验10）。

（2）在（1）的基础上，调用ipdb进行调测debug。

（3）剥离ipdb调测，回归常规操作。
'''


import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="nornir.yaml")
output = nr.run(netmiko_send_command, command_string='display interface brief',use_textfsm = True)
print_result(output)

print(output)
# ipdb.set_trace()


#ipdb逐步调测debug
'''
我们看到AggregatedResult (netmiko_send_command)后面好像是个字典，于是考虑用字典键值对索引的方法提取，得到键名'SW1'对应的值，一个MultiResult对象。

ipdb> output['sw1']
MultiResult: [Result: "netmiko_send_command"]
ipdb> 
我们尝试output['sw1'].result，即MultiResult对象的一个属性。

有时候就是试试试给试出来的，反正对话框再手头，你问它答，顶多只会报错，不会电脑爆炸~所以大胆的试。

ipdb> output['sw1'].result
[{'interface': 'GigabitEthernet0/0/1', 'phy': 'up', 'protocol': 'up'}, 
{'interface': 'GigabitEthernet0/0/2', 'phy': 'down', 'protocol': 'down'}, 
{'interface': 'GigabitEthernet0/0/3', 'phy': 'down', 'protocol': 'down'}, 
{'interface': 'GigabitEthernet0/0/4', 'phy': 'down', 'protocol': 'down'}, 
{'interface': 'GigabitEthernet……
返回一个列表，我们尝试取第一项，也即索引为0，继续调试。渐渐地我们看出东西来了是吧？！继续继续。

ipdb> output['192.168.31.100'].result[0]
{'interface': 'GigabitEthernet0/0/1', 'phy': 'up', 'protocol': 'up'}
返回一个字典，我们用键来取值，继续调试。

ipdb> output['192.168.31.100'].result[0]['interface']
'GigabitEthernet0/0/1'
ipdb> 
这样一个复杂且陌生的AggregatedResult对象，就被我们一层一层“抽丝破茧”给探出来了
'''

print (output['192.168.31.100'].result[0]['interface'],
       output['192.168.31.100'].result[0]['phy'])      #GE1/0/0  up