# 类： 洗衣服  功能  洗衣服

# 1. 定义类
class Washer():
    def wash(self):
        print('我会洗衣服')
        # <__main__.Washer object at 0x0000024BA2B34240>
        print(self)


# 2. 创建对象
haier1 = Washer()
# <__main__.Washer object at 0x0000018B7B224240>
print(haier1)
# haier1对象调用实例方法
haier1.wash()


haier2 = Washer()
# <__main__.Washer object at 0x0000022005857EF0>
print(haier2)