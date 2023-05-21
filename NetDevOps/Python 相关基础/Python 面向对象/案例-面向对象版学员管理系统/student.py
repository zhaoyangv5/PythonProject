# -*- coding: UTF-8 -*-


# 学员信息包含：姓名，性别，手机号
# 添加__str__魔法方法，方便查看学员对象信息

# 定义类
class Student():
    def __init__(self, name, gender, tel):
        # 定义姓名，性别，手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'

# 测试
# student = Student('aa','nv', 11)
# print(student)