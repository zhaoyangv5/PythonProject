'''
直接发送配置send_config_set
send_config_set支持将配置通过ssh隧道按序发送到设备的功能，并且它会自动进入设备的config模式，配置发送完成，设备接收到之后，它还会自动退出config模式。
但是这个方法聚焦去配置的发送，如果涉及到配置的保存，需要调用另外一个方法save_config来进行，
使用save_config无需关注当前驱动的配置保存命令是什么，直接调用，netmiko会帮助我们自动输入对应平台的保存命令，并自动完成一部分交互
'''

from netmiko import ConnectHandler

# dev = {'device_type': 'huawei',
#        'host': '192.168.31.108',
#        'username': 'python',
#        'password': 'Admin@123',
#        'port': 22,
#        'session_log': '192.168.31.108.log'
#        }
#
# with ConnectHandler(**dev) as conn:
#     print("已经成功登陆交换机" + dev['host'])
#     # 如需提权 执行enable
#     # conn.enable()
#     # 将配置放到列表中，实际使用tuple等可以迭代的对象也可以
#     config_cmds = ['interface GE1/0/0','description cofiged by netmiko','commit']
#     # 调用send_config_set,赋值config_commands,返回整个交互过程的回显
#     config_output = conn.send_config_set(config_commands=config_cmds)
#     print('config_output:')
#     print(config_output)
#     # save_config,无需赋值，netmiko已经处理好它所支持的厂商型号的保存过程,返回整个交互过程的回显
#     save_output = conn.save_config()
#     print('save_output:')
#     print(save_output)

#对于某些需要提权的如enable的设备类型更改代码如下
dev = {'device_type': 'cisco_ios',
       'host': '192.168.31.110',
       'username': 'python',
       'password': 'Admin@123',
       'secret': 'Admin@123',
       'port': 22}

with ConnectHandler(**dev) as conn:
    print("已经成功登陆交换机" + dev['host'])
    # 如需提权 执行enable
    conn.enable()
    # 将配置放到列表中，实际使用tuple等可以迭代的对象也可以
    config_cmds = ['interface Gi0/0','description cofiged by netmiko']
    # 调用send_config_set,赋值config_commands,返回整个交互过程的回显
    config_output = conn.send_config_set(config_commands=config_cmds)
    print('config_output:')
    print(config_output)
    # save_config,无需赋值，netmiko已经处理好它所支持的厂商型号的保存过程,返回整个交互过程的回显
    save_output = conn.save_config()
    print('save_output:')
    print(save_output)

'''参数详解'''

# config_commands
#要推送给设备的配置，推荐使用列表或者元组。此参数也接受字符串，
#但是会被认为是一条命令，我们如果试图在字符串中自己添加换行，由于netmiko对回显的判断机制，这个方法实际是行不通的

# enter_config_mode
# 是否进入配置模式，默认值为True，这个config_mode方法中会有一个config_command的参数，各厂商的驱动都会重写此方法，赋值为其实际的进入配置模式的命令


#config_mode_command
#进入配置模式的命令，默认值为None。如果用户选择进入配置模式（参考enter_config_mode），一般各家驱动都会重写config_mode，内置了对应的进入配置模式的命令，
#所以在send_config_set中会有机制进行判断，如果用户传入的config_mode_command为None，
#则不会给config_mode的config_command赋值，从而使用驱动内置的config_command的默认值。此参数大家了解即可，一般已经适配的平台基本无需调整此参数的值

#exit_config_mode
#如果此参数为True，netmiko会调用exit_config_mode方法，退出配置模式

#error_pattern
#在回显中判断配置是否有错误的正则表达式。默认为空字符串，即认为错误命令判断机制不会生效，netmiko会逐行推送配置，无论每条命令是否成功
#如果根据各平台特性配置错误的正则表达式，则在输入配置命令行，回显中出错时，netmiko会自动停止配置下发，并抛出异常
# with ConnectHandler(**dev) as conn:
#     print("已经成功登陆交换机" + dev['host'])
#     # 如需提权 执行enable
#     conn.enable()
#     # 将配置放到列表中，实际使用tuple等可以迭代的对象也可以
#     config_cmds = ['interface Gi2/1','description cofiged by netmiko']  #输入一个不存在的端口
#     # 调用send_config_set,赋值config_commands,返回整个交互过程的回显
#     ## error_pattern进行赋值，注意取消转义
#     config_output = conn.send_config_set(config_commands=config_cmds, error_pattern=r"'\^'")
#     print('config_output:')
#     print(config_output)
#     # save_config,无需赋值，netmiko已经处理好它所支持的厂商型号的保存过程,返回整个交互过程的回显
#     save_output = conn.save_config()
#     print('save_output:')
#     print(save_output)

#delay_factor
#延迟因子，默认值为1。其基本原理与send_command一致，不建议调整，因为不同于show命令，配置的命令刷入设备时延小，回显快。此参数调整的意义并不是很大

# max_loops
# 同send_command最大循环次数，但是其默认值为150。原因同上

#strip_prompt
#去除回显的设备提示符左右空白符，默认值为False。可能是出于发送的配置要“原汁原味”，不容篡改的考虑，所以设置为了False。建议不修改此默认值

# strip_command
# 去除回显中发送命令行的左右空白符，默认值为False。s建议不修改此默认值。
#
# cmd_verify
# 确认命令行回显，默认值为True。原理同send_command，由于配置几乎都会回显，且确认回显可以保证设备接受到了配置命令，所以不建议修改默认值.



