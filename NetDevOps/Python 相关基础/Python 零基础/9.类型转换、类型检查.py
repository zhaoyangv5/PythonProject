'''
Python对基础数据提供了类型转换，比如用int函数将数据转为整数，float将对象转为浮点数，str将对象转为字符串，list将对象转为列表，
tuple将对象转为元组，set将对象转为集合。
其中列表、元组、集合可以通过对应函数相互转换，但是可能会丢失部分信息，比如排序，以及重复成员只会保留一个。
以上均不改变原来的数据的值，而是新返回一个数据，大家按需将返回值赋值给一个新的变量或者是赋值给原有的变量。
'''

# type函数可输出变量的类型
a = '1'
a = int(a)
print(a, type(a))  # 输出1 <class 'int'>

a = '1'
a = float(a)
print(a, type(a))  # 输出1.0 <class 'float'>

a = 100
a = str(a)
print(a, type(a))  # 输出100 <class 'str'>

a = (1, 2, 3)
a = list(a)
print(a, type(a))  # 输出 [1, 2, 3] <class 'list'>

a = [1, 2, 3]
a = tuple(a)
print(a, type(a))  # 输出 (1, 2, 3) <class 'tuple'>

a = [1, 2, 3, 3, 3]
a = set(a)
print(a, type(a))  # 输出{1, 2, 3} <class 'set'>,丢失了成员，顺序也无法保证。

#类型检查
#字符串isdigit()常常被用来判断一个字符串是否为纯数字字符串，即是否为数字的“照片”
print("switch".isdigit())
# isalpha()它检查一个字符串是否是只包含字母，而不包含其它
print('switch'.isalpha())
print('switch1'.isalpha())
# isalnum()这个有点点绕，它相当于（isdigit() or isalpha()），检查字符串是否包含字母或者数字
print('switch2022'.isalnum())
print('switch    2022'.isalnum())
