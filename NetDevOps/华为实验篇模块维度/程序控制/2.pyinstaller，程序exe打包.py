"""
实验目的

（1）模块使用常规套路新，初识了解pyinstaller模块。

（2）做一个Python脚本，将其打包成exe，测试运行。

（3）将这个exe包放到其他人电脑上，测试运行。


"""
"""
pyinstaller打包语法
# 语法
pyinstaller [options] script [script …] | specfile
# 语法
pyinstaller [options] script

options带了中括号，表示可选。手册中罗列了一大箩筐选项值，我们结合“道听途说”消息，一般就用两个。

-D	单文件夹，默认。
-F	单文件。（一般我用这个）

相应系统只能打包相应系统的可执行程序，比如mac只能打包。app, windows只能打包。exe
"""

from ping3 import ping
from datetime import datetime


def fun_ping3(ih):
    # ih 表示ip或host
    result = ping(ih)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if result is None:
        print(ih + '  不通')
        with open('toping_result.txt', mode='a') as f:
            f.write(f'{now}   {ih},不通\n')

    elif result is False:
        print(ih + '  域名解析失败')
        with open('toping_result.txt', mode='a') as f:
            f.write(f'{now}   {ih},域名解析失败\n')

    else:
        print(ih + '  可达')
        with open('toping_result.txt', mode='a') as f:
            f.write(f'{now}   {ih},可达\n')


if __name__ == '__main__':
    # toping_list.txt存放IP地址或域名，一项一行。
    with open('toping_list.txt') as f:
        toping_list = f.readlines()

    with open('toping_result.txt', mode='a') as f:
        f.write('\n')

    for each in toping_list:
        fun_ping3(each.strip())

# pyinstaller -F lab_pyinstaller.py

