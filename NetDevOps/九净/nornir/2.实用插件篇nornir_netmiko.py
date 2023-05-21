"""
从目录结构上而言，它的主要职责有两类：

与设备进行CLI的交互（本书暂时不涉及文件传输相关功能的讲解）。
负责管理netmiko的连接。

我们观察其参数，发现有三个比较重要的:

command_string，字符串类型，发送给网络设备的命令。
use_timing，布尔值，决定在底层是调用Netmiko连接的send_command方法还是send_comman_timing，默认为False，即会调用send_command方法。
enable决定，布尔值，决定是否调用Netmiko连接的enable方法，如果调用，对应的secret参数要配置到Host对象中。
一般情况下，我们只需传入command_string这个参数即可。其他两个参数按需进行赋值。
此外，在netmiko_send_command还可以传入任Netmiko的send_command和send_command_timing支持的参数，
这些参数都会透传给这两个方法，比如expect_string、use_textfsm等等。
"""
"""
netmiko_send_command函数执行完成后会将Netmiko执行的结果包装到Result对象中去，
如果我们使用了textfsm，且解析出了数据，则Result对象中的result属性会是结构化数据，
我们未使用textfsm或者解析失败，则result属性的值会是show出来的回显文本。
"""
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=netmiko_send_command,
                 command_string='display version',
                 use_textfsm=True,
                 textfsm_template='huawei_display_version.textfsm')
print_result(results)


"""netmiko_send_config函数"""
# 配置命令config_commands一定是字符串列表（或者元组），我们也可以写成一个多行的字符串，然后用splitlines做切割。
# 然后初始化Nornir对象，调用其run方法，赋值参数task指定其调用netmiko_send_config函数，赋值需要透传给task函数的参数config_commands为config_cmds，
# 然后打印结果即可
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

config_cmds = """interface GE1/0/0
description configed by nornir_netmiko
commit""".splitlines()

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=netmiko_send_config, config_commands=config_cmds)
print_result(results)


#也可以通过配置文件的方式进行配置，首先准备一个配置的文本文件，配置内容与代码中相同，文件命名用户自己定义
nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=netmiko_send_config, config_file='config.txt')   #config_file 配置文件
print_result(results)

"""提交生效"""

# 部分网络设备刷入配置后，不会立即生效，需要执行commit操作，我们只需要调用netmiko_commit函数即可，它会执行对应设备的commit命令。
# 鉴于Netmiko会对众多设备进行适配，理论上我们只需调用此task函数即可，
# 实际情况，如果对应方法不完善，我们可能需要调用netmiko_send_command函数，结合expect等进行交互完成配置提交生效。比如像华为的CE交换机系列，需要在命令行中传入commit命令。
# 一些其他国外的设备，我们直接调用commit这个task函数即可，此处代码仅做演示，在实际使用中一定结合实际情况。

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config, netmiko_commit

nr = InitNornir(config_file="nornir.yaml")
config_results = nr.run(task=netmiko_send_config, config_file='config.txt')
print_result(config_results)

commit_results = nr.run(task=netmiko_commit)
print_result(commit_results)


"""保存"""
# Netmiko对于主流网络设备的save方法是比较完善的，我们一般直接调用netmiko_save_config函数即可。此处代码做演示，实际中要结合设备型号的具体操作稍微调整。

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config, netmiko_save_config

nr = InitNornir(config_file="nornir.yaml")
config_results = nr.run(task=netmiko_send_config, config_file='config.txt')
print_result(config_results)

save_results = nr.run(task=netmiko_save_config)
print_result(save_results)

"""获取nornir_netmiko中创建的连接"""
# 有时候需要频繁与网络设备交互，频繁调用nornir_netmikotask函数，可能仍有一些开销，另外有一些其他的业务逻辑上的问题。
# 这个时候我们希望能够自己创建一个Netmiko的连接，一种思路是获取Host对象中的相关信息，自己构建Netmiko连接，可以参考如下代码
from netmiko import ConnectHandler
from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_utils.plugins.functions import print_result


def my_func_using_netmiko(task_context: Task, show_cmds):
    dev_info = {
        'ip': task_context.host.hostname,
        'username': task_context.host.username,
        'password': task_context.host.password,
        'device_type': task_context.host.platform,
        'port': task_context.host.port,

    }
    outputs = []
    with ConnectHandler(**dev_info) as net_conn:
        for cmd in show_cmds:
            outputs.append(net_conn.send_command(cmd))
    return Result(host=task_context.host, result=outputs)

if __name__ == '__main__':

    show_cmds = ['display version', 'display interface']

    nr = InitNornir(config_file="nornir.yaml")
    results = nr.run(task=my_func_using_netmiko, show_cmds=show_cmds)
    print_result(results)


# 如果一个task函数被反复调用就会反复地创建到网络设备的连接，开销有点“浪费”
# 由于nornir_netmiko的connection会帮助我们“智能”管理维护Netmiko连接，会大大减少这方面的“浪费”
# 直接调用net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)即可
from netmiko import ConnectHandler
from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_utils.plugins.functions import print_result

def my_func_using_netmiko(task_context: Task, show_cmds):
    outputs = []
    net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)
    for cmd in show_cmds:
        outputs.append(net_conn.send_command(cmd))
    return Result(host=task_context.host, result=outputs)

if __name__ == '__main__':

    show_cmds = ['display version', 'display interface']

    nr = InitNornir(config_file="nornir.yaml")
    results = nr.run(task=my_func_using_netmiko, show_cmds=show_cmds)
    print_result(results)