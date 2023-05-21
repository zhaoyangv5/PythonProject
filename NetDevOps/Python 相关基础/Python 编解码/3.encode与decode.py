'''
str ->【编码方式】 -> bytes	encode
bytes ->【解码方式】 -> str	decode

str ->【编码方式】 -> bytes ->【解码方式】 ->  str
使用的编码方式和解码方式要保持一致，否则就容易发生混乱。（如用UTF-8编码，那最好解码也用UTF-8)

有个叫“Unicode三明治”的规则：

1、bytes数据传递进程序，尽快解码，即 bytes -> str。

2、程序中尽量都用Unicode，即 str -> str。

3、在传输前尽快编码，即 str -> bytes。
'''

'''对象.encode'''
# >>> device_str = "华为"
# >>> type(str_device)
# <class 'str'>
# >>> device_bytes_utf8 = device_str.encode('utf8')
# >>> device_bytes_utf8
# b'\xe5\x8d\x8e\xe4\xb8\xba'
# >>> device_bytes_utf16 = device_str.encode('utf16')
# >>> device_bytes_utf16
# b'\xff\xfeNS:N'
# >>> device_bytes_utf32 = device_str.encode('utf32')
# >>> device_bytes_utf32
# b'\xff\xfe\x00\x00NS\x00\x00:N\x00\x00'
# >>> device_bytes_gbk = device_str.encode('gbk')
# >>> device_bytes_gbk
# b'\xbb\xaa\xce\xaa'
# >>> device_bytes_ascii = device_str.encode('ascii')  # 报错，超ASCII的范围，其无能为力
# Traceback (most recent call last):
#   File "<pyshell#63>", line 1, in <module>
#     device_bytes_ascii = device_str.encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# >>> device_bytes_gbk == device_bytes_utf8
# False
# >>> device_bytes_utf8 == device_bytes_utf16
# False
# >>> type(device_bytes_gbk)
# <class 'bytes'>

'''对象.decode'''
# >>> device_bytes_utf8
# b'\xe5\x8d\x8e\xe4\xb8\xba'
# >>> device_bytes_utf8.decode('utf8')
# '华为'
# >>> device_bytes_utf8.decode('utf16')
# '跥\ue48e몸'
# >>> device_bytes_utf8.decode('gbk')
# '鍗庝负'

'''类.encode（str.encode）'''
device_str = "华为"
print(type('华为'))
print(str.encode(device_str,'utf-8'))       ## 位置参数
print(str.encode(device_str,encoding='utf-8'))   # 关键字参数


'''类.decode（bytes.decode）'''

print([ each_fun for each_fun in dir(bytes) if each_fun.endswith('code')])

device_bytes_utf8 = b'\xe5\x8d\x8e\xe4\xb8\xba'
print(bytes.decode(device_bytes_utf8,'utf-8'))          # 位置参数
print(bytes.decode(device_bytes_utf8,encoding='utf-8'))     # 关键字参数