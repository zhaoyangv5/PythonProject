"""
进程的概念
一个正在运行的程序或者软件就是一个进程，它是操作系统进行资源分配的基本单位，也就是说每启动一个进程，操作系统都会给其分配一定的运行资源(内存资源)保证进程的运行。

注意:
一个程序运行后至少有一个进程，一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程。

说明:
多进程可以完成多任务，每个进程就好比一家独立的公司，每个公司都各自在运营，每个进程也各自在运行，执行各自的任务
"""
"""
Process进程类的说明：
Process([group [, target [, name [, args [, kwargs]]]]])

group：指定进程组，目前只能使用None
target：执行的目标任务名
name：进程名字
args：以元组方式给执行任务传参
kwargs：以字典方式给执行任务传参

Process创建的实例对象的常用方法:
start()：启动子进程实例（创建子进程）
join()：等待子进程执行结束
terminate()：不管任务是否完成，立即终止子进程

Process创建的实例对象的常用属性:
name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
"""

import multiprocessing
import time

# 跳舞任务
def dance():
    for i in range(5):
        print("跳舞中....")
        time.sleep(0.2)

# 唱歌任务
def sing():
    for i in range(5):
        print("唱歌中....")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None
    # target: 表示执行的目标任务名(函数名、方法名)
    # name: 进程名称, 默认是Process-1, .....
    dance_process = multiprocessing.Process(target=dance, name='myprocess1')
    sing_process = multiprocessing.Process(target=sing)

    # 启动子进程执行对应任务
    dance_process.start()
    sing_process.start()