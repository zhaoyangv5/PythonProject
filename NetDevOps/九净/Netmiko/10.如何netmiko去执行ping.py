'''
我们在日常运维的时候，经常会有一些ping的检查，大家使用netmiko去做ping检查的时候，假如ping的包数比较多，包比较大，耗时比较长，会导致超时。
即使不超时，由于netmiko的send_command机制，它直到回显全部返回才结束，而我们可能希望实时了解ping的情况。
这种ping操作的场景，对时间和这种实时性有要求的时候，我们就可以尝试使用write_channel与read_channel，
通过write_channel发送了ping的命令后，通过read_channel循环读取隧道中信息，实时将回显输出到某个地方，
可以是直接标准输出到终端，也可以是写入某种MQ（消息队列），也可以是某种数据库（比如redis内存数据库或者传统的数据库）。同时可以自己加一些参数来控制超时时间等
'''

import time

from netmiko import ConnectHandler

dev = {'device_type': 'huawei',
       'host': '192.168.31.100',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
       'session_log': 'session.log'
       }

# 执行ping的相关变量
dest_ip = '192.168.31.1'
count = '100'
ping_cmd = 'ping -c {} {}'.format(count, dest_ip)
# 判断回显结束的标识
end_pattern = '>'
# 用于循环的相关变量
loop_delay = 0.2
timeout = 60
loops = timeout / loop_delay
i = 0
# 存放ping结果
ping_result = ''

with ConnectHandler(**dev) as conn:
    # 发送ping命令
    conn.write_channel('{}{}'.format(ping_cmd, conn.RETURN))
    while i <= loops:
        output = conn.read_channel()
        if output:
            # 此处我们进行打印，实际各个厂商的设备，
            # ping的成功与否都会有对应符号特征，我们可以对一些情况就行计算或者解析实时输出到某处
            print(output)
            ping_result = ping_result + output
        time.sleep(loop_delay)
        i = i + 1
        if end_pattern in output:
            break
if i > loops:
    raise Exception('ping超时')

print('ping 结果为：{}'.format(ping_result))