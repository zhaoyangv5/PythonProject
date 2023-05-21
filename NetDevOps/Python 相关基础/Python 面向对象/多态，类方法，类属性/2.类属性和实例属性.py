

"""
类属性就是 类对象 所拥有的属性， 他被 该类的所有实例对象 所共有
类属性可以使用 类对象 或 实例对象 访问
"""

# 设置和访问类属性
class Dog():
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

# 修改类属性
# 类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示是创建了一个实例属性

# 修改类属性
# 通过类修改
print('='*15 + '通过类属性修改'+ '='*15)
Dog.tooth = 12
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

print('='*15 + '通过对象修改'+ '='*15)
# 通过对象修改类属性
wangcai.tooth = 200
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
