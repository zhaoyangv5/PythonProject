'''
函数的定义方式如下：
以def开头
空一个编写函数名，函数名建议使用蛇形命名法
函数名后圆括号，括号内可以编写参数，也可以不写参数
圆括号后接冒号，回车，一个缩进（4个空格），编写函数内的代码块。
def func_name(<参数1>,<参数2>,..,<参数N>):
    <代码块>
    return <返回值>
其中参数可以是零个，也可以是多个。参数可以给默认值，默认值的参数一定要在无默认值参数的后面。
'''
def gen_intf_desc_configs(intf_name,description='NetDevOps'):
    # 模板字符串
    intf_desc_config_tmpl = f'''interface {intf_name}
description {description}'''
    # 通过format函数格式化出配置
    configs = intf_desc_config_tmpl.format(intf_name=intf_name,description=description)
    # 配置以行为单位，整理成列表，返回配置
    return configs.splitlines()

#函数要先定义才能调用，调用的时候直接函数名，给各个参数赋值即可。

#赋值的逻辑有两种，按位置赋值和按参数名赋值。两种方式可以结合，按位置赋值的方法排在按参数赋值的方法前。

#按位置赋值，就是按照参数的位置一一对应，Python会帮我们自动对齐参数和所赋值，一定要注意顺序，
#顺序不对可能导致代码错误（这种错误可能不是代码报错，而是由于赋值不对，导致出的结果不对），示例：

intf_name = 'Eth1/1'
description = 'configed by netdevops'
configs = gen_intf_desc_configs(intf_name,description)
print(configs)
#有默认值的参数我们可以不赋值，这个参数将使用默认值。
# 这个时候函数的description参数会使用默认值NetDevOps
configs = gen_intf_desc_configs(intf_name)
print(configs)
#按参数名赋值，顺序可以调整，但建议尽量按顺序赋值，我们显示的告诉函数每个参数我们赋值为多少，示例

configs = gen_intf_desc_configs(intf_name=intf_name,description=description)
# 等同于
configs = gen_intf_desc_configs(description=description,intf_name=intf_name)
#我们也可以按位置和按关键字混合使用，但对于新手最佳实践我们总结：

# 参数相对比较少，可以使用按位置赋值的方式
# 复杂参数的情况下，第一个参数使用按位置赋值，即我们可以直接传入值，其余参数，按顺序显示地使用参数名赋值
# （即使是写了几十万行代码，笔者仍保留这个习惯，使用这种方法，良好的可读性非常重要）
configs = gen_intf_desc_configs(intf_name,description=description)


print('*'*20+' return返回值 '+'*'*25)

'''
函数返回值return
return的作用，其用户终止函数，并返回一些数据（如果有）；默认情况下，返回None（如果无）。 
借助return这个操作符，结果就灵活很多了。你调用完函数，接住结果后，又可以重新使用Python的基础功能（如循环遍历、分支判断等）
'''

def conf_intf(inf, ip, mask):
    print('interface',inf)
    print('ip address',ip, mask)
    # return None                                      ## 如果你不写return内容，Python会默默地帮你补上这一行。（缺省情况）

# print(conf_intf('ge1/0/1','192.168.10.1','255.255.255.0'))

result = conf_intf('ge1/0/1','192.168.10.1','255.255.255.0')   #函数赋值给一个变量
print(result)               #结果为NONE，原因是定义函数时，函数默认会自带return NONE

print('='*50)

def conf_intf(inf, ip, mask):
    config = f'interface{inf}\nip address{ip}{mask}'
    return config           # 将config值返回给conf_intf

result = conf_intf('ge1/0/1','192.168.10.1','255.255.255.0')
print(result)

print('*'*20+' return 操作符（终止函数 '+'*'*25)
'''return 操作符（终止函数）'''

def conf_intf(inf, ip, mask):
    config = f'interface{inf}\nip address{ip}{mask}'
    return config           # 将config值返回给conf_intf
    print('这些是无效数据！')   # 调用函数，这个print是不会执行的。

result = conf_intf('ge1/0/1','192.168.10.1','255.255.255.0')
print(result)


print('*'*20+' return 操作符（返回多值) '+'*'*25)
''' return 操作符（返回多值）'''

def conf_intf(inf, ip, mask):
    config_int = f'interface {inf}'
    config_ip = f'ip address {ip}{mask}'
    return config_int, config_ip            #返回的函数值是tuple类型

result = conf_intf('ge1/0/1','192.168.10.1','255.255.255.0')
print(result, type(result))
intf, ip_addr = result      #tuple的赋值方法
print(intf, ip_addr)


print('*'*20+' docstring '+'*'*25)
'''
docstring
简单介绍一下，函数体的第一行，可以写一个长字符串，作为函数说明
'''

def conf_intf(inf, ip, mask):
    '''本函数可生产接口配置'''

    config_int = f'interface {inf}'
    config_ip = f'ip address {ip}{mask}'
    return config_int, config_ip  # 返回的函数值是tuple类型

result = conf_intf('ge1/0/1','192.168.10.1','255.255.255.0')
print(result, type(result))
intf, ip_addr = result      #tuple的赋值方法
print(intf, ip_addr)

print(conf_intf.__doc__)