'''
在Nornir中，可以使用filter()以及在filter()里配合F()函数来做过滤，前者叫做简单过滤（simple filtering），后者叫做高级过滤（advanced filtering）。
针对过滤的内容我将分成三个实验来讲，实验3中我将介绍filter配合F()函数做过滤的方法，实验4中我将介绍使用filter()过滤的方法，
实验5中我将介绍filter()配合lambda来做过滤的方法
'''



from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="nornir.yaml")
group1 = nr.filter(F(groups__contains="huawei_group1"))
group2 = nr.filter(~F(groups__contains="huawei_group1"))
results = group1.run(netmiko_send_command, command_string='display ip int brief')
print_result(results)

# 1、波浪线~表示取非操作；
# 2、groups__contains中是两行下划线；

# 3、末尾都是“huawei_group1”。结合拓扑翻译一下：
# 变量	                代码操作	                  指向的交换机
# group1	filter()配合F()，即huawei_group1	       sw1、sw2
# group2	filter()配合F()取非，即 huawei_group2	   sw3、sw4


#要对huawei_group2进行操作
results1 = group2.run(netmiko_send_command, command_string='display ip int brief')
print_result(results1)

#不想过滤分组
results2 = nr.run(netmiko_send_command, command_string='display ip int brief')
print_result(results2)

