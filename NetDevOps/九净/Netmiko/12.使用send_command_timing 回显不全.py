'''
假如使用了send_command_timing经常会遇到配置不全的情况，产生这种问题有两种原因：

1.执行命令耗时较长，在timeout规定的时间窗口内未收集全配置，send_command_timing不再读取隧道中信息，强制退出，将已收集到的回显返回。
2.设备在传输回显的过程中，会稍微“卡顿”几秒，比如思科的设备在查看配置的时候，会在building configuration回显处卡住几秒。。
而这时，默认判断回显为空的时间间隔比较小（默认值是2秒），netmiko判定这个时间窗口内无数据回显，回显已经结束。

解决方案是:注意创建连接时的timeout，将其设置为一个稍微长点的合理值，同时在调用send_command_timing方法时，传入一个delay_factor参数，
将延迟因子适当调大，延迟因子默认为1，延迟基数是2秒，所以判断回显为空的默认时间为二者乘积2秒，我们每调大一下延迟因子，判定为空的时间窗口就会2秒的倍数级增加
'''

from netmiko import ConnectHandler

# 设备连接信息 timeout调大

dev = {'device_type': 'cisco_ios',
       'host': '192.168.31.110',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
       'timeout': 180,
       'session_log': 'netdevops.log'
       }

with ConnectHandler(**dev) as conn:
    # send_command_timing中调大延迟因子delay_factor（其默认值为1）
    output = conn.send_command_timing('display current-configuration', delay_factor=3)
    print(output)