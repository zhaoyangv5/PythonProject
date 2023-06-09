"""
语法
try:
    可能发生错误的代码
except 异常类型：
    如果捕获到的该异常类型执行的代码

注意：
1.如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
2.一般try下方只放一行尝试执行的代码
"""

try:
    print(num)
    # print(1/0)
except NameError:
    print('有错误')