"""
互斥锁的概念：
    互斥锁: 对共享数据进行锁定，保证同一时刻只能有一个线程去操作。
互斥锁的使用：
    threading模块中定义了Lock变量，这个变量本质上是一个函数，通过调用这个函数可以获取一把互斥锁。

小结:
    互斥锁的作用就是保证同一时刻只能有一个线程去操作共享数据，保证共享数据不会出现错误问题
    使用互斥锁的好处确保某段关键代码只能由一个线程从头到尾完整地去执行
    使用互斥锁会影响代码的执行效率，多任务改成了单任务执行
    互斥锁如果没有使用好容易出现死锁的情况

互斥锁使用步骤:
# 创建锁
mutex = threading.Lock()
# 上锁
mutex.acquire()
...这里编写代码能保证同一时刻只能有一个线程去操作, 对共享数据进行锁定...
# 释放锁
mutex.release()

注意点:
    acquire和release方法之间的代码同一时刻只能有一个线程去操作
    如果在调用acquire方法的时候 其他线程已经使用了这个互斥锁，那么此时acquire方法会堵塞，直到这个互斥锁释放后才能再次上锁。
"""
import threading


# 定义全局变量
g_num = 0

# 创建全局互斥锁
lock = threading.Lock()

# 循环一次给全局变量加1
def sum_num1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("sum1:", g_num)
    # 释放锁
    lock.release()


# 循环一次给全局变量加1
def sum_num2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print("sum2:", g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)
    # 启动线程
    first_thread.start()
    second_thread.start()

    # 提示：加上互斥锁，那个线程抢到这个锁我们决定不了，那线程抢到锁那个线程先执行，没有抢到的线程需要等待
    # 加上互斥锁多任务瞬间变成单任务，性能会下降，也就是说同一时刻只能有一个线程去执行