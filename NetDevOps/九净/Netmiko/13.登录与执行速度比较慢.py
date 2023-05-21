'''
netmiko和设备交互，都是通过write_channel写入命令到通信隧道中，然后以某种频率去隧道中循环读取数据。所以在网络条件恒定的前提之下，适当调小停顿等待时间，进而调高隧道中读取的频率，可以让回显尽早收集齐，完成相关操作的确认。而提高整个频率就是靠延迟因子的调整，我们之前讲解的延迟因子很多都是方法内部的延迟因子，实际上netmiko的延迟因子不是只有这一个，或者说，这个延迟因子只是局部延迟因子（大部分局部的延迟因子默认值都是1），还有一个隐藏的全局延迟因子。只要是和设备有相关命令行交互的方法，大都会有delay_factor这个参数。但是并不是由这个局部延迟因子单独决定最终的实际延迟因子进而控制频率的，netmiko有一套比较灵活的延迟因子选举机制：

在初始化连接的时候，有一个全局延迟因子global_delay_factor（默认值为1）和fast_cli模式（默认值为False）。

当不开启fast_cli模式的时候，netmiko在各个方法内选择局部延迟因子delay_factor和全局延迟因子global_delay_factor中的较大者。所以我们单纯调整任何一个延迟因子不得其法可能都不会有效果。

当开启fast_cli模式的时候，netmiko会认为用户需要优化读取数据的性能，需要提高读取信息的频率，这时它会选择局部延迟因子delay_factor和全局延迟因子global_delay_factor中的较小者。

以上行为是netmiko内部的select_delay_factor方法的基本逻辑，各个方法执行的时候基本都先调用此方法来判定最终的延迟因子，比如取消分页的时候，在取消分页方法内部调用select_delay_factor方法，大多数设备给其赋值局部延迟因子是1，这个时候我们单纯调整全局的延迟因子，并不会提高效率。

为了调高读取隧道信息中的频率，我们调小程序停顿等待的时间，调小延迟因子是我们的“出路”。结合上面的逻辑，为了提高登录速度，fast_cli调整为True，开启快速模式，全局延迟因子global_delay_factor调小，比如笔者设置为0.1。有些设备不调整参数，使用默认值，笔者的模拟器设备华为CE交换机登录耗时大约8秒甚至更久，但是调整上面的参数后，时间可以缩短到一秒。
'''

from netmiko import ConnectHandler
import time
# 设备连接信息 开启fast_cli快速模式，全局global_delay_factor延迟因子调小（默认值为1）
dev = {'device_type': 'huawei',
       'host': '192.168.31.100',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
       'timeout': 180,
       'fast_cli':True,
       'global_delay_factor':0.01,
       'session_log': 'session.log',
       }
print(time.time())
with ConnectHandler(**dev) as conn:
       print(time.time())
       print(conn.is_alive())