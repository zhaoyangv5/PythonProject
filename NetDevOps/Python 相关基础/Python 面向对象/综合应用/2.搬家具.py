"""
步骤分析
需求涉及两个事物:房⼦子 和 家具，故被案例例涉及两个类:房⼦子类 和 家具类。

定义类
房⼦子类
    实例例属性
       房⼦子地理理位置
       房⼦子占地⾯面积
       房⼦子剩余⾯面积
       房⼦子内家具列列表
实例例⽅方法
    容纳家具
显示房屋信息

家具类
    家具名称
    家具占地⾯面积

"""
# 家具类
class Furniture():
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area

# 房子类
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address}, 占地面积{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳加固"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬入后，房屋剩余面积= 之前剩余面积 - 该家具面积
            self.free_area -= item.area

        else:
            print(f'{item.name}太大，剩余面积不足，无法容纳')

# 创建对象并调用实例属性和方法
bed = Furniture('双人床', 6)
print(bed.name, bed.area)
jia1 = Home('北京', 1200)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('篮球场', 1500)
jia1.add_furniture(ball)
print(jia1)