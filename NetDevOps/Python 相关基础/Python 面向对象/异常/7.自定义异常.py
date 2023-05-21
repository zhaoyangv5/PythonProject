# -*- coding: UTF-8 -*-

#在Python中，抛出自定义异常的语法为raise 异常类对象

# 需求：密码长度不足，则报异常

# 自定义异常类，继承Exception
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len


    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length}, 不能少于{self.min_len}个字符'


# 抛出异常
def main():
    try:
        con = input('请输入密码: ')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    # 捕获异常
    except Exception as e:
        print(e)
    else:
        print('没有异常，输入密码完成')

main()