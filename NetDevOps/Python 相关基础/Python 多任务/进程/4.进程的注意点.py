# -*- coding: UTF-8 -*-

"""
进程的注意点介绍
    进程之间不共享全局变量
    主进程会等待所有的子进程执行结束再结束

进程之间不共享全局变量的小结:
    创建子进程会对主进程资源进行拷贝，也就是说子进程是主进程的一个副本，好比是一对双胞胎，
    之所以进程之间不共享全局变量，是因为操作的不是同一个进程里面的全局变量，只不过不同进程里面的全局变量名字相同而已。

主进程会等待所有的子进程执行结束再结束的小结:
    为了保证子进程能够正常的运行，主进程会等所有的子进程执行完成以后再销毁，设置守护主进程的目的是主进程退出子进程销毁，不让主进程再等待子进程去执行。
    设置守护主进程方式： 子进程对象.daemon = True
    销毁子进程方式： 子进程对象.terminate()
"""

import multiprocessing
import time

"""进程之间不共享全局变量"""

# 定义全局变量
g_list = ['主进程数据']

# 添加数据任务
def add_data():
    for i in range(5):
        # 因为列表是可变类型，可以在原有的内存的基础上修改数据，并且修改后内存地址不变，所以不需要加上global关键字
        # 加上global 表示声明要修改全局变量的内存地址
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("添加完成", g_list)

# 读取数据任务
def read_data():
    print('read:', g_list)

if __name__ == '__main__':
    # 添加数据的子进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    # 当前进程等待添加数据的进程执行完成以后在继续往下执行
    add_process.join()
    read_process.start()

    print("main", g_list)

# 对于Linux和Mac主进程执行的代码不会进程拷贝，但是对于windows系统来说主进程执行的代码也会进行拷贝执行
# 对于Windows来说创建子进程的代码如果进程拷贝执行相当于递归无限制进行创建子进程，会报错
# 解决Windows递归创建子进程，通过判断是否是主模块来解决


"""主进程会等待所有的子进程执行结束再结束"""

def task():
    for i in range(10):
        print(f'任务执行中...{i}')
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 方式1：把子进程设置成为守护主进程，以后主进程退出子进程直接销毁
    # sub_process.daemon = True
    sub_process.start()
    time.sleep(0.5)    # 这个时间差，主进程会等待子进程执行完成后程序在退出
    print('over')

    # 退出主进程前，先让让子进程销毁
    sub_process.terminate()
