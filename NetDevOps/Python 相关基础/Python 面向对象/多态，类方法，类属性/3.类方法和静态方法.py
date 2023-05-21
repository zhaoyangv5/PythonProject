
# 类方法特点：需要用装饰器@classmethod来标识其为类方法，对与类方法，第一个参数必须是类对象，一般以cls作为第一个参数
# 类方法使用场景：
#   当方法中 需要使用类对象(如访问私有类属性等)时，定义类方法
#   类方法一般和类属性配合使用

class Dog():
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

wangcai = Dog()
result = wangcai.get_tooth()
print(result)


# 静态方法
# 需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）
# 静态方法也能够通过 实例对象 和 类对象 去访问

# 静态方法使用场景：
#       当方法中 既不需要使用实例对象（如实例对象，实例属性），也不需要使用类对象（如类属性，类方法，创建实例等）时，定义静态方法
#       取消不需要的参数传递，有利于 减少不必要的内存占用和性能消耗

class Dog():
    @staticmethod
    def info_print():
        print('这是一个狗类，用于创建狗实例....')

wangcai = Dog()
# 静态方法既可以使用对象访问又可以使用类访问
wangcai.info_print()
Dog.info_print()