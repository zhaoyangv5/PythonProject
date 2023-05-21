'''
串（Strings）
Pyhon这么定义的string，一组不可变的Unicode字符序列，如str类即使用此编码
'''

device1 = "huawei"
device2 = "\u0068\u0075\u0061\u0077\u0065\u0069"
device3 = "\N{LATIN SMALL LETTER h}\N{LATIN SMALL LETTER u}\N{LATIN SMALL LETTER a}\N{LATIN SMALL LETTER w}\N{LATIN SMALL LETTER e}\N{LATIN SMALL LETTER i}"
print(device1 == device2 == device3)


shebei1 = "华为"
shebei2 = "\N{CJK UNIFIED IDEOGRAPH-534E}\N{CJK UNIFIED IDEOGRAPH-4E3A}"
shebei3 = "\u534e\u4e3a"
print(shebei1 == shebei2 == shebei3)

print(len(device1), len(shebei1))       #用len函数看一下其长度

print(ord('h'), ord('为'))       #函数ord可查询Unicode编码的代码点

print(chr(104), chr(20026))         #函数chr可根据Unicode编码的代码点查询字符


'''
字节（Bytes）
Pyhon这么定义的Bytes，一组不可变的字节序列。
Python中已约定俗成，Bytes的表示其实就是在strings表示之前加一个字母b
'''
b_shebei1 = b'\xe5\x8d\x8e\xe4\xb8\xba'
b_shebei2 = b"\xe5\x8d\x8e\xe4\xb8\xba"
b_shebei3 = b'''\xe5\x8d\x8e\xe4\xb8\xba'''
print(b_shebei1 == b_shebei2 == b_shebei3)
print(type(b_shebei1), len(b_shebei1))

#在Python如果一个字符是ASCII码表示的范围，则会直接按字符显示，并不会显示成编码值
b_device1 = b'huawei'
print(b_shebei1)
print(b_shebei1.hex())

b_device2 = b'\x68\x75\x61\x77\x65\x69'
print(b_device2)