"""
Process类执行任务并给任务传参数有两种方式:
    args 表示以元组的方式给执行任务传参
    kwargs 表示以字典方式给执行任务传参
元组方式传参(args): 元组方式传参一定要和参数的顺序保持一致。
字典方式传参(kwargs): 字典方式传参字典中的key一定要和参数名保持一致。
"""

# args参数的使用
import multiprocessing
import time


# 带有参数的任务
def task1(count):
    for i in range(count):
        print("任务1执行中..")
        time.sleep(0.2)


def task2(count):
    for i in range(count):
        print("任务2执行中..")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    # args: 以元组的方式给任务传入参数
    sub_process1 = multiprocessing.Process(target=task1, args=(5,))
    # kwargs: 表示以字典方式传入参数
    sub_process2 = multiprocessing.Process(target=task2, kwargs={'count': 3})

    sub_process1.start()
    sub_process2.start()
