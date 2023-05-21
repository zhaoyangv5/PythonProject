#netdev支持7加厂商12中操作系统，不是全部

import asyncio
import netdev
import time

async def task(dev):
    async with netdev.create(**dev) as ios:
        commands = ["line vty 5 15", "login local", "exit"]
        out = await ios.send_config_set(commands)
        print(out)

async def run():
    devices = []
    f = open('ip_list.txt')
    for ips in f.readlines():
        ip = ips.strip()
        dev = {
            'username': 'python',
            'password': '123',
            'device_type': 'cisco_ios',
            'host': ip
        }
        devices.append(dev)
    tasks = [task(dev) for dev in devices]
    await asyncio.wait(tasks)

start_time = time.time()
print(f"程序于{time.strftime('%X')} 开始执行）")
asyncio.run(run())
print(f"程序于{time.strftime('%X')} ）执行结束")