
from pprint import pprint

'''
同行信息组字典
代码呈现：disp ip int bri 之后各个接口的IP地址
'''

result = {}   # 这个字典用来装结果，最开始它是个空字典。
with open('disp_ip_int_bri.txt') as f:
    for line in f:
        # print(line)   # 想调测可以在各个地方嵌入函数print
        line = line.split()
        print(line)
        if line and len(line)>1:   # 这一行主要是为了适配元文本中 '<SW-XXXX-S5328C-EI-HW>' 这一行的情形，否则程序会报错。
            if line[1][0].isdigit():    #isdigit()常常被用来判断一个字符串是否为纯数字字符串
                interface, address, *other = line   # 这个 *other 有点超出我们的知识范围了，即剩下的都给打包一个叫other的成列表，了解一下即可。
                # print(other,type(other))
                result[interface] = address
# print(result)
print(pprint(result))



