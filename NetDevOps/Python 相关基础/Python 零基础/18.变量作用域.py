'''
1.1 LEGB
Python在变量查找方面，遵循一个叫LEGB原则，其在接触一个变量后，会按照这个顺序依次进行查找匹配。
L（local），本地（比如当前函数内部）
E（enclosing），上一层本地（比如嵌套函数的外层函数内部）
G（global），全局（本程序内）
B（built-in），Python保留值

1.2 局部变量（local variables）
函数中定义的变量
一旦函数退出，这个变量随即失效

1.3 全局变量（global variables）
函数外部定义的变量
该变量仅在本模块内是“全局”的
如果跨模块使用变量，则需要用到导入（如import操作）。

'''

def conf_intf(intf, ip, mask):
    config = f'interface {intf}\nip address {ip} {mask}'  # 此时config为一个内部变量,其在函数内部，作用域仅为conf_intf函数中
    return config

# print(config)   #在外部调用会报错   NameError: name 'config' is not defined

'''我们怎么办内部变量的值给传到函数外面来呢？答案就是用return操作符'''
result = conf_intf('Vlanif201','172.25.1.234','255.255.255.224')  #函数的返回值赋值变量result，就传到外面了
print(result)