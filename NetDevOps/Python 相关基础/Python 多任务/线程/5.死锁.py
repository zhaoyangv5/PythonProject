"""
死锁的概念：
    死锁: 一直等待对方释放锁的情景就是死锁
死锁的结果：
    会造成应用程序的停止响应，不能再处理其它任务了

小结：
    使用互斥锁的时候需要注意死锁的问题，要在合适的地方注意释放锁。
    死锁一旦产生就会造成应用程序的停止响应，应用程序无法再继续往下执行了。
"""

"""死锁示例"""
import threading
import time

# 创建互斥锁
lock = threading.Lock()


# 根据下标去取值， 保证同一时刻只能有一个线程去取值
def get_value(index):

    # 上锁
    lock.acquire()
    print(threading.current_thread())
    my_list = [3,6,8,1]
    # 判断下标释放越界
    if index >= len(my_list):
        print("下标越界:", index)
        return
    value = my_list[index]
    print(value)
    time.sleep(0.2)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 模拟大量线程去执行取值操作
    for i in range(30):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()


"""避免死锁"""
import threading
import time

# 创建互斥锁
lock = threading.Lock()


# 根据下标去取值， 保证同一时刻只能有一个线程去取值
def get_value(index):

    # 上锁
    lock.acquire()
    print(threading.current_thread())
    my_list = [3,6,8,1]
    if index >= len(my_list):
        print("下标越界:", index)
        # 当下标越界需要释放锁，让后面的线程还可以取值
        lock.release()
        return    # return 之后代表函数结束，后面代码就不会执行
    value = my_list[index]
    print(value)
    time.sleep(0.2)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 模拟大量线程去执行取值操作
    for i in range(30):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()