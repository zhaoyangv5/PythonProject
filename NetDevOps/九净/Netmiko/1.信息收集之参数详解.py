'''
netmiko的很多入门也以show命令演示为主，主要用到了netmiko的send_command方法与send_commnad_timing方法

send_command基于pattern的命令执行，
它是基于正则机制的，它执行命令后会持续收集回显，直至收到网络设备提示符，当前网络设备的提示符会由netmiko自动判定
所谓提示符是指每次我执行命令结束后设备停住的那行，等待我们下一条命令而显示的文本，一般是设备名与#]>等的组合，有时候是提示我们输入密码等等
netmiko会自动决定提示符，它会在登录结束后输入一个回车，回显是什么提示符就是什么，netmiko会整理成一个正则
'''
from netmiko import ConnectHandler

# dev = {'device_type': 'huawei',
#        'host': '192.168.31.100',
#        'username': 'python',
#        'password': 'Admin@123',
#        'port': 22}
#
# with ConnectHandler(**dev) as conn:
#     output = conn.send_command(command_string='display cu')
#     print(output)


'''
send_command_timing基于时间延迟的命令执行
它是一种基于延迟机制的方法。（一会我们会详解这种延迟机制）
它主要用于show命令。（实际在一些特殊的配置推送场景，它也会有奇效，前提是我们需要吃透这个方法和复杂场景的交互）
send_command_timing方法是基于时间延迟机制的，如果我们想适当扩大判断回显结束的停顿时间，只需在方法中给delay_factor（默认值为1）赋值即可，适当调整大一些
'''

# dev = {'device_type': 'huawei',
#        'host': '192.168.31.100',
#        'username': 'python',
#        'password': 'Admin@123',
#        'port': 22}
#
# with ConnectHandler(**dev) as conn:
#     output = conn.send_command_timing(command_string='display cu', delay_factor=2)
#     print(output)

'''send_command参数详解'''
#expect_string
#用于判断回显是否结束的正则表达式，如果不赋值或者传入为空，则由netmiko自动判断结束的提示符（含有设备名称的提示符）

# dev = {'device_type': 'huawei',
#        'host': '192.168.31.100',
#        'username': 'python',
#        'password': 'Admin@123',
#        'port': 22,
#        'session_log':'sw.log'}

# #当我们输入system-view时，新出的提示符是[~netdevops],这个时候netmiko一直在找之前提示符<netdevops>（实际是一个正则表达式），自然就会报错
# #通过在send_command方法中赋值expect_string，告诉netmiko我们希望用]来判定回显结束，这样这段代码就可以顺利执行
# with ConnectHandler(**dev) as conn:
#     output = conn.send_command(command_string='system-view', expect_string=r']')
#     print(output)

'''delay_factor'''
#延迟因子，默认值为1
#当fast_cli模式关闭（即其值为False）的时候，在具体执行时的延迟因子取global_delay_factor和delay_factor中的较大者。反之则取较小者
#在send_command方法中，我们如果希望程序速度提升，可以设置fast_cli为True，并在发送命令的方法中将此参数调整小一些

'''max_loops'''
#最大循环次数，默认值为500。它与delay_factor共同控制超时时间
#当方法中发现max_loops和delay_factor是默认值的时候，会根据刚才的逻辑计算出实际的max_loops。否则则使用用户传入的max_loops。这个值不建议大家修改

'''auto_find_prompt'''
#自动发现提示符，类型布尔值，默认值为True
#当用户调用send_command方法时，未传入expect_string的时候，netmiko会根据此参数决定是否自动发现提示符，其逻辑是发送一个回车到ssh隧道中，然后等待一段时间后从ssh隧道中读取设备发送的回显，普通情况下多为设备名称加一些特殊符号。
#如果用户传入了expect_string的时候，则此功能会自动取消

'''strip_prompt'''
#去除回显的设备提示符左右空白符，默认值为True。send_command方法中没有修改的意义，建议不修改此默认值

'''strip_command'''
#去除回显中发送命令行的左右空白符，默认值为True。send_command方法中没有修改的意义，建议不修改此默认值

'''normalize'''
#发送命令行规范标准化，默认值True。它用于确保每个命令行最右侧有一个换行符（简单理解为回车）

'''cmd_verify'''
#确认命令行回显，默认值为True
# dev = {'device_type': 'cisco_ios',
#        'host': '192.168.137.201',
#        'username': 'netdevops',
#        'password': 'admin123!',
#        'port': 22,
#        'session_log': 'netdevops.log'
#        }

#实际已经完成了交互，但是netmiko底层机制一直在等待我们输入的密码的回显，最终导致超时。我们只需要在输入密码的那行代码，把cmd_verify
# 赋值为False即
# with ConnectHandler(**dev) as conn:
#     output = conn.send_command(command_string='enable', expect_string='assword:')
#     print(output)
#     output = conn.send_command(command_string='admin1234!', expect_string='#', cmd_verify=False)
#     print(output)

'''textfsm、ttp、genie数据化输出'''
#netmiko安装时会自动安装textfsm与ntc-templates（一个内置了400个左右textfsm解析模板的库），
#如果内置有对指定命令回显的解析模板，则netmiko会自动将配置解析出结构化的数据（字典的列表），如果无解析模板则返回原始的回显文本（字符串）

'''send_command_timing参数详解'''
#参数解释同send_command


