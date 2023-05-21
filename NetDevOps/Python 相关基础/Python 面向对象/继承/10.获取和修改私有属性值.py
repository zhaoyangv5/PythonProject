


# 一般定义函数名get_xx用来获取私有属性，定义set_xx用来修改私有属性值

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

        # 定义私有属性
        self.__money = 200000

    # 定义函数：获取私有属性值
    def get__money(self):
        return self.__money

    # 定义函数：修改私有属性值
    def set_money(self):
        self.__money = 500

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')


    def make_cake(self):
        # 如果是先调⽤用了了⽗父类的属性和⽅方法，⽗父类属性会覆盖⼦子类属性，故在调⽤用属性前，先调⽤自己子类的初始化
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')


# 创建徒孙类
class TuSun(Prentice):
    pass

# 用Tusun类调用父类的方法和属性
xiaoqiu = TuSun()
print(xiaoqiu.get__money())

xiaoqiu.set_money()
print(xiaoqiu.get__money())