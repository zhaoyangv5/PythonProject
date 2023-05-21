"""
当捕获多个异常时，可以把要捕获的异常类型的名字，放在except后，并使用元组的方式进行书写

"""
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('Error')