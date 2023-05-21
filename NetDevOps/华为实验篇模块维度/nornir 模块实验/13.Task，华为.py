'''
1、Task是我们定义要完成的任务动作，被封装为自定义函数。

2、上述这个自定义函数，调用是需要借助<class 'nornir.core.Nornir'>.run()这个函数。

3、<class 'nornir.core.Nornir'>就是网络设备类，如果比如初始化nr = InitNornir(config_file='config.yaml')，那nr就是对象，我们随即写为nr.run(task=xxx)。
'''

'''
实验目的

实验12中，我们已经通过Nornir的inventory插件，获取hosts.yaml中保存的设备信息，
如交换机SW1对应的name, hostname，username，password，platform，groups，data等。那么，这次我们用Task仿照inventory来获取这些。
'''

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result

nr = InitNornir(config_file='nornir.yaml')

print(type(nr))

#关这个叫“上下文”的task_wgsy还解释得挺累的，它其实作为Task函数的第一个参数，就是固定是所谓的“上下文”了吧。
#然后我们把它命名为task_wgsy，此后在自定义Task函数内部可以召唤它！
def host_parm(task_wgsy:Task) -> Result:   #名为host_parm类型为Task的函数，整个函数就是一个Task对象，返回结果为Result对象，
                                           # Task和Result只是限定标注类型（即告诉你函数是什么对象，其结果是什么对象，说白了就是“注释”！）而已
    return (task_wgsy.host.name,
            task_wgsy.host.hostname,
            task_wgsy.host.username,
            task_wgsy.host.password,
            task_wgsy.host.platform,
            task_wgsy.host.groups,
            task_wgsy.host.data)

#写成这样也可以
# def host_parm(task_wgsy):
#     return (task_wgsy.host.name,
#         task_wgsy.host.hostname,
#         task_wgsy.host.username,
#         task_wgsy.host.password,
#         task_wgsy.host.platform,
#         task_wgsy.host.groups,
#         task_wgsy.host.data)


result = nr.run(task=host_parm)
print_result(result)
