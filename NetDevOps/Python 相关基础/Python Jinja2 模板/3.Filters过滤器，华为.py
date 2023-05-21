'''
在Jinja2中，我们可以使用过滤器（Filters）来调整变量。过滤器和变量之间使用管道符（|）隔开，其使用很灵活
'''
from jinja2 import Environment, FileSystemLoader
import yaml

'''default（常规)'''
env = Environment(
    loader=FileSystemLoader('./templates'),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template('filters_defult0.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/filters_defult0.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''
default（带空值）
缺省情况下，如果一变量有定义但其值为空，jinja2也会直接使用空值，而不会使用默认值。
换句话说，缺省情况下，变量只要在yaml中有定义，就与jinja2模板中的默认值无关
'''
template = env.get_template('filters_defult_none.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/filters_defult_none.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))
# area
#   network 10.0.1.0 0.0.0.255
#   quit

'''
default（带空值，boolean=true）
能不能把空值当成没定义呢？Jinja2模板需要来多一个参数，boolean=true
'''
template = env.get_template('filters_defult_boolean.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/filters_defult_boolean.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''
dictsort
过滤器dictsort允许我们按字典进行排序。缺省情况下，dictsort按键排序，也可以通过参数改为按值排序
dictsort(value, case_sensitive=False, by='key')
过滤器dictsort处理以后，其返回的是一个元组列表，而非字典
'''
template = env.get_template('filters_dictsort.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/filters_dictsort.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = 'filters_dictsort.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))

'''
join
过滤器join的用法和python中的join的用法非常类似。通过它，您可以用特定的字符来连接一个序列的元组
'''
template = env.get_template('filters_join.jinja2')
#print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open('yaml_data/filters_join.yaml') as f:
    vars_dict = yaml.safe_load(f)

# 开始渲染，生成对应脚本并命名。
for sw in vars_dict:
    print(sw)
    #swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = 'filters_join.txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))
