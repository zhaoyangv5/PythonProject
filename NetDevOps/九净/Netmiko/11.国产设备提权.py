'''
我们可以通过send_command方法即可，注意调整expect_string和cmd_verify
'''

from netmiko import ConnectHandler

dev = {'device_type': 'cisco_ios',
       'host': '192.168.31.110',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
       'session_log': 'netdevops.log'
       }

with ConnectHandler(**dev) as conn:
    output = conn.send_command(command_string='enable', expect_string='assword:')
    print(output)
    output = conn.send_command(command_string='Admin@123', expect_string='#')
    print(output)


#使用write_channel和read_channel来给大家实现一遍

from netmiko import ConnectHandler
import time

dev = {'device_type': 'cisco_ios',
       'host': '192.168.31.110',
       'username': 'python',
       'password': 'Admin@123',
       'secret': 'Admin@123',
       'port': 22,
       'session_log': 'netdevops.log'
       }
# 提权的命令
enable_cmd = 'enable'
# 提权时输入密码的标识
password_pattern = 'assword'
# 提权成功后的标识
enable_success_pattern = '#'

with ConnectHandler(**dev) as conn:
    # 通过通信隧道发送提权命令
    conn.write_channel('{}{}'.format(enable_cmd, conn.RETURN))
    # 让程序等待2秒，如果不停顿，直接读取隧道，隧道中可能还来不及接收任何数据
    time.sleep(2)
    # 停顿2秒后读取数据
    output = conn.read_channel()
    # 确认回显中有输入密码的提示
    if password_pattern not in output:
        raise Exception('请确认输入的提权命令正确，未发现输入密码的提示')
    # 输入密码
    conn.write_channel('{}{}'.format(dev['secret'], conn.RETURN))
    # 停顿并读取数据
    time.sleep(2)
    output = conn.read_channel()
    # 根据回显判断判断是否成功
    if enable_success_pattern in output:
        print('提权成功')
    elif password_pattern not in output:
        raise Exception('提权密码错误，请确认相关信息')
    else:
        raise Exception('发生未知错误，提权失败')
