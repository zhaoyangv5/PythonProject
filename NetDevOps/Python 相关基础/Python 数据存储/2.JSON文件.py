'''
json.dump、json.dumps、json.load、json.loads，如果不带s的，直接是操作文件；如果带s的，不直接操作文件，只涉及到字符串str

json.load	读取 JSON 文件，转成Python对象。
json.loads	读取 JSON 字符串，转成Python对象。
'''
import json
import pprint

print('*'*20+'json.load'+'*'*25)
'''
json.load
读取json文件
'''

with open('sw_templates.json', 'r') as f:
    templates = json.load(f)

print(type(templates))
# print(templates)
pprint.pprint(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))


print('\n'+'*'*20+'json.loads'+'*'*25)
'''
json.loads
函数json.loads没办法读取文件，只能读取字符串。那也简单，我们借助read函数帮忙一下即可
'''
with open('sw_templates.json', 'r') as f:
    file_content = f.read()
    templates = json.loads(file_content)

# print(type(templates))
# print(templates)
pprint.pprint(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))


'''
写入（Writing）
json.dump	将Python对象转为JSON格式，写入文件。
json.dumps	将Python对象转为JSON格式，写入字符串。
'''
print('\n'+'*'*20+'写入（Writing)'+'*'*25)
print('*'*20+'json.dump'+'*'*25)

'''
json.dump
方法 json.dump 可直接与文件互动，无需write帮助，更适合用来把JSON格式直接写入文件
'''
access_template = [
    "port link-type access", "port default vlan 110",
    "port discard tagged-packet", "port link-flap protection enable"
]

trunk_template = [
    "port priority 5", "port link-type trunk",
    "port trunk allow-pass vlan 100", "port link-flap interval 50",
    "port type uni"
]

to_json = {'trunk': trunk_template, 'access': access_template}

print(type(to_json))
print(to_json)

with open('sw_templates_dump.json', 'w') as f:
    json.dump(to_json, f)                           #直接操作的json文件


print('\n'+'*'*20+'json.dumps'+'*'*25)

'''
json.dumps
方法 json.dumps 很适合在应用间传递数据，如API
'''

access_template = [
    "port link-type access", "port default vlan 110",
    "port discard tagged-packet", "port link-flap protection enable"
]

trunk_template = [
    "port priority 5", "port link-type trunk",
    "port trunk allow-pass vlan 100", "port link-flap interval 50",
    "port type uni"
]

to_json = {'trunk': trunk_template, 'access': access_template}

print(type(to_json))
print(to_json)

with open('sw_templates_dumps.json', 'w') as f:
    f.write(json.dumps(to_json))                #写入的json格式的字符串


print('\n'+'*'*20+'带参数写入（Writing）'+'*'*25)

'''
带参数写入（Writing）
sort_keys	按键值进行排序
indent	缩进
'''
access_template = [
    "port link-type access", "port default vlan 110",
    "port discard tagged-packet", "port link-flap protection enable"
]

trunk_template = [
    "port priority 5", "port link-type trunk",
    "port trunk allow-pass vlan 100", "port link-flap interval 50",
    "port type uni"
]

to_json = {'trunk': trunk_template, 'access': access_template}

print(type(to_json))
print(to_json)

with open('sw_templates_dump.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)                 #带参数直接读取json文件

with open('sw_templates_dump.json') as f:
    print(f.read())             #直接用Python打印出来


print('\n'+'*'*20+'更改数据类型'+'*'*25)

'''
更改数据类型
Python ->	-> JSON		JSON ->	   -> Python
dict	       object   object	      dict
list,tuple	   array	array	      list
str	           string	string	      str
int, float	   number	number (int)  int
True	       true		number (real) float
False	       false	true	      True
None	       null		false	      False
                        null	      None
'''
trunk_template = (
    "port priority 5",
    "port link-type trunk",
    "port trunk allow-pass vlan 100",
    "port link-flap interval 50",
    "port type uni"
)

print(type(trunk_template))     #元组类型

with open('trunk_template.json', 'w') as f:
    json.dump(trunk_template, f, sort_keys=True, indent=2)

# 此时可以打开trunk_template.json文件看看

templates = json.load(open('trunk_template.json'))
print(type(templates))      #list类型
print(templates)


print('\n'+'*'*20+'限制数据类型'+'*'*25)

'''限制数据类型'''

#在Python中用元组作为键，这是允许的，但如果将其写入JSON格式，则马上报错
access_template = [
    "port link-type access", "port default vlan 110",
    "port discard tagged-packet", "port link-flap protection enable"
]

trunk_template = [
    "port priority 5", "port link-type trunk",
    "port trunk allow-pass vlan 100", "port link-flap interval 50",
    "port type uni"
]

to_json = {('trunk','huawei'): trunk_template, 'access': access_template}       #元组作为键值，会报错

print(type(to_json))
print(to_json)

with open('json_keytuple_dump.json', 'w') as f:
    # json.dump(to_json, f)       ##运行Python，两行print可正常打印，而写入json_keytuple_dump.json时会出错
    json.dump(to_json, f, skipkeys=True)    #用skipkeys参数则可忽略掉元组键值,('trunk','huawei')丢掉，access正确的保留
#!!!!特别注意，skipkeys=True这种方式会丢失信息，慎用！！！

with open('json_keytuple_dump.json', 'r') as f:
    print(f.read())

'''
JSON数据中，字典键只允许是字符串，但是在python字典中是允许数字类型的。此时dump过程不会报错，而是默默地进行了调整替换
'''
d = {5700:24, 3700:48}
print(json.dumps(d))