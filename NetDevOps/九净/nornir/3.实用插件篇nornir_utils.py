"""
write_file

结合笔者的实际使用情况，我比较推荐其处理文件的task函数——write_file。使用它，我们可以非常便捷的将文本内容写入文件。

参数Arguments部分，它有三个核心参数（我们选择无视dry_run）：

filename，我们要写入文本内容的文件路径。
content，我们想写入的文本内容。
append，是否为追加模式，默认是False，即如果源文件存在，则每次会覆盖其内容。

这个task函数的返回值则可以看Returns部分，从函数的return代码中我们也可以观察到，它主要包含了两个属性：

diff，文本差异部分，是Linux的diff差异风格。
changed，本次写入内容与之前文件中的文本内容是否发生变化。
"""
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir.core.task import Result, Task


def write_file_for_single_dev(task_context: Task):
    file_name = '{}.txt'.format(task_context.host.hostname)
    content = 'Hello World, dda'
    multi_results = task_context.run(write_file,filename=file_name,content=content)
    # 返回所有子任务中的第一个即write_file函数运行结果，Result对象
    # print(multi_results)     #MultiResult: [Result: "write_file"]
    return multi_results[0]

# nr = InitNornir(config_file="nornir.yaml")
# results = nr.run(task=write_file_for_single_dev)
# print_result(results)


"""
tcp_ping

tcp_ping实现了对指定ip和端口的一个tcp探测，用于网络设备的发现或者测试。
结合笔者的认知而言，建议用于探测指定Host对象的指定端口是否对我们的脚本所部署的主机开通。
假如我们是通过CMDB获取的网络设备，可以通过这个task函数来判断我们的主机是否与网络设备可达（用于测试22、830这些指定协议的端口）。
其路径为nornir_utils.plugins.tasks.networking.tcp_ping


ports，类型为整数的列表，是要ping的tcp端口。
timeout，ping探测的超时时间，默认为2秒，类型是整数，可选参数。
host，我们要ping探测的主机，默认是当前网络设备Host对象，可选参数。
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.networking import tcp_ping

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=tcp_ping, ports=[22, 830])
print_result(results)