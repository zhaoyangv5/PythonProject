
from pprint import pprint


'''
跨行信息组字典
代码呈现：display ip interface | include Address|current|Unit 之后的接口的MTU值
'''
print('*'*20+' 跨行信息组字典 '+'*'*25)

result = {}             ## 这个字典用来装结果，最开始它是个空字典
with open('disp_ip_int.txt') as f:
    for line in f:
        # print(line)
        if not line.startswith('Line'):
            if 'current state' in line:
                # print(line.split())             #['LoopBack0', 'current', 'state', ':', 'UP']
                interface = line.split()[0]     #将带有current state的数据分裂，并提取索引0的字符串   LoopBack0
                # print(interface)
            elif 'Maximum Transmit Unit' in line:
                # print(line.split())             #['The', 'Maximum', 'Transmit', 'Unit', ':', '1490', 'bytes']
                mtu = line.split()[-2]            ##将带有current state的数据分裂，并提取索引-2的字符串   1490
                # print(mtu)
                # print(f'{interface:15}{mtu}')     #f 字符串格式化方法 :15表示站15个字符宽度     LoopBack0      1490

                result[interface] = mtu           #加入字典result

print(result)
# print(pprint(result))               #有时候字典太短了，函数 pprint 与可能打印得跟函数 print 一样



'''
嵌套字典
'''
print('*'*20+' 嵌套字典 '+'*'*25)
print('*'*20+' 没有NULLO '+'*'*25)

with open('disp_ip_int.txt') as f:
    for line in f:
        if not line.startswith('Line'):
            if 'current state' in line:
                interface = line.split()[0]
            elif 'Maximum Transmit Unit' in line:
                mtu = line.split()[-2]    # 为什么是 -2 ，是测试出来的，不是拍脑袋拍出来的。
            elif 'Internet Address'  in line:
                # print(line.split())
                ip_address = line.split()[-1]
                print(f'{interface:15}{ip_address:17}{mtu}')    #接口 NULL0 此时丢了，因为它没 IP 信息


print('*'*20+' 带NULLO '+'*'*25)

result = {}
with open('disp_ip_int.txt') as f:
    for line in f:
        if not line.startswith('Line'):
            if 'current state' in line:      # 开始找接口
                interface = line.split()[0]  # 提取接口信息
                result[interface] = {}       # 以“接口名”作为键，其值为空字典，就在这里开始嵌套。
            elif 'Maximum Transmit Unit' in line:
                mtu = line.split()[-2]
                result[interface]['mtu'] = mtu         # 收集 mtu 信息
            elif 'Internet Address'  in line:
                ip_address = line.split()[-1]
                result[interface]['ip'] = ip_address   # 收集 ip 信息

pprint(result)


'''过滤空值'''
#上个代码带有NULLO的空值，此代码剔除
print('*'*20+' 剔除NULLO '+'*'*25)

result = {}
with open('disp_ip_int.txt') as f:
    for line in f:
        if not line.startswith('Line'):
            if 'current state' in line:
                interface = line.split()[0]
            elif 'Maximum Transmit Unit' in line:
                mtu = line.split()[-2]
            elif 'Internet Address'  in line:
                ip_address = line.split()[-1]
                result[interface] = {}         # 看好了，其实只是调整一下代码的顺序。
                result[interface]['mtu'] = mtu
                result[interface]['ip'] = ip_address

pprint(result)