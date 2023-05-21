
# 所谓多继承就是一个类同时继承了多个父类
# 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法

# 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_a(self):
        print('这个师父的另一个方法')

# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_b(self):
        print('这是学校的另一个方法')

# 用徒弟类创建对象，并调用实例属性和方法
class Prentice(School, Master):
    pass

# 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
daqiu.make_a()
daqiu.make_b()