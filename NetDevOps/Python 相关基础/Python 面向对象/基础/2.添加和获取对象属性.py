

class Washer():
    def wash(self):
        print('洗衣服')

    # 类里面获取对象属性
    def print_info(self):
        # 类里面获取实例属性
        # self.属性名
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier1 = Washer()

# 添加属性  对象名.属性名 = 值
haier1.width = 500
haier1.height = 800

# 类外面获取对象属性
print(f'haier1洗衣机的宽度是{haier1.width}')
print(f'haier1洗衣机的高度是{haier1.height}')

haier1.print_info()


