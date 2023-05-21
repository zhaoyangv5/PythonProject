'''
实验目的

（1）准备脚本文件，使用netmiko_send_config进行配置。

（2）使用netmiko_send_command进行配置检查，做个复习

'''
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result, print_title

nr = InitNornir(config_file="nornir.yaml")

def config(huawei):
    huawei.run(task=netmiko_send_config, config_file='commands.cfg')   #netmiko_send_config配合配置文件commands.cfg
    huawei.run(task=netmiko_send_command, command_string='display vlan summary')  #netmiko_send_command来检查netmiko_send_config的配置情况

print_title('正在配置VLAN999')   #这里我们还用到print_title函数,来做任务实施提示
results = nr.run(task=config)

print_result(results)