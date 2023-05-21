

# 通过os模块，修改当前目录
import os
os.chdir(r"/Users/domic/PycharmProjects/PythonProject/NetDevOps/华为实验篇模块维度/nornir 模块实验")
print(os.getcwd())


#几条指令在解释器直接敲，看回显内容
from nornir import InitNornir
nr = InitNornir(config_file='nornir.yaml')
print(nr.inventory.hosts)
print(nr.inventory.groups)

print(nr.inventory.hosts['192.168.31.100'].platform)
print(nr.inventory.hosts['192.168.31.100'].username)
print(nr.inventory.hosts['192.168.31.100'].password)
print(nr.inventory.hosts['192.168.31.101'].hostname)
print(nr.inventory.hosts['192.168.31.102'].hostname)
print(nr.inventory.hosts['192.168.31.108'].hostname)

print(nr.inventory.groups['huawei_group1'].platform)
print(nr.inventory.groups['huawei_group2'].platform)


#修改hosts.yaml文件，配合filter()
# data下面的键值对起的仅是备注的作用，building、level等字眼可以随意修改成别的，看你喜欢。
# 特别注意1、2值得话，如果是纯数字，一定要加引号，如果有带字母就不用引号啦.
# data	       sw1	sw2	sw3	sw4
# building	   1	1	2	2
# level	       1	2	1	2
# 可以是其它信息

from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="nornir.yaml")
targets = nr.filter(building='1')
# targets = nr.filter(building='2')
# targets = nr.filter(level='1')
#其它参数调整，比如building改成‘2’，就会只处理sw3、sw4。我们也可以修改level的值，还可以自定义其它的值。
results = targets.run(netmiko_send_command, command_string='dis arp ')

print_result(results)



