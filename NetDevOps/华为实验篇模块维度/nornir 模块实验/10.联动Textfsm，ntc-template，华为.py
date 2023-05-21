'''
实验目的

为了能前后对比，我们把实验目标拆解成两个小目标来。

（1）nornir_netmiko，执行 display interface brief 命令（复习）。

（2）nornir_netmiko，调用参数use_textfsm=True，执行 display interface brief 命令，并进行对比。


'''
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from textfsm import TextFSM


nr = InitNornir(config_file="nornir.yaml")
# results = nr.run(netmiko_send_command, command_string= "display interface brief")
results = nr.run(netmiko_send_command, command_string= "display interface brief", use_textfsm = True)
print_result(results)