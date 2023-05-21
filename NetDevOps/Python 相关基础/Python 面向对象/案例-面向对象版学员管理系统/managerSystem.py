# -*- coding: UTF-8 -*-


"""
需求:
存储数据的位置: 文件(student.data)
     加载⽂文件数据
     修改数据后保存到⽂文件
存储数据的形式: 列列表存储学员对象
系统功能
     添加学员
     删除学员
     修改学员
     查询学员信息
     显示所有学员信息
     保存学员信息
     退出系统
"""
# 添加学员函数内部需要创建学员对象，故先导入student模块
from student import *

# 定义类
class StudentManager():
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 一. 程序⼊入⼝口函数，启动程序后执⾏行行的函数
    def run(self):
        # 加载学员信息
        self.load_student()

        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入目标功能序号
            menu_num = int(input('请输入您需要的功能序号: '))
            # 根据用户输入的序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员
                self.show_student()
            elif menu_num == 6:
                # 保存学员
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

# 二. 系统功能函数
    # 显示功能菜单 -- 打印序号的功能对应关系 -- 静态
    @staticmethod
    def show_menu():
        print('---------请选择如下功能---------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    # 添加学员
    def add_student(self):
        # print('添加学员')
        # 用户输入姓名，性别，手机号
        name = input('请输入您的姓名: ')
        gender = input('请输入您的性别: ')
        tel = input('请输入您的手机号: ')

        # 创建学员对象
        student = Student(name, gender, tel)
        # 将该对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 删除学员
    def del_student(self):
        # print('删除学员')
        # 用户输入目标学员姓名
        del_name = input('请输入要删除的学员姓名: ')

        # 如果用户输入的目标学员存在则删除，否则提示学员不存在
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                print('已删除：'+ i)
                break
        else:
            print('查无此人')

        # 打印学员列表，验证删除功能
        print(self.student_list)

    # 修改学员信息
    def modify_student(self):
        # print('修改学员')
        # 用户输入目标学员的姓名
        modify_name = input('请输入要修改的学员姓名: ')

        # 遍历列表数据，如果学员存在则修改，否则提示学员不存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名: ')
                i.gender = input('性别: ')
                i.tel = input('手机号: ')
                print(f'学员信息update成功，姓名：{i.name},性别：{i.gender}，手机号：{i.tel}')
                break
        else:
            print("查无此人")

    # 查询学员
    def search_student(self):
        # print('查询学员信息')
        # 用户输入目标学员的姓名
        search_student = input('请输入要查询的学员姓名: ')

        # 遍历列表数据，查询学员是否存在
        for i in self.student_list:
            if search_student == i.name:
                print(f'姓名：{i.name},性别：{i.gender}，手机号：{i.tel}')
                break
        else:
            print("查无此人")

    # 显示所有学员
    def show_student(self):
        # print('显示所有学员信息')
        # 显示所有学员信息
        print('姓名\t\t\t性别\t\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t\t{i.gender}\t\t{i.tel}')

    # 保存学员
    def save_student(self):
        # print('保存学员信息')
        # 打开文件
        f = open('student.data', 'w')

        # 文件写入学员数据
        # 注意1:文件写⼊入的数据不能是学员对象的内存地址，需要把学员数据转换成列列表字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        # [{'name': 'aa', 'gender': 'nv', 'tel': '111'}]
        print(new_list)
        # 注意2:文件内数据要求为字符串类型，故需要先转换数据类型为字符串串才能文件写⼊数据
        f.write(str(new_list))

        # 关闭文件
        f.close()

    # 加载学员信息
    def load_student(self):
        # print('加载学员数据')
        # 尝试以"r"模式打开数据文件，文件不存在则提示用户；文件存在（没有异常）则读取数据
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 1. 读取数据
            data = f.read()  # <class 'str'>
            print(data)

            # 2. 文件中读取的数据都是字符串且字符串内部为字典数据，故需要转换数据类型再转换字典为对象后存储到学员列表
            new_list = eval(data)    # <class 'list'>   [{'name': '张淑君', 'gender': '女', 'tel': '13888888888'}, {'name': '曾俊杰', 'gender': '男', 'tel': '13777777777'}]
            print(new_list)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # 3. 关闭文件
            f.close()