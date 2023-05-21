

# 使用super()可以自动查找父类。调用顺序遵循__mro__类属性的书序，比较适合单继承使用

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 创建学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 2.1 super带参数写法
        # super(School, self).__init__()
        # super(School, self).make_cake()
        # 2.2 无参数
        super().__init__()
        super().make_cake()

# 用徒弟类创建对象，并调用实例属性和方法，添加和父类同名的属性和方法用于重写
# 独创配方
class Prentice(School):
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

    # 需求：一次性调用父类school Master的方法
    def make_old_cake(self):
        # 方法一：如果定义的类名修改，这里也要修改，麻烦；代码量庞大，冗余
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

    # 方法二：super()
    # 2.1 super(当前类名，self).函数
    #     super(Prentice, self).__init__()
    #     super(Prentice, self).make_cake()

    # 2.2 无参数super
        super().__init__()
        super().make_cake()


daqiu = Prentice()
daqiu.make_old_cake()
