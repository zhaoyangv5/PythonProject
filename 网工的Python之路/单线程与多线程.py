#coding =utf-8

import threading
import time

# def say_after(what, delay):
#     print(what)
#     time.sleep(delay)
#     print(what)
#
# t = threading.Thread(target = say_after, args = ('hello', 3))       #target对应函数名，args对应函数参数
# print(f"程序于{time.strftime('%X')}开始执行")
# t.start()
# t.join()                #强制阻塞调用它的线程，直到该线程运行完毕或者终止（类似单线程同步）
# print(f"程序于{time.strftime('%X')}结束")

def say_after(what, delay):
    print(what)
    time.sleep(delay)
    print(what)
print(f"程序于{time.strftime('%X')} 开始执行\n")
threads = []

for i in range(1,6):
    t = threading.Thread(target=say_after, name="线程" + str(i), args=('hello',3))
    print(t.name + "开始执行.")
    t.start()
    threads.append(t)

for i in threads:
    i.join()
print(f"\n程序于{time.strftime('%X')}结束")

