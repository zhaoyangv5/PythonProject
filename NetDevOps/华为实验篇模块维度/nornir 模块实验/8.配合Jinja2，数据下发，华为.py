'''
实验目的

实验目的是Layer3Switch-1、Layer3Switch-2上配置BGP邻居，然后各自宣告自己的Loopback0口网段进入BGP中。我们分解成小目标。

（1）nornir_jinja2模块安装，完成Jinja2模板及YAML文件的制作。

（2）模板内容通过nornir+Jinja2配合，Jinja2渲染生成实际配置脚本，nornir下发至Layer3Switch-1、Layer3Switch-2。
'''

from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
from nornir_netmiko import netmiko_send_command, netmiko_send_config

def load_data(task):
    data = task.run(task=load_yaml,file=f'{task.host}.yaml')
    # data = task.run(task=load_yaml,file=f'{task.host}.yaml')利用任务task=load_yaml，
    # 配合host.yaml文件进行YAML配置读取任务加载，
    # 此时全部Layer3Switch都会执行，即sw1.yaml、sw2.yaml、sw3.yaml、sw4.yaml。
    # 但实际我们只准备了前两个yaml文件，所以涉及到后两个会为空。不用怕，我们已经过了高级过滤，
    # 所以最后就是关于Layer3Switch-1和Layer3Switch-2的任务，即huawei_group1的任务
    task.host["asn"] = data.result["asn"]
    #几行task.host["XXX"] = data.result["XXX"]都是类似的，为的是给jinja2模板BGP.j2提供一些必要的参数集，其实您理解成填表过程
    task.host["neighbor"] = data.result["neighbor"]
    task.host["remoteas"] = data.result["remote-as"]
    task.host["loopbacks"] = data.result["loopbacks"]
    task.host["networks"] = data.result["networks"]
    #有了要执行的参数集，我们又启动另一个任务，开始渲染，BGP.j2在当前目录，所以path=""。这个任务我们给个变量，叫rendering
    rendering = task.run(task=template_file, template="bgp.j2", path="")
    #rendering.result装的就是渲染的结果，即要下发的配置指令装在里面了，此时我们又再启动另一个任务task=netmiko_send_config
    task.run(task=netmiko_send_config, config_commands=rendering.result.split('\n'))

nr = InitNornir(config_file="nornir.yaml")   #初始化一个InitNornir对象nr
group1 = nr.filter(F(groups__contains="huawei_group1"))  #通过高级过滤F()功能，筛选出属于huawei_group1的设备，即对象group1
r = group1.run(task=load_data)   #通过对象group1的run方法，调用自定义函数load_data(task)
print_result(r)