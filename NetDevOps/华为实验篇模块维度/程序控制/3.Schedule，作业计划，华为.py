"""
实验目的

（1）学习schedule模块的常规使用。

（2）Schedule+ping3，定制ping任务。

（3）Schedule+paramiko，对设备进行实时部分参数的监控。

"""
"""
# 每隔啥做啥，task是具体任务，通常为函数形式，可定义。
schedule.every(interval=1).(seconds,minutes,hours,days).do(task)

# 具体示例
schedule.every(10).seconds.do(task)
schedule.every(10).minutes.do(task)
schedule.every().hour.do(task)
schedule.every().day.at("10:30").do(task)
schedule.every(5).to(10).minutes.do(task)
schedule.every().monday.do(task)
schedule.every().wednesday.at("13:15").do(task)
schedule.every().minute.at(":17").do(task)

另一处是：

schedule.run_pending()
任务放入schedule并不会马上执行起来，而是进入pending状态，由函数run_pending()来启动执行。

"""

import schedule
from datetime import datetime


"""示例一（打印时间）"""

# def job():
#     now = datetime.now()
#     time = now.strftime("%H:%M:%S")
#     print (f'现在的时间是: {time}')
#
# schedule.every(3).seconds.do(job)       #每三秒就调用一次函数job()，一调用就进入pending状态
#
# while True:
#     schedule.run_pending()              #schedule.run_pending()在while中，永远执行


""" 示例二（ping）"""

import schedule
from datetime import datetime
from ping3 import verbose_ping

def job_ping3():
    time = datetime.now().strftime("%H:%M:%S")  # 如果不是很清晰，则还是分开写程序的可读性好些。
    print (f'\n现在的时间是: {time}')
    verbose_ping('huawei.com')

schedule.every(5).seconds.do(job_ping3)

while True:
    schedule.run_pending()


"""示例三（监控设备性能）"""

from datetime import datetime
import paramiko
import time

def job_paramiko():
    nowtime = datetime.now().strftime("%H:%M:%S")
    print (f'\n现在的时间是: {nowtime}')   # 【注意】import了time模块，这里必须改一下，不然会冲突。

    ip = "172.25.1.234"
    username = "*********"   # 根据实际用户名
    password = "*********"   # 根据实际密码

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
    print("Successfully connected to ",ip)

    command = ssh_client.invoke_shell()
    command.send("screen-length 0 temporary\n")
    command.send("display temperature all\n")
    time.sleep(1)

    output = command.recv(65535).decode("ascii")
    print(output.split('\n')[-3])   # 可以先把索引[-3]去掉，看看要取哪一项。

    ssh_client.close()

schedule.every(3).seconds.do(job_paramiko)

while True:
    schedule.run_pending()