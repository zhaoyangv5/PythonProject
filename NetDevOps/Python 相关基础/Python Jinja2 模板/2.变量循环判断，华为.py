'''
语法概述
Jinja2常用的基础语法大体有如下这些，加粗的本文介绍。

变量（Variables）
循环（Loop for）
条件（if/elif/else）
过滤（filters） - 特殊内置方法，可以转换变量
测试（tests） - 检查变量是否匹配条件
设置（set） - 变量的一些简化操作
包含（include） - 不同模板组合
Jinja2还允许模板间继承，对我们网络工程师来说，这可能稍微高阶一点了。我们先弄点来“应付”生产，其它的后续有机会再学习
'''
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os
import re

# 与上次实验脚本差异部分，这里我们从CMD取Jinja2模板和yaml配置参数。
# template_dir, template_file = os.path.split(sys.argv[1])
# vars_file = sys.argv[2]

# 如果过程中有异常，可以去除注释，用print()函数辅助定位。
# print(template_dir)
#print(template_file)
#print(vars_file)

# 通过template_dir, template_file = os.path.split(sys.argv[1])，模板的位置及模板内容。
env = Environment(
    loader=FileSystemLoader('./templates'),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template('sw_template.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/sw_info.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''变量（variables）'''

template = env.get_template('variables.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/variables.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))


'''
循环（for）
for 循环必须写在{% %}内，而且，其结束还必须显式标识，其结构体如下：

{% for x in xxx %}
  ......
{% endfor %}
'''
template = env.get_template('for.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/for.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''
条件判断（if）
{% if xxx %}
......
{% endif %}
'''
template = env.get_template('if.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/if_have_ospf.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''条件分支（if/elif/else）'''
template = env.get_template('if-else.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/if-else.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf =  'if-else.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))


'''循环中的过滤（if 配合 for）'''
template = env.get_template('if_for.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/if_for.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))