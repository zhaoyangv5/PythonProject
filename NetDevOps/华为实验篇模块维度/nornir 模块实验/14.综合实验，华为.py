"""
实验目的

（1）Nornir结合Textfsm，找出hosts.yaml设备中的trunk和access端口。（复习lab10内容）

（2）Nornir用description命令将trunk口，描述配置为：Trunk Port (Nornir)。

（3）Nornir用description命令将access口，描述配置为：Access Port to VLAN xxx (Nornir)。xxx为VLAN号。

（4）Nornir检查结果。
"""

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="nornir.yaml")
output = nr.run(netmiko_send_command, command_string='display current-configuration | be interface GE',
                use_textfsm=True)

# print_result(output)
# netmiko_send_command************************************************************
# * sw1 ** changed : False *******************************************************
# vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
# [ {'interface': 'GigabitEthernet0/0/1', 'mode': 'access', 'vlan': ''},
#   {'interface': 'GigabitEthernet0/0/2', 'mode': 'trunk', 'vlan': ''},
#   {'interface': 'GigabitEthernet0/0/3', 'mode': 'access', 'vlan': '999'}]
# ^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

for switch in output.keys():
    # print(output[switch].result)  #这种可以用来调测，探寻返回是啥，具体操作思路在lab11、12中介绍了。
    for i in range(len(output[switch].result)):
        trunk_cmd = ['interface ' + output[switch].result[i]['interface'], 'description Trunk Port (Nornir)', 'commit']
        access_cmd = ['interface ' + output[switch].result[i]['interface'], 'description Access Port to VLAN ' +
                      (output[switch].result[i]['vlan'] if output[switch].result[i]['vlan'] else '1') + ' (Nornir)', 'commit']
        # print(trunk_cmd,',', access_cmd)
        # print(output[switch].result[i])
        # print(output[switch].result[i]['mode'])
        if 'trunk' in output[switch].result[i]['mode']:
            nr.run(netmiko_send_config, config_commands=trunk_cmd)
            print(switch, output[switch].result[i]['interface'], '已配置完成')
        elif 'access' in output[switch].result[i]['mode']:
            nr.run(netmiko_send_config, config_commands=access_cmd)
            print(switch, output[switch].result[i]['interface'], '已配置完成')

results = nr.run(netmiko_send_command, command_string='display interface description | inc Nornir')
print_result(results)
