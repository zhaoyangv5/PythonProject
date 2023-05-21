
# 捕获异常描述信息

try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)


# 捕获所有异常信息
try:
    print(num)
except Exception as e:   # Exception是所有程序异常类的父类
    print(e)