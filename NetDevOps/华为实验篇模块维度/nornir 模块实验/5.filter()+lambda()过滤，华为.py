'''
在filter()中使用lambda来实现单个或多个设备的过滤
Inventory是nornir中最重要部分，包含inventory.hosts和inventory.groups，它们对应的配置文件是hosts.yaml和groups.yaml。
我们在nornir中，通过调用nr.inventory.hosts或nr.inventory.groups即可查inventory中的hosts和groups。
于是，配合filter()简单过滤的功能，我们即可精准地过滤特定设备，再开展操作

'''
'''lambda函数，叫匿名函数。lambda函数的主要作用是让你随时随地构建一个函数'''

def lambda_test(x):
    return x.title()
print(lambda_test('huawei'))

#两段代码其实功能是一致的，都可以把“huawei”处理成“Huawei”

#2 lambda表示
print((lambda x:x.title())('huawei'))


vendors = ['huawei','cisco','juniper']
print(list(filter(lambda x:x=='huawei',vendors)))
#vendors列表共有3个元素，filter()+lambda()配合后，过滤出1个符合条件的，list()处理成列表，然后print出来


from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

#filter+lambda 过滤单台

nr = InitNornir(config_file="nornir.yaml")
targets = nr.filter(filter_func=lambda host: host.name=='192.168.31.101')
#targets = nr.filter(filter_func=lambda host: host.hostname=='192.168.31.101')#用IP进行定位
results = targets.run(netmiko_send_command, command_string='dis arp')
print_result(results)

#filter+lambda 过滤多台 host.name
switches = ['192.168.31.101','192.168.31.102','192.168.31.108']
targets = nr.filter(filter_func=lambda host: host.name in switches)
results = targets.run(netmiko_send_command, command_string='dis arp | inc 31.101')
print_result(results)

##filter+lambda 过滤多台 host.hostname
switches1 = ['192.168.31.100','192.168.31.108']
targets = nr.filter(filter_func=lambda host: host.hostname in switches1)
results = targets.run(netmiko_send_command, command_string='dis arp | inc 31.108')
print_result(results)