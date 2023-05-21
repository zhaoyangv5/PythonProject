'''
该数据类型的数据以“键值对”形式出现。
列表通过位置数字来索引，而字典中各条目的值可通过键来索引。
字典中的条目按照添加的时间前后而进行排序。
因字典是可变、有序的，所以字典中的条目可以被增删改。
条目中的“键”必须是不可变的对象，如数字，字符串，元组等。
条目中的“值”可以是任何类型的数据。
'''
import pprint

dict1 = {'Vendor':'HUAWEI','Model':'Quidway S5328C-EI','Ports':24,'Version':'VRP (R) Software, Version 5.150 (V200R005C00SPC500)'}
print(dict1)

#pprint模块
print(pprint.pformat(dict1))

print('='*25+'字典索引'+'='*25)

'''字典索引'''
print(dict1['Vendor'])
print(dict1['Ports'])

print('='*25+'字典嵌套'+'='*25)

'''字典嵌套'''
dev1 = {
    'r1': {
        'vendor': 'Cisco',
        'model': '4451',
        'ip': '192.168.11.51'
    },
    'sw1': {
        'vendor': 'Huawei',
        'model': 'S5700',
        'ip': '192.168.11.151'
    }
}
print(dev1['r1']['model'])
print(dev1['sw1']['vendor'])

print('='*25+'新建条目'+'='*25)

'''新建条目'''
dict1 = {'Vendor':'HUAWEI','Model':'Quidway S5328C-EI','Ports':24,'Version':'VRP (R) Software, Version 5.150 (V200R005C00SPC500)'}
dict1['vlan_m_str'] = '54'
dict1['vlan_m_int'] = 54
print(pprint.pformat(dict1))

print('='*25+'更新条目'+'='*25)

'''更新条目'''
dict1 = {'Vendor': 'HUAWEI', 'Model': 'Quidway S5328C-EI', 'Ports': 24, 'Version': 'VRP (R) Software, Version 5.150 (V200R005C00SPC500)', 'vlan_m': 54, 'vlan_m1': 54, 'vlan_m_str': '54', 'vlan_m_int': 54}
dict1['vlan_m_str'] = '55'
print(pprint.pformat(dict1))

print('='*25+'排序函数sorted()'+'='*25)
'''
排序函数 sorted()
返回值是字典对应的键进行排序后的列表。记住，它返回的是一个新生成的列表。原来的字典原封不动，没有一丝丝改变
'''
dict1 = {'Vendor': 'HUAWEI', 'Model': 'Quidway S5328C-EI', 'Ports': 24, 'Version': 'VRP (R) Software, Version 5.150 (V200R005C00SPC500)', 'vlan_m_str': '55', 'vlan_m_int': 54}
dict1 = sorted(dict1)
print(dict1)

dev2 = sorted(dev1['r1'])  #{'r1': {'vendor': 'Cisco', 'model': '4451', 'ip': '192.168.11.51'}, 'sw1': {'vendor': 'Huawei', 'model': 'S5700', 'ip': '192.168.11.151'}}
dev3 = sorted(dev1)
print(dev2)
print(dev3)

print('='*25+'字典方法'+'='*32)
print('='*25+'清空字典clear()'+'='*25)

'''清空字典clear()'''
dict1 = {'Vendor': 'HUAWEI', 'Model': 'Quidway S5328C-EI', 'Ports': 24, 'Version': 'VRP (R) Software, Version 5.150 (V200R005C00SPC500)', 'vlan_m_str': '55', 'vlan_m_int': 54}
print(dict1.clear())

print('='*25+'拷贝copy()'+'='*25)

'''
拷贝copy()
先说一下用赋值形式大拷贝，此时等于是拿多一块“标签”，往要拷贝的对象一贴完事。这个时候，这两个标签指向的对象是同一个。对其中一个修改，则另一个也会跟着修改
'''
#赋值
sw1 = {'vendor': 'Huawei', 'model': 'S5700', 'ip': '192.168.11.151'}
sw2 = sw1
print(id(sw1))
print(id(sw2))
sw2['ip'] = '192.168.111.111'
print(sw2['ip'])
print(sw1['ip'])

#拷贝copy
sw1 = {'vendor': 'Huawei', 'model': 'S5700', 'ip': '192.168.11.151'}
sw2 = sw1.copy()
print(id(sw1))
print(id(sw2))      #复制占用的另外一个空间
sw2['ip'] = '192.168.111.100'
print(sw2['ip'])
print(sw1['ip'])        #copy方法对原sw1的没有影响，只修改本sw2的

sw1 = {'vendor': 'Huawei', 'model': 'S5700', 'ip': ['192.168.11.151','192.168.11.152']}
sw2 = sw1.copy()
print(id(sw1))
print(id(sw2))      #sw1和sw2指向不同的空间对象
sw1['ip'][1] = '192.168.200.200'
print(sw1)
print(sw2)
print(id(sw1))
print(id(sw2))      # 仔细看好了，改 sw1 的内容，竟然 sw2 也被影响了


print('='*25+'索引get(),setdefault()'+'='*25)

'''
索引 get()、setdefault()
如果我们通过中括号键名的方式进行索引的话，如果该不存在该键，则会报错！
程序中途报错如果不做处理的话，会中断执行，比较麻烦。此时如果我们用方法get()，如果字典没有对应的键名，则会返回None，而非报错
'''
sw1 = {'vendor': 'Huawei', 'model': 'S5700', 'ip': '192.168.11.151'}
# print(sw1['version'])
print(sw1.get('version'))
print(sw1.get('version','原数据不含版本信息'))       ## 可以加多一个参数，如果在字典中找不到，则返回后面的信息。

'''方法setdefault()。它的作用是如果没找到键名对应的值，则直接新建一个'''
print(sw1.setdefault('ip'))
sw1.setdefault('version')
print(sw1)      #{'vendor': 'Huawei', 'model': 'S5700', 'ip': '192.168.11.151', 'version': None}
sw1.setdefault('local','shantou')   ## 如果找不到，增加新的条目后，给它一个初始值
print(sw1)          #{'vendor': 'Huawei', 'model': 'S5700', 'ip': '192.168.11.151', 'version': None, 'local': 'shantou'}

print('='*25+'keys(), values(), items()'+'='*25)

'''keys(), values(), items()'''
print(sw1.keys())
print(sw1.values())
print(sw1.items())

keys = sw1.keys()
print(keys)
sw1['port'] = 24
print(keys)             ## key这个变量所对应的“视图”会随着实际的字典内容的变化而变化

list_keys = list(sw1.keys())
print(list_keys)        # 此后它是什么就是什么了，跟原来的sw1字典没有半毛钱关系了，不会随着变化而变化了。


print('='*25+'更新 update()'+'='*25)

'''
更新 update()
把一个字典添加到另一个字典上
'''
sw1 = {'vendor': 'Huawei', 'model': 'S5700'}
sw1.update({ 'local': 'shantou', 'ports': 24})      ## 如果原字典中没有，则直接添加。
print(sw1)
sw1.update({ 'local': 'shantou', 'ports': 48})      # 如果原字典中已存在，则直接进行修改。
print(sw1)

print('='*25+'删除元素 del'+'='*25)

'''删除元素 del'''
sw1 = {'vendor': 'Huawei', 'model': 'S5700'}
del sw1['model']
print(sw1)

list1 = [1,2,3]     #列表也可以这么使用
del list1[1]
print(list1)

print('='*25+'字典的创建方式'+'='*25)

'''文本创建'''
sw1 = {'vendor': 'Huawei', 'model': 'S5700'}

'''构造函数 dict()'''
sw1 = dict(vendor='Huawei',model='S5700')
print(sw1)

print('*'*50)
'''利用元组构造'''
#元组中第一个元素是键（key），第二个元素是值（value），这样组成一个条目（item）；而后各个条目组成一个列表，传入dict()中进行构造
sw1 = dict([('vendor','Huawei'),('model','S5700')])
print(sw1)

print('*'*50)
'''
dict.fromkeys
这是一个“类”的方法,也就是说只有类没有对象，我们通过类的方法来生成对象
经常用这个方法来建一个字典模板，里面只有键，值为空
'''
sw1_keys = ['vendor','model','local','ports']
sw1 = dict.fromkeys(sw1_keys)       #默认的情况下，dict.fromkeys给每个条目的值赋了个None值
print(sw1)

print('*'*50)
sw1_keys = ['vendor','model','local','ports']
sw1 = dict.fromkeys(sw1_keys,'wgsy_none')
print(sw1)
print(pprint.pformat(sw1))

print('*'*50)
sw1_keys = ['vendor','model','local','ports']
sw1 = dict.fromkeys(sw1_keys, [])
print(sw1)
# sw1['vendor'].append('huawei')      #{'vendor': ['huawei'], 'model': ['huawei'], 'local': ['huawei'], 'ports': ['huawei']}
# print(sw1)
sw1['vendor'] = 'huawei'
print(sw1)