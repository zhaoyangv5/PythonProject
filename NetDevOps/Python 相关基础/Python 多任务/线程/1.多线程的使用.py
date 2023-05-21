"""
线程的概念：
    线程是进程中执行代码的一个分支，每个执行分支（线程）要想工作执行代码需要cpu进行调度 ，也就是说线程是cpu调度的基本单位，
    每个进程至少都有一个线程，而这个线程就是我们通常说的主线程。

线程是Python程序中实现多任务的另外一种方式，线程的执行需要cpu调度来完成。
"""

"""
线程类Thread参数说明：
    Thread([group [, target [, name [, args [, kwargs]]]]])
    group: 线程组，目前只能使用None
    target: 执行的目标任务名
    args: 以元组的方式给执行任务传参
    kwargs: 以字典方式给执行任务传参
    name: 线程名，一般不用设置

启动线程：
    启动线程使用start方法
"""
import threading
import time

# 唱歌任务
def sing():
    # 扩展： 获取当前线程
    # print("sing当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)

# 跳舞任务
def dance():
    # 扩展： 获取当前线程
    # print("dance当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)


if __name__ == '__main__':
    # 扩展： 获取当前线程
    # print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌的线程
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing)

    # 创建跳舞的线程
    dance_thread = threading.Thread(target=dance)

    # 开启线程
    sing_thread.start()
    dance_thread.start()
