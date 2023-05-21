'''
实验目的

（1）利用Jinja2模板，制作Layer3Switch-1的vty登录限制脚本，用ACL方式。

（2）用netmiko登录Layer3Switch-1（192.168.11.11），执行（1）脚本并回显。

（3）实验目的效果预期：

可登录Layer3Switch-1
PC电脑WIN10（192.168.31.243）
Layer3Switch-2（192.168.31.101）
不可登录Layer3Switch-1
Layer3Switch-3（192.168.11.13）
Layer3Switch-4（192.168.11.14）
（4）Layer3Switch-5（192.168.11.15），无相关配置，看一下什么效果
'''

import netmiko
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

# allow_ip = ['192.168.31.243', '192.168.31.101']
# disallow_ip = ['192.168.31.102', '192.168.31.108']
#
# sw1 = {'device_type':'huawei_vrpv8',
#       'ip':'192.168.31.100',
#       'username':'python',
#       'password':'Admin@123'}
#
# loader = FileSystemLoader('./template')
# environment = Environment(loader=loader)
# tpl = environment.get_template('acl.conf.tpl')
# out = tpl.render(allow_ip=allow_ip, disallow_ip=disallow_ip, interface='vty 0 4')
#
# with open("configuration.conf", "w") as f:
#        f.write(out)
#
# with ConnectHandler(**sw1) as conn:
#         print ("已经成功登陆交换机" + sw1['ip'])
#         output = conn.send_config_from_file("configuration.conf")
#         print (output)


#扩展：多机登录写acl

# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放网络不通的设备信息
switch_not_reachable = []

allow_ip = ['10.1.1.1', '11.1.1.1']
disallow_ip = ['100.1.1.1', '99.1.1.1']

loader = FileSystemLoader('./template')
environment = Environment(loader=loader)
tpl = environment.get_template('acl.conf.tpl')

with open('ip_list.txt') as f:
    for ips in f.readlines():
        try:
            ip = ips.strip()
            connection_info = {
                'device_type': 'huawei_vrpv8',
                'ip': ip,
                'username': 'python',
                'password': 'Admin@123',
                # 'conn_timeout':10
            }
            out = tpl.render(allow_ip=allow_ip, disallow_ip=disallow_ip, interface='vty 0 4')

            with open("configuration.conf", "w") as f1:
                f1.write(out)

            with ConnectHandler(**connection_info) as conn:
                print("已经成功登陆交换机" + connection_info['ip'])
                output = conn.send_config_from_file("configuration.conf")
                print(output)

        except netmiko.NetmikoAuthenticationException:
            print(ip + "用户验证失败！")
            switch_with_authentication_issue.append(ip)

        except netmiko.exceptions.NetmikoTimeoutException:
            print(ip + "目标不可达！")
            switch_not_reachable.append(ip)

print('\n ====结果输出====')
print('·下列交换机用户验证失败：')
for i in switch_with_authentication_issue:
    print(f"  {i}")

print('·下列交换机不可达：')
for i in switch_not_reachable:
    print(f"  {i}")