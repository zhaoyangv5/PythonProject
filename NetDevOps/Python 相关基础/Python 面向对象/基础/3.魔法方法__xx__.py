

# __init__()方法作用：初始化对象

class Washer():

    # 定义__init__，添加实例属性
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        # 类里面调用实例属性
        print(f'洗衣机宽度是{self.width},高度是{self.height}')

haier = Washer()
haier.print_info()



# 给类传递参数，
class Washer():

    # 定义__init__
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def print_info(self):
        # 类里面调用实例属性
        print(f'{self.name}洗衣机宽度是{self.width},高度是{self.height}')


# 创建对象，创建多个对象且属性值不同；调用实例方法
haier1 = Washer('haier1', 10, 20)
haier1.print_info()

haier2 = Washer('haier2', 50, 80)
haier2.print_info()


# __str__ 当使用print输出对象默认打印对象的内存地址，如果定义了__str__，那么就会打印这个方法中的return数据
class Washer():

    # 定义__init__
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def __str__(self):
        return '解释说明：类的说明或者对象状态的说明'

# 创建对象，创建多个对象且属性值不同；调用实例方法
haier1 = Washer('haier1', 10, 20)
print(haier1)


# __del__，当删除对象时，Python解释器会默认调用__del__()方法
class Washer():
    def __init__(self):
        self.width = 500

    def __del__(self):
        print(f'{self}对象已经删除')

haier3 = Washer()



print('*'*15)
# __dict__
class A():
    a = 0

    def __init__(self):
        self.b = 1

aa = A()
# 返回类内部所有属性和方法对应的字典
print(A.__dict__)
# 返回实例属性和值组成的字典
print(aa.__dict__)