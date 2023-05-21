'''
我们如何提取保存指令回显信息呢？Nornir_utils.plugins.taks.files中调用write_file插件可以来帮忙。没错，我们可以把它当成一个数据采集利器

实验目的

（1）使用nornir_napalm插件（需配合napalm-huawei-vrp）指令采集网元配置，并保存至本地目录。

（2）使用nornir_napalm插件（需配合napalm-huawei-vrp）指令采集网元端口，并保存至本地目录。
'''

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date


#配置保存
def backup_configurations(task1):
    r = task1.run(task=napalm_get, getters=["config"])
    task1.run(task=write_file, content=r.result["config"]["running"],
              filename= str(task1.host.name) + "-" + str(date.today()) + ".txt")


#端口采集
def backup_getports(task2):
    r = task2.run(task=napalm_get, getters=["facts"])
    # task2.run(task=write_file, content=r.result["facts"]["interface_list"],
    #           filename=str(task2.host.name) + "-ports-" + str(date.today()) + ".txt")
    task2.run(task=write_file, content='\n'.join(r.result["facts"]["interface_list"]),
              filename=str(task2.host.name)  + "-ports-" + str(date.today()) + ".txt")


nr = InitNornir(config_file="nornir.yaml")
result = nr.run(name="正在备份交换机配置", task=backup_configurations)
result2 = nr.run(name="正在采集交换机端口列表", task=backup_getports)
print_result(result)
print_result(result2)

