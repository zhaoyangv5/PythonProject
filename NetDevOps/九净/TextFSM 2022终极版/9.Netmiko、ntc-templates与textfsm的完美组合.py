"""
ntc-templates也给了我们一些定制化的方法，让我们可以在ntc-templates的基础上，把自己的一些模板加入。

我们要做的是三件事情：

将ntc-templates的解析库（包含TextFsm解析模板和index索引文件）拷贝到某目录
将此目录的路径加入到环境变量“NTC_TEMPLATES_DIR”中去。
添加自己的解析模板，追加相应规则到index文件中，形如“{解析模板名称}, .*, {设备的平台}, {执行的命令}”，其中命令可以参考已有的，用“[[]]”包起可能被省略掉的字母。
"""
# import os
# os.environ['NTC_TEMPLATES_DIR'] = '/path/to/new/templates/location/templates'

import os
from netmiko import ConnectHandler, Netmiko

os.environ['NET_TEXTFSM'] = r'C:\Pythons\python3.9.5\lib\site-packages\ntc_templates\templates'

if __name__ == '__main__':
    device = {
        'device_type': 'cisco_nxos',
        'host': '192.168.137.203',
        'username': 'admin',
        'password': 'admin123!',
        'port': 22,
        'conn_timeout': 20,
        'timeout': 120,
    }
    with ConnectHandler(**device) as net_conn:
        data = net_conn.send_command('show version', use_textfsm=True)
        if isinstance(data, list):
            print('解析成功，数据如下:{}'.format(data))
        else:
            print('解析失败，配置如下:{}'.format(data))
