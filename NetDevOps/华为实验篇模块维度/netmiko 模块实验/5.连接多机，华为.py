'''
实验背景

现网如果只有一台设备，那我们还讨论啥运维自动化哈？咱们把整台设备的配置文件都背下来就行了。事实上，稍微大一点的企业，网络设备量都是几百上千的。前面的实验，我们都是通过netmiko登录1台设备，这次我们来用netmiko模块操作多台设备，顺便串一下以前paramiko模块实验中用到的“循环遍历、读取文件、异常处理”等，当做温故而知新吧。

实验目的

（1）用netmiko登录各台Layer3Switch，执行display cur | inc sysname命令，抓取回显。

（2）用netmiko处理“网络不通”，“认证失败”2个模拟场景
'''
import netmiko
from netmiko import ConnectHandler

# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放网络不通的设备信息
switch_not_reachable = []

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
            with ConnectHandler(**connection_info) as conn:
                print(f'已经成功登陆交换机{ip}')
                output = conn.send_command('display cur | inc sysname')
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