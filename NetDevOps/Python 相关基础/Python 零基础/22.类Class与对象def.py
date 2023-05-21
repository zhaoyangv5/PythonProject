'''
类是对一类事物的抽象总称，比如人类、交换机、网络设备、端口。对象是类的一个实例化，是一个相对而言的实体，
比如小明是具体的一个人，as01交换机是具体的一个交换机，as01交换机的Eth1/1端口是一个具体的端口，这些都是具体的，是对象。
在编程中，根据类创建一个对象的过程，我们称之为实例化
'''
class Switch(object): # 通过Class <类名>
    description = '提供交换能力的网络设备'

    def __init__(self, ip, name, username, password):
        self.ip = ip
        self.name = name
        self.username = username
        self.password = password
        self.connect()  # 调用实例化后对象的方法进行登录连接

    def connect(self):
        # 在方法中调用自己的属性
        print('使用用户：{}登录交换机完成'.format(self.username))

    def send_commad(self, cmds):
        # 接受参数发送多条命令
        for cmd in cmds:
            print('发送命令{}成功'.format(cmd))

#对象的实例化与使用

# 定义好类之后，我们就可以使用类名进行实例化出一个对象
# 实例化，<类名>(<__init__方法的参数赋值>)
dev = Switch(ip='192.168.1.1', name='as01', username='admin', password='admin123')
# 使用点来访问对象属性和类属性，<对象>.<属性名>
dev_ip = dev.ip

# 使用点来调用对象方法 <对象>.<对象方法>(<参数>)
cmds = ['show version', 'show clock']
dev.send_commad(cmds)



'''继承'''


class Switch(object):     # 在Python3中，括号中的object可以省略
    def __init__(self, model, os_version, ip_add):
        self.model = model
        self.os_version = os_version
        self.ip_add = ip_add

    def description(self):
        description = f'Model  : {self.model}\n'\
                 f' OS Version : {self.os_version}\n'\
                 f' IP Address : {self.ip_add}\n'
        return description

class Router(Switch):               #Switch是父类，Router是子类；Router由Switch继承而来，Switch被Router继承了
    pass

SW1 = Switch('Huawei S5700', 'V200R001C00', '192.168.11.11')
SW2 = Switch('Huawei S3700', 'V200R001C00', '192.168.11.12')

Router1 = Router ('Huawei S2200', 'V800R009C00', '192.168.11.21')
Router2 = Router ('Huawei S2200', 'V800R011C00', '192.168.11.22')

print(' SW1\n', SW1.description())
print(' SW2\n', SW2.description())
print (' Router1\n', Router1.description())
print (' Router2\n', Router2.description())

# 模块 (module)
#有了类的概念，我们可以把一些固定功能进行标准化封装，然后存在另一个py文件中，形成模块(module)。后续我们再要使用，则直接import即可。
# 其实，python第三方模块都是这么一个套路
