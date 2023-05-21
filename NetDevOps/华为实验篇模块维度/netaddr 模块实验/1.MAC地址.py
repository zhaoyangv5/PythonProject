'''
MAC地址包含两部分：

前24比特是组织唯一标识符（OUI，OrganizationallyUniqueIdentifier），由IEEE统一分配给设备制造商。
后24比特是厂家自定义的。

'''


from netaddr import *

'''str -> EUI'''
# 【贝尔格式】aabb:cc80:7000
# 【华为格式】aabb-cc80-7000
# 【思科格式】aabb.cc80.7000

mac_huawei = 'aabb-cc80-7000'
# mac_al = 'aabb:cc80:7000'
# mac_cisco = 'aabb.cc80.7000'
#无论你是什么厂家的，只要是netaddr模块认识的MAC地址，则会全部被标准化
# print(EUI(mac_huawei))
# print(EUI(mac_al))
# print(EUI(mac_cisco))
# print(type(EUI(mac_huawei)))  #<class 'netaddr.eui.EUI'>

print('*'*50)


'''EUI ->str'''
mac_huawei_netaddr = EUI(mac_huawei)
print(mac_huawei_netaddr)
str_mac_huawei = str(mac_huawei_netaddr)
print(str_mac_huawei)
print(type(str_mac_huawei))         #<class 'str'>

print('*'*50)

#还可以使用bin、hex等分别变成二进制、十六进制
print(bin(mac_huawei_netaddr))   #0b101010101011101111001100100000000111000000000000
print(hex(mac_huawei_netaddr))   #0xaabbcc807000

#从Python内置函数角度，如果从类和对象的属性方法角度，也有类似功能
print(mac_huawei_netaddr.bits())

print('*'*50)
''' info、oui、ei'''
mac = EUI('6008-1009-64ab')
print(mac.info)
print(mac.oui)      ## 前24比特
print(mac.ei)       ## # 后24比特


print('*'*50)
'''dialect'''
#EUI类中有一个dialect属性，直译过来是方言或者土话的意思，即mac地址在EUI类中的展现形式
'''
dialect有如下几个枚举值，大家可以挨个尝试。
None
mac_unix
mac_unix_expanded
mac_cisco
mac_bare
mac_pgsql
'''

mac = EUI('00-1B-77-49-54-FD')

mac.dialect = mac_cisco
print(mac)
mac = str(mac).replace('.','-')
print(mac)
# class mac_huawei(mac_eui48): pass
#
# mac_huawei.word_size = 16
# mac_huawei.num_words = 3
# mac_huawei.word_sep = '-'
#
# mac.dialect = mac_huawei
# print(mac)  #1B-7749-54FD
# mac_huawei.word_fmt = '%.4x'
# print(mac)
# mac_huawei.word_fmt = '%.4X'
# print(mac)