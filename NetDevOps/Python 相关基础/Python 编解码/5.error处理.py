'''
掌握Python编解码过程定位问题及问题处理
'''

# 方式合适很重要
device_unicode = "华为"
print(device_unicode.encode("ASCII"))       #提示错误了，这个已经超过了ASCII码的操作范围了。这种我们日常最好记住了
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)


#如果我们用合适方式（如utf-8）进行编码，然后试图用不合适方式（如ASCII）来解码，那自然也会报错!
# >>> device_unicode = "华为"
# >>> device_bytes = device_unicode.encode('utf-8')
# >>> device_bytes.decode('ascii')
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     device_bytes.decode('ascii')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 0: ordinal not in range(128)
# >>>

# >>> device_unicode = "华为"
# >>> device_bytes_utf16 = device_unicode.encode('utf-16')
# >>> device_bytes_utf16.decode('utf-8')
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     device_bytes_utf16.decode('utf-8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
# >>>

#错误消息可能是个好消息，如果没报错来对乱码或者误导信息就更遭了
# >>> device_unicode = "华为"
# >>> device_bytes_utf8 = device_unicode.encode('utf-8')
# >>> device_bytes_utf8
# b'\xe5\x8d\x8e\xe4\xb8\xba'
# >>> device_bytes_utf8.decode('utf-16')
# '跥\ue48e몸'

'''encode过程中的错误处理'''
#到遇到问题时候往往老师就在身边。我们尝试着help一下
# >>> help(str.encode)
# Help on method_descriptor:
#
# encode(self, /, encoding='utf-8', errors='strict')
#     Encode the string using the codec registered for encoding.
#
#     encoding
#       The encoding in which to encode the string.
#     errors
#       The error handling scheme to use for encoding errors.
#       The default is 'strict' meaning that encoding errors raise a
#       UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
#       'xmlcharrefreplace' as well as any other name registered with
#       codecs.register_error that can handle UnicodeEncodeErrors.
#上述告知encode过程中，默认用了strict（严格）方式，发生错误是就报UnicodeEncodeError错。
# 大家可以回到前面的几个例子看看，是不是报UnicodeEncodeError错。除了strict，帮助还告诉我们可以用ignore（忽略），replace（代替）

'''
>>> device_unicode = "huawei华为"
>>> device_unicode.encode('ascii','ignore')
b'huawei'
>>> device_unicode.encode('ascii','replace')
b'huawei??'
>>> device_unicode.encode('ascii','namereplace')
b'huawei\\N{CJK UNIFIED IDEOGRAPH-534E}\\N{CJK UNIFIED IDEOGRAPH-4E3A}'
'''
# 这里我们用位置参数的方式传入，也可以用关键字参数传入。
# 在遇到encode不了时，如果参数error为ignore时，直接忽略；如果为replace时，则替换成问号；
# 如果namereplace时，则替换成unicode编码名（不常用)


'''decode过程中的错误处理'''
'''
>>> device_unicode = "huawei华为"
>>> device_unicode_utf8 = "huawei华为".encode('utf-8')
>>> device_unicode_utf8
b'huawei\xe5\x8d\x8e\xe4\xb8\xba'
>>> device_unicode_utf8.decode('ascii','ignore')
'huawei'
>>> device_unicode_utf8.decode('ascii','replace')
'huawei������'
>>> device_unicode_utf8.decode('ascii','namereplace')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    device_unicode_utf8.decode('ascii','namereplace')
TypeError: don't know how to handle UnicodeDecodeError in error callback
>>> 
'''