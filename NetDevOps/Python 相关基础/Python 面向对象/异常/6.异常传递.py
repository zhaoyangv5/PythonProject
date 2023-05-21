# -*- coding: UTF-8 -*-

import time

# 尝试只读打开test.txt，文件存在读取内容，不存在提示用户
# 读取内容，循环读取，当无内容时退出循环，如果用户意外终止，提示用户已经被意外终止
try:
    f = open('test.txt')

    try:
        # 尝试循环读取内容
        while True:
            con = f.readline()
            con = con.strip()
            # 如果读取完成则退出
            if len(con) == 0:
                break

            time.sleep(2)
            print(con)

    except:
        print('程序被意外终止Ctrl+C')

except:
    print('该文件不存在')
