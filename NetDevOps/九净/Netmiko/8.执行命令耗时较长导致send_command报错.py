'''
在执行配置备份或者相关show信息的时候，经常会遇到程序报错：
OSError: Search pattern never detected in send_command: <netdevops>
在执行show信息的场景下出现pattern检测不到的，有两种情况，执行命令耗时较长，
当前用户无取消分页的权限，在此我们讨论执行命令回显时间耗时较长这种情况
'''

#调整执行命令超时时间的示例：
#只需要在设备连接信息中将timeout设置为比较大的值即可
import logging
from netmiko import ConnectHandler

logging.basicConfig(level=logging.DEBUG)

dev = {'device_type': 'huawei',
       'host': '192.168.31.100',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
        'timeout':180,
       'session_log': 'session.log',
       }

with ConnectHandler(**dev) as conn:
    output = conn.send_command('display version')
    print(output)