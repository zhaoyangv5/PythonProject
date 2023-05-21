

#同步和异步都是在单线程下的概念

import asyncio
import time

# async def main():
#     print('hello')
#     await asyncio.sleep(1)
#     print('word')
#
# print(f"程序于{time.strftime('%X')} 开始执行）")
# asyncio.run(main())
# print(f"程序于{time.strftime('%X')} ）执行结束")


#多函数的同步
# async def say_after(what, delay):
#     print(what)
#     await asyncio.sleep(delay)
#
# async def main():
#     print(f"程序于{time.strftime('%X')} ）执行结束")
#     await say_after('hello',1)
#     await say_after('world',2)
#     print(f"程序于{time.strftime('%X')} ）执行结束")
#
# asyncio.run(main())

async def say_after(what, delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after('hello', 1))
    task2 = asyncio.create_task(say_after('world',2))
    print (f"程序于{time.strftime('%X')} 开始执行）")
    await task1
    await task2
    print (f"程序于{time.strftime('%X')} ）执行结束")
asyncio.run(main())