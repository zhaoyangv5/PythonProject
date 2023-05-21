
# 如果子类和父类拥有同名的属性和方法，子类创建对象调用属性和方法的时候，调用的是子类里面的同名的属性和方法

# 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 用徒弟类创建对象，并调用实例属性和方法，添加和父类同名的属性和方法用于重写
# 独创配方
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

# 展现当前类的层级继承关系
print(Prentice.__mro__)