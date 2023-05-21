
# Python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法。
# 在Python中，所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类。

# 定义父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 定义子类，继承父类
class B(A):
    pass

# 创建对象，验证结论
result = B()
result.info_print()