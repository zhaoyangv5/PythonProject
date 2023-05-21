"""
Thread类执行任务并给任务传参数有两种方式:
    args 表示以元组的方式给执行任务传参
    kwargs 表示以字典方式给执行任务传参
线程执行任务并传参有两种方式:
    元组方式传参(args) ：元组方式传参一定要和参数的顺序保持一致。
    字典方式传参(kwargs)：字典方式传参字典中的key一定要和参数名保持一致。
"""

"""args参数的使用"""
import threading
import time


# 带有参数的任务
def task(count):
    for i in range(count):
        print("任务执行中..")
        time.sleep(0.2)
    else:
        print("任务执行完成")


if __name__ == '__main__':
    # 创建子线程
    # args: 以元组的方式给任务传入参数
    sub_thread = threading.Thread(target=task, args=(5,))
    sub_thread.start()


"""kwargs参数的使用"""
# 带有参数的任务
def task(count):
    for i in range(count):
        print("任务执行中..")
        time.sleep(0.2)
    else:
        print("任务执行完成")


if __name__ == '__main__':
    # 创建子线程
    # kwargs: 表示以字典方式传入参数
    sub_thread = threading.Thread(target=task, kwargs={"count": 3})
    sub_thread.start()



