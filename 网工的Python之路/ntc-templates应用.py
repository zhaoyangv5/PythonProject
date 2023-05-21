from netmiko import ConnectHandler
import json

"""
因为Netmiko是用NET——TEXTFSM条用ntc_template，所以需要提前设备环境变量
将ntc_template模板集完整路径赋值给变量net_textfsm
export NET_TEXTFSM='/ntc-template/ntc-templates/templates'
echo $NET_TEXTFSM
"""


# sw1 = {
#     'device_type': 'cisco_ios',
#     'ip': '192.168.2.1',
#     'username': 'python',
#     'password': '123'
# }
#
# connect = ConnectHandler(**sw1)
# print('sucess connect to ' + sw1['ip'])
# intfaces = connect.send_command('show ip int brief', use_textfsm=True)
# print(json.dumps(intfaces, indent=2))

SW1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.11',
    'username': 'python',
    'password': '123',
}

connect = ConnectHandler(**SW1)
print ("Sucessfully connected to " + SW1['ip'])
interfaces = connect.send_command('show ip int brief', use_textfsm=True)
for interface in interfaces:          #netmiko调用textfsm后send_command返回值是列表，所以可以循环遍历
    if interface["status"] == 'up':
        print (f'{interface["intf"]} is up!  IP address: {interface["ipaddr"]}')