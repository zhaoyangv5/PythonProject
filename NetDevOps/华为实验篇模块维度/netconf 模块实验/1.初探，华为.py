"""
实验目的

在CE12800华为交换机探索NETCONF功能，实验环境搭建。
使用Python的ncclient模块进行设备简单联动。

手册中NETCONF的内容其实还是挺多的，以下我做点与本次实验相关的概括与摘抄。

角色关系
NETCONF Manager
NETCONF Manager担任网络中的Client，利用NETCONF协议对网络设备进行系统管理。
NETCONF Agent
NETCONF Agent担任网络中的Server。
在我们的拓扑中，PC是Client，而CE1是Server。如果你有点现网运维经验，这个有时候会有点绕，因为我们往往说“网管服务器”，但这个“网管服务器”在NETCONF世界里实际扮演者客户端的角色。

建模语言
Schema（本次实验暂时探讨这个）
Schema是为了描述XML文档而定义的一套规则。Schema文件中定义了设备所有管理对象，以及管理对象的层次关系、读写属性和约束条件。设备通过Schema文件向网管提供配置和管理设备的接口。Schema文件类似于SNMP的MIB文件。
YANG
YANG是专门为NETCONF协议设计的数据建模语言，用来为NETCONF协议设计可操作的配置数据、状态数据模型、远程调用（RPCs）模型和通知机制等。YANG数据模型为一个面向机器的模型接口，明确定义数据结构及其约束，可以更灵活、更完整的进行数据描述。
"""

from ncclient import manager

host = '192.168.31.100'
port = '830'
user = 'netconf'
password = 'Admin@1234'

def huawei_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify = False,
                           device_params={'name': "huawei"},
                           allow_agent = False,
                           look_for_keys = False)

m = huawei_connect(host=host, port=port, user=user, password=password)


FILTER = ''' <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
<interfaces>
<interface>
<ifName/>
</interface>
</interfaces>
</ifm>'''

# get_reply1 或 get_reply2 选一个就好！
get_reply1 = m.get(("subtree", FILTER))
#get_reply2 = m.get_config(source='running',filter=("subtree",FILTER))

print(get_reply1)
#m.close  # 不用上下文 with 管理器的话，我们最后close一下。


