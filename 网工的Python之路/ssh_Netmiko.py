from netmiko import ConnectHandler

sw2 = {'device_type': 'huawei',
       'ip': '10.211.55.100',
       'username': 'huawei',
       'password': 'huawei@123',
       }

connect = ConnectHandler(**sw2)
print("Successfully connnect to " + sw2['ip'])
config_commands = ['int loop 1', 'ip address 2.2.2.2 255.255.255.255']
output =connect.send_config_set(config_commands)
print(output)
result = connect.send_command('show run int loop 1')
print(result)


