'''
from netaddr import IPAddress,IPNetwork,cidr_merge,IPRange    # 不嫌麻烦，挨个导入

IPAddress 处理IP地址
IPNetwork 处理IP网段
cidr_merge 处理网段汇总
IPRange 构造类，处理IP范围
'''

from netaddr import *

ip1 = IPAddress('192.168.2.1')
ip2 = IPAddress('2001::1')
# ip3 = IPAddress('2001::1-aaa')   #如果传输的IP地址非法，则Python会抛出异常
print(type(ip1), type(ip2))
# print(ip1, ip2, ip3)

print(dir(ip1))
print([method for method in dir(ip1) if not method.startswith('_') and method.islower()] )

print(ip1.info)
print(ip1.version)
print(ip1.bin)

print('*'*50)

ip1 = IPNetwork('192.168.2.11/24')  # 前缀
ip2 = IPNetwork('192.168.2.12/255.255.255.0') # 子网掩码
ip3 = IPNetwork('2001::1/64')  # 可以支持IPv6，往下内容多以IPv4演示

print(ip1, ip2, ip3)
print(type(ip1), type(ip2))
print([method for method in dir(ip1) if not method.startswith('_') and method.islower()])

print(ip1.netmask)
print(ip3.netmask)

print('*'*50)


'''ip -> str'''
# IPNetwork -> IPAddress
print(ip1, type(ip1))
ip1_add = ip1.ip
print(ip1_add, type(ip1_add))
print(ip1_add.bits())

ip1_str = str(ip1)
print(ip1_str, type(ip1_str))  #有了字符串类型数据后，就可以按照字符串方法，正则表达式，TextFSM等进行处理了

'''划分子网'''

ip_m = IPNetwork('192.168.2.0/24')
print(ip_m.subnet(27))
print(list(ip_m.subnet(27))) #我们用Python内置函数list处理成IPNetwork列表。如果你想得到网段信息文本，也可以配合一下列表推导式
snet_list = [str(snet) for snet in ip_m.subnet(27)]
print(snet_list)

print('*'*50)

'''获取网段可用地址'''
ip_s1 = IPNetwork('192.168.2.0/27')
print(ip_s1.iter_hosts())
# ip = [ip for ip in ip_s1.iter_hosts()]  # [IPAddress('192.168.2.1'), IPAddress('192.168.2.2'),
ip = [str(ip) for ip in ip_s1.iter_hosts()]  #处理从字符串['192.168.2.1', '192.168.2.2',
print(ip)

print('*'*50)

'''网段归属判断'''
ip1 = IPAddress('192.168.2.1')
ip_s1 = IPNetwork('192.168.2.0/27')
ip_s2 = IPNetwork('192.168.2.32/27')
print(ip1 in ip_s1)
print(ip1 in ip_s2)


'''cidr_merge（IP汇总）'''
ip_s1 = IPNetwork('192.168.2.0/27')
ip_s2 = IPNetwork('192.168.2.32/27')
ip = cidr_merge([ip_s1, ip_s2])   #[IPNetwork('192.168.2.0/26')]
print(ip)

print('*'*50)

'''IPRange（IP范围）'''
ip_range1 = IPRange('192.168.2.1','192.168.2.15')
print(ip_range1, type(ip_range1))

ip = [str(ip) for ip in ip_range1]
print(ip)