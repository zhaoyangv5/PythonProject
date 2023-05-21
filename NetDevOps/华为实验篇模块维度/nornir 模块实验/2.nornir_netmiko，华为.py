'''
实验背景

正好之前做了netmiko的一些实验，我们对netmiko的一些操作都有所了解。Nornir中有个nornir_netmiko模块来联动netmiko。我们来简单复习一下netmiko模块中几个向设备推送指令大函数。

（1）send_command()：向设备发送一条命令，通常用于查询、排错、保存等命令。

（2）send_config_set()：向设备发送一条或多条配置命令，会自动适配到配置模式，通常配合指令列表。

（3）send_config_from_file()：如 send_config_set() 指令列表过大，可单独放入文本中配合 send_config_from_file() 调用。

（4）send_command_timing()：主动延迟等待，主要用于应对设备交互管理平台回显量大出现有意延迟或异常卡顿的现象。（初学者少用，但其它函数遇到问题时，可尝试用它。）

实验目的

通过 PC（192.168.11.2，Python所在，Pycharm环境），连接 Layer3Switch-1（192.168.11.11）

调用 nornir_netmiko，执行display clock检查设备时钟，回显打印。
'''

# nornir_napalm是huawei_vrp，咱们这次用nornir_netmiko是huawei

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(netmiko_send_command, command_string='display clock')
print(type(results))
print(results)
#nr.run()返回的值的类型为nornir.core.task.AggregatedResult，必须用nornir.utils里的print_result()才能将它完整打印出来
print_result(results)