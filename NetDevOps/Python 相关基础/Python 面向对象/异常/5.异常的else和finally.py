
"""
else表示的是如果没有异常要执行的代码
"""

try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，没有异常时执行的代码')


#finally表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    f = open('text.txt', 'r')
except Exception as e:
    print(e)
    f = open('text.txt', 'w')
else:
    print('没有异常')
finally:
    f.close()