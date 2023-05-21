'''
Tests
Jinja2的tests校验还挺多，具体可以参考其官方文档Template Designer Documentation
'''

from jinja2 import Environment, FileSystemLoader
import yaml
'''
defined
Defined校验可以用来判断yaml资源数据中某个变量是否已经定义了
'''

#测试defined与上篇的过滤器default功能类似，甚至还麻烦一点，但是它能实现根据变量的申明与否，执行不同的命令
env = Environment(
    loader=FileSystemLoader('./templates'),
    trim_blocks=True,
    lstrip_blocks=True)

template = env.get_template('defined.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/defined.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''
iterable
测试iterable能检查一个对象是不是迭代器。通过这项测试，我们在模板中可以根据对象类型设置不同的分支
'''

template = env.get_template('iterable.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/iterable.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = 'Layer3Switch-3-iterable.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''
join
复习 join

我们知道创建多个vlan，trunk口放通多个vlan，指令可以如下：

vlan 30 40 50 60
……
port trunk allow-pass vlan 30 40 50 60
'''
template = env.get_template('iterable_join.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/iterable.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = 'Layer3Switch-3-iterable_join.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))