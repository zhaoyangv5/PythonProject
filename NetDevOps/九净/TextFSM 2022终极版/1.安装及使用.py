"""
一个极简的TextFSM解析模板parser.textfsm（解析模板一般后缀名为textfsm）

Huawei Versatile Routing Platform Software
VRP (R) software, Version 8.180 (CE6800 V200R005C10SPC607B607)
Copyright (C) 2012-2018 Huawei Technologies Co., Ltd.
HUAWEI CE6800 uptime is 100 day, 0 hour, 3 minutes


Value version (\S+)

Start
 ^VRP \(R\) software, Version ${version} -> Record
"""

from textfsm import TextFSM

if __name__ == '__main__':
    '''
    从textfsm导入TextFSM类，实例化的时候传入的是一个IO文件对象，不是字符串，这点一定要注意。
    实例化后，调用函数ParseTextToDicts，传入参数我们show出来的网络配置，即可解析出来字典的列表。
    '''
    with open('cli_output.log', 'r', encoding='utf8') as f:
        show_text = f.read()

    with open('parser.textfsm', encoding='utf8') as textfsm_file:
        template = TextFSM(textfsm_file)
        # datas = template.ParseText(show_text)             #[['8.180']]
        datas = template.ParseTextToDicts(show_text)    #[{'version': '8.180'}]
        print(datas)

#ParseTextToDicts此方法会返回一个字典的列表，这样一个字典就是一个record。如果本模板解析的是mac地址表，那一条mac记录就是一个字典，就是一个record
#textfsm模块的使用比较简单，只需要用解析模板构建TextFSM对象，然后调用ParseTextToDicts方法，传入要解析的网络配置（字符串）即可
#同时它也支持ParseText方法，将数据解析为二维列表（列表的列表），这样可以比较方便的输出到文本文件，形成csv
