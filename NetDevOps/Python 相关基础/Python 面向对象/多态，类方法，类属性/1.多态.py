
"""
多态是指一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
定义：多态是一种使用对象的方式，子类重写父类的方法，调用不通子类对象的相同父类方法，可以产生不通的执行结果
好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变话
实现步骤：
定义父类，提供公共方法
定义子类，并重写父类方法
传递子类对象给调用者，可以看到不同子类执行效果不通
"""

# 定义父类，提供公共方法
class Dog():
    def work(self):
        pass

# 定义子类，子类重写父类方法，定义两个类表示2中警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人....')

class DrugDog(Dog):
    def work(self):
        print('追查毒品....')

# 定义人类
class Person():
    def work_with_dog(self, dog):
        dog.work()

# 创建对象，调用不同的功能，传入不同的对象
aa = ArmyDog()
dd = DrugDog()

xiaoqiu = Person()
xiaoqiu.work_with_dog(dog=aa)
xiaoqiu.work_with_dog(dog=dd)