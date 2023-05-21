'''
需要学会开启netmiko的debug模式，将netmiko底层运作的相关信息输出出来，同时也建议在初始化netmiko连接的同时将整个session进行日志记录。
这两个方法有助于我们快速定位问题。如果开启debug模式，对于大家有困难，我们也可以选择后者，常见问题在netmiko的session日志当中也比较容易定位
'''

import logging
from netmiko import ConnectHandler

logging.basicConfig(level=logging.DEBUG)

dev = {'device_type': 'huawei',
       'host': '192.168.31.100',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
       'session_log': 'session.log'
       }

with ConnectHandler(**dev) as conn:
    output = conn.send_command(command_string='display version')
    print(output)