'''
字符
字符定义版本多种多样（历史原因），有往unicode字符方向演进的趋势。
# >>> dev_str = '华为'
# >>> type(dev_str)
# <class 'str'>
# >>> dev_str
# '华为'
# >>>

字节
字符的二进制表示形式
# >>> dev_bytes = '华为'.encode('utf-8')
# >>> type(dev_bytes)
# <class 'bytes'>
# >>> dev_bytes

码位
通常，Unicode标准中，码位以4-6个十六进制数字表示
# >>> '华为'.encode("unicode_escape").decode()
# '\\u534e\\u4e3a'
# >>>
'\\u534e\\u4e3a'其实是个字符串，因为需要在屏幕上显示出来。我们调整一下，把\\变成\，便可以得到码位
'''

'''
编码（encode)
字符序列（string）---->字节序列（bytes）
'''
dev_bytes = '华为'.encode('utf-8')
print(dev_bytes, type(dev_bytes))       #b'\xe5\x8d\x8e\xe4\xb8\xba' <class 'bytes'>

'''
解码（decode）
字节序列（bytes）---->字符序列（string）
'''
print(dev_bytes.decode('utf-8'))

print('='*20 + '混合编码原因' + '='*20)
# 问题原因及处理
'''混合编码原因'''
dev_bytes_2 = '华为'.encode('utf-8') + '思科'.encode('gbk')
print(dev_bytes_2)      #b'\xe5\x8d\x8e\xe4\xb8\xba\xcb\xbc\xbf\xc6'
# print(dev_bytes_2.decode('utf-8'))  #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbf in position 8: invalid start byte
print(dev_bytes_2.decode('gbk'))        ## 不报错，但是来乱码了    鍗庝负思科

#由于报错提示是0xbf引起的，我们可以对编码进行切片，不过需要找到相应字符的解码切片
print(dev_bytes_2[0:6].decode('utf-8'))
print(dev_bytes_2[6:len(dev_bytes_2)].decode('gbk'))
print(dev_bytes_2[0:6].decode('utf-8') + dev_bytes_2[6:len(dev_bytes_2)].decode('gbk'))


print('='*20 + 'chardet 方法' + '='*20)
'''
chardet 方法
第三方模块chardet 是一个比较常用的编码检查库，其实根据原始文本进行一些特征统计从而给出编码结果推测的。因此，它给是一个可能值，而非确定值
'''
import chardet

dev_bytes_2 = '华为'.encode('utf-8') + '思科'.encode('gbk')
print(chardet.detect(dev_bytes_2))      #很遗憾，它识别不出来。这很正常，它并不是万能的

dev_bytes_3 = '华为'.encode('utf-8') + '思'.encode('gbk')
print(chardet.detect(dev_bytes_3))
#这下它就识别出utf-8了。它的意思是， dev_bytes_3这玩意里面大概率的编码是utf-8, 确定性为87.625%。 这就是我们刚才之所以说它是统计学意义上的预估值，只能辅助


print('='*20 + '抓大放小方法' + '='*20)

'''
抓大放小方法
通常，一堆字节序列信息，有些杂乱的编码使得解码异常，我们可以称这种情况为“数据被污染”了。
如果使用第三方库chardet识别出一种编码格式，而且自信度confidence 还挺高的。那我们就可以抓大放小、舍小取大了。
在国内，有些设备支持中文配置（尤其是防火墙），大体会是两种编码utf-8、gbk
'''

dev_bytes_2 = '华为'.encode('utf-8') + '思科'.encode('gbk')
# print(dev_bytes_2.decode('utf-8'))          # 有可能不会报错，但会有乱码
print(dev_bytes_2.decode('utf-8',errors='ignore'))          # 直接忽略
print(dev_bytes_2.decode('utf-8',errors='replace'))         # 直接替换