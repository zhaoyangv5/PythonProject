"""
需求
需求主线:
1. 被烤的时间和对应的地⽠瓜状态:
  0-3分钟:⽣生的
  3-5分钟:半⽣生不不熟
  5-8分钟:熟的
  超过8分钟:烤糊了了
2. 添加的调料料: ⽤用户可以按⾃自⼰己的意愿添加调料料

定义类
地⽠瓜的属性
     被烤的时间
     地⽠瓜的状态
     添加的调料料
地⽠瓜的⽅方法 被烤
       ⽤用户根据意愿设定每次烤地⽠瓜的时间
判断地⽠瓜被烤的总时间是在哪个区间，修改地⽠瓜状态 添加调料料
       ⽤用户根据意愿设定添加的调料料
       将⽤用户添加的调料料存储
显示对象信息

"""
# 定义地瓜初始化属性，后期根据程序员推进更新实例属性
class SweetPotato():
    def __init__(self):
        # 焙烤时间
        self.cook_time = 0
        # 地瓜状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []

    # 定义烤地瓜的方法
    def cook(self, time):
        # 烤地瓜的方法
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    # 添加调料
    def add_condiments(self, condiment):
        # 添加调料
        self.condiments.append(condiment)

    # 书写魔法方法， 用于输出对象状态
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static}, 添加的调料有{self.condiments}'

#创建对象，测试实例属性和实例方法
digua = SweetPotato()
print(digua)
digua.cook(5)
digua.add_condiments('酱油')
digua.add_condiments('盐')
print(digua)
