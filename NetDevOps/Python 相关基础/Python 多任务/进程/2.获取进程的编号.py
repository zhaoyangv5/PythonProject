"""
获取进程编号的目的：
    获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由那个主进程创建出来的。

获取进程编号的两种操作：
    获取当前进程编号
    获取当前父进程编号

os.getpid() 表示获取当前进程编号
os.getppid() 表示获取当前父进程编号
"""
import multiprocessing
import time
import os


# 跳舞任务
def dance():
    # 获取当前进程的编号
    print("dance:", os.getpid())
    # 获取当前进程
    print("dance:", multiprocessing.current_process())
    # 获取父进程的编号
    print("dance的父进程编号:", os.getppid())
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)
        # 扩展:根据进程编号杀死指定进程
        # os.kill(os.getpid(), 9)


# 唱歌任务
def sing():
    # 获取当前进程的编号
    print("sing:", os.getpid())
    # 获取当前进程
    print("sing:", multiprocessing.current_process())
    # 获取父进程的编号
    print("sing的父进程编号:", os.getppid())
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)


if __name__ == '__main__':

    # 获取当前进程的编号
    print("main:", os.getpid())
    # 获取当前进程
    print("main:", multiprocessing.current_process())
    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None
    # target: 表示执行的目标任务名(函数名、方法名)
    # name: 进程名称, 默认是Process-1, .....
    dance_process = multiprocessing.Process(target=dance, name="myprocess1")
    sing_process = multiprocessing.Process(target=sing)

    # 启动子进程执行对应的任务
    dance_process.start()
    sing_process.start()