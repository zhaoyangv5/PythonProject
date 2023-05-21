'''
方法1：我们可以只调用write_channel与read_channel方法进行原始通信，发送命令接收回显，针对一些比较短的回显，比如show version，或者单行刷配置（刷配置的回显非常短），我们都可以直接按这种思路进行。

方法2：我们也可以把一些比较个性化的部分通过这两个方法执行，比如取消分页、提权等，之后的继续使用send_command或者send_config_set等方法即可。

方法3：我们调用write_channel与read_channel方法，再结合send_command的基本思路进行封装，针对日常的show命令和配置命令进行相关个性化编写。
'''

'''针对方法1，示例如下'''
# from netmiko import ConnectHandler
# import time
#
# dev = {'device_type': 'terminal_server',
#        'host': '192.168.31.111',
#        'username': 'python',
#        'password': 'Admin@123',
#        'secret': 'Admin@1234',
#        'port': 22,
#        'session_log': 'session.log'
#        }
# RETURN = '\n'
# with ConnectHandler(**dev) as conn:
#     # 通过通信隧道发送提权命令
#     conn.write_channel('show version{}'.format(RETURN))
#     # 让程序等待2秒，如果不停顿，直接读取隧道，隧道中可能还来不及接收任何数据
#     time.sleep(5)
#     output = conn.read_channel()
#     print(output)


'''
类似display current-configuration回显比较多的情况下，
上述代码可能存在回显不全的情况，我们可以按照send_command的思路进行一个循环读取并判断是否回显结束的逻辑
'''
from netmiko import ConnectHandler
import time
import re

dev = {'device_type': 'terminal_server',
       'host': '192.168.31.100',
       'username': 'python',
       'password': 'Admin@123',
       'secret': 'Admin@1234',
       'port': 22,
       'session_log': 'session.log'
       }

more_pattern = '  ---- More ----'
RETURN = '\n'
timeout = dev.get('timeout', 100)
loop_delay = 0.2
loops = timeout / loop_delay
i = 0
cmd = 'display version'
# 有些设备登录后会有提示修改密码的交互，才进入banner
# 我们可以修改配置关闭此类配置，也可以对其判断，输入否定选项
change_password_pattern = '[Y/N]:'

with ConnectHandler(**dev) as conn:
    # 模拟人工多输入几个回车，遇到一些修改密码的
    # 只有发送信息给网络设备，才能有新的回显
    conn.write_channel(RETURN)
    time.sleep(1)
    output = conn.read_channel()
    print(output)
    # 如果有提示密码修改的交互，则输入否（N）
    if change_password_pattern in output:
        conn.write_channel('N{}'.format(RETURN))
    time.sleep(1)
    output = conn.read_channel()
    # 在show情况下，最后一行就是提示符，作为回显结束的判断依据
    print(output.splitlines())
    prompt_pattern = output.splitlines()[-1]
    print('当前提示符为：{}'.format(prompt_pattern))
    # 重新初始化回显，置空
    output = ''
    # 通过通信隧道发送提权命令
    conn.write_channel('{}{}'.format(cmd, RETURN))

    while i <= loops:
        # 读取隧道中的信息，放入chunk_output
        chunk_output = conn.read_channel()
        # 判断是否有分页交互提示
        if more_pattern in chunk_output:
            # 回显中的分页提示去除
            chunk_output = chunk_output.replace(more_pattern, '')
            # 拼接回显
            output += chunk_output
            # 发送回车换行符
            conn.write_channel(RETURN)
        # 根据提示符判断是否回显结束
        elif re.search(prompt_pattern, chunk_output):
            # 拼接回显 并跳出循环
            output += chunk_output
            break
        # 停顿loop_delay秒
        time.sleep(loop_delay)
        # 计数器i加一 类似其他语言中的i++
        i += 1
        # 如果超过了，则证明超时，我们可以自己抛出异常
    if i > loops:
        raise Exception('执行命令"{}"超时'.format(cmd))
    print(output)
