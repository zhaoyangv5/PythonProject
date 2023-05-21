
# 多继承

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
        # 如果是先调⽤用了了⽗父类的属性和⽅方法，⽗父类属性会覆盖⼦子类属性，故在调⽤用属性前，先调⽤自己子类的初始化
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 调⽤用⽗父类⽅方法，但是为保证调⽤用到的也是⽗父类的属性，必须在调⽤用⽅方法前调⽤用⽗父类的初始化
    def make_master_cake(self):
        # 父类类名.函数（）
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 创建徒孙类
class TuSun(Prentice):
    pass

# 用Tusun类调用父类的方法和属性
xiaoqiu = TuSun()
xiaoqiu.make_cake()
xiaoqiu.make_master_cake()
xiaoqiu.make_school_cake()
xiaoqiu.make_cake()

