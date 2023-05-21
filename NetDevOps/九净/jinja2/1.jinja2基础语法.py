'''
在讲解jinja2语法的时候，为了便捷直观，我们先暂时将模板与代码耦合在一起，后面我们会慢慢讲解一些高阶用法，
将模板与代码剥离，甚至将数据与代码剥离。

jinja2是一种模板引擎，类似于其他的Web模板系统，它也支持变量的定义、判断、循环这些最基础的语法，
我们先从基础的语法讲起，结合使用场景遇到的问题，我们再会讲解一下空白符的控制和注释的编写
'''

"""变量"""
from jinja2 import Template


# 通过字符串定义了一个模板，有两个变量——“name”和“desc”。调用Template类进行初始化，
# 可以通过字符串赋值给第一个参数source（代码中省略）加载出一个模板对象。
# Template实例化后的对象有一个render（渲染）的方法，它可以接受可变参数，简单理解就是我们在模板定义的变量，在这里都可以进行赋值
templ_str="""interface {{ name }} 
 description {{ desc }}
 undo shutdown
"""
templ = Template(templ_str)
result = templ.render(name='Eth1/1', desc='gen by jinja2')
print(result)


# 赋值可以是任何Python数据类型，比如字符串、数字、字典、列表等，包括自定义的对象，但最终都会被jinja2以类似强制转为str类型渲染到指定位置
templ_str = """我们可以传入数字，传入的数字为：{{ my_num }}，
我们可以传入字典，传入的字典为：{{ my_dict }},
我们可以传入列表，传入的列表为：{{ my_list }},
"""
templ = Template(templ_str)
result = templ.render(my_num=100,
                      my_dict={'course': 'NetDevOps'},
                      my_list=['1', 2, {"course": "NetDevOps"}]
                      )
print(result)
# 我们可以传入数字，传入的数字为：100，
# 我们可以传入字典，传入的字典为：{'course': 'NetDevOps'},
# 我们可以传入列表，传入的列表为：['1', 2, {'course': 'NetDevOps'}]

# 同时字典和列表还可以保留原有的访问方式，在模板中直接取其成员的值
templ_str = """访问传入字典的成员值：{{ my_dict['course'] }},
访问传入的列表的成员值：{{ my_list[2] }},
"""
templ = Template(templ_str)
result = templ.render(my_num=100,
                      my_dict={'course': 'NetDevOps'},
                      my_list=['1', 2, {"course": "NetDevOps"}]
                      )
print(result)
# 访问传入字典的成员值：NetDevOps,
# 访问传入的列表的成员值：{'course': 'NetDevOps'}
print('='*25 + '判断' + '='*25)
"""判断"""
templ_str = """interface {{ name }}
 description {{ desc }}
{% if shutdown=='yes' %}
shutdown
{% elif shutdown=='no' %}
undo shutdown
{% else %}
请人工确认端口状态配置
{% endif %}"""

templ = Template(templ_str)
result = templ.render(name='Eth1/1', desc='gen by jinja2', shutdown=' ')
print(result)

print('='*25 + '空白控制 -%' + '='*25)

"""空白控制 -%"""
# 空白行来自于条件成立时的“{% elif shutdown=='no' %}”，在模板中控制结构后面还有一个换行符，当此条件成立时后面的换行符则会保留
# 最简单的方式是使用空白控制，即在控制符的内侧添加减号，它会去除所属控制符左侧或者右侧的紧邻它的所有连续的空白符。
# 如果放在左侧的控制符，则去除左侧的所有空白符，如果放在右侧的控制符则去除右侧的所有空白符
templ_str = """interface {{ name }}
 description {{ desc }}
{% if shutdown=='yes' -%}

  shutdown
{% elif shutdown=='no' -%}
undo shutdown
{% else -%}
请人工确认端口状态配置
{% endif -%}"""

templ = Template(templ_str)
result = templ.render(name='Eth1/1', desc='gen by jinja2', shutdown='yes')
print(result)

print('='*25 + '循环' + '='*25)

"""循环"""
#inja2的循环也是一种逻辑控制，循环标签是for，同时需要加上控制符。用法上也类似Python的for循环
templ_str = """{% for i in data_in_list -%}
列表数据中包含：{{ i }}
{% endfor %}"""

templ = Template(templ_str)
result = templ.render(data_in_list=[1,2,3])
print(result)

# 对迭代产生的局部变量，我们可以取其属性或者使用其一些方法
# 对于字典取值，我们可以直接用Python中字典的取值方式取值，也可以使用类似对象的属性访问方法（用点加字段名称），这种可读性好，编写简单
templ_str = """{% for intf in data -%}
interface {{ intf['name'] }}
 description {{ intf.desc }}
{% if intf.shutdown=='yes' -%}
shutdown
{% elif intf.shutdown=='no' -%}
undo shutdown
{% else -%}
请人工确认端口状态配置
{% endif -%}
{% endfor -%}"""

templ = Template(templ_str)
data = [{'name': 'Eth1/1', 'desc': 'gen by jinja2', 'shutdown': 'yes'},
        {'name': 'Eth1/2', 'desc': 'gen by jinja2', 'shutdown': 'no'}]
result = templ.render(data=data)
print(result)

print('='*25 + '通过文件系统加载模板' + '='*25)

"""
通过文件系统加载模板

这就涉及到了两个非常重要的类Environment和FileSystemLoader。
Environment是jinja2最核心的概念之一，当我们简单使用jinja2的时候我们对此无感知，
但是当我们想比较成体系的组织我们的jinja2模板时就需要使用Environment了。Environment里包含非常重要的一些共享的变量，
诸如配置、过滤器、全局变量等，当我们将这些赋值实例化的时候，会加载出一个特定的Environment对象，用于处理我们的模板渲染。
Environment实例化的时候需要加载我们的所有模板，涉及到一个参数加载器loader。
jinja2内置了几种模板的加载器，比如FileSystemLoader可以通过文件目录加载模板，PackageLoader可以从Python包加载模板。
笔者推荐大家使用FileSystemLoader，我们仅需指定目录就可以构造一个加载器。
"""

from jinja2 import Environment, FileSystemLoader

# 通过目录创建加载器
loader = FileSystemLoader("jinja2_templates")
# 通过文件系统加载器创建环境
env = Environment(loader=loader)
# 获取指定jinja2模板文件
template = env.get_template("jinja2_demo.j2")

data = [{'name': 'Eth1/1', 'desc': 'gen by jinja2', 'shutdown': 'yes'},
        {'name': 'Eth1/2', 'desc': 'gen by jinja2', 'shutdown': 'no'}]
result = template.render(data=data)
print(result)


print('='*25 + '通过文件承载渲染所需的数据' + '='*25)

"""通过文件承载渲染所需的数据"""
from jinja2 import Environment, FileSystemLoader
import pandas as pd


# get_jinja2_templ从指定的目录中的模板文件名称在家一个jinja2的模板对象。
# get_data_from_excel从指定表格文件加载出数据，以字典的列表形式返回给调用方

def get_jinja2_templ(templ, dir='jinja2_templates'):
    # 通过目录创建加载器
    loader = FileSystemLoader(dir)
    # 通过文件系统加载器创建环境
    env = Environment(loader=loader)
    # 获取指定jinja2模板文件
    template = env.get_template(templ)
    return template


def get_data_from_excel(file='data.xlsx'):
    df = pd.read_excel(file)
    data = df.to_dict(orient='records')
    return data


if __name__ == '__main__':
    template = get_jinja2_templ(templ='jinja2_demo.j2')
    data = get_data_from_excel()
    result = template.render(data=data)
    print(result)


print('='*25 + '模板的组合' + '='*25)

"""模板的组合"""
#我们可以考虑将模板拆解成比较小的原子模块，然后使用jinja2的include语法对模板进行组合
"""
我们来演示两个模板文件组合生成一个新的模板文件
这是第一个模板文件A.j2渲染的文本
{% include 'A.j2' %}
这是第二个模板文件B.j2渲染的文本
{% include 'B.j2' %}
"""
from jinja2 import Environment, FileSystemLoader
import pandas as pd


def get_jinja2_templ(templ, dir='jinja2_templates'):
    # 通过目录创建加载器
    loader = FileSystemLoader(dir)
    # 通过文件系统加载器创建环境
    env = Environment(loader=loader)
    # 获取指定jinja2模板文件
    template = env.get_template(templ)
    return template


# def get_complex_data_from_excel(file='data.xlsx'):
#     data = {}
#     df_dict = pd.read_excel(file, sheet_name=None)
#     for i in df_dict:
#         data[i] = df_dict[i].to_dict(orient='records')
#     return data
data = {
        'hostname': [{'hostname': 'netdevops'}],
        'ntp': [{'ip': '192.168.137.1'}],
        'syslog': [{'level': 'debugging',
                    'source_intf': 'vlanif15',
                    'loghost': '192.168.137.10',
                    }],
        'interface': [{'name': 'Eth1/1',
                       'desc': 'gen by jinja2',
                       'shutdown': 'yes'},
                      {'name': 'Eth1/2',
                       'desc': 'gen by jinja2',
                       'shutdown': 'no'}]
    }

if __name__ == '__main__':
    # data = get_complex_data_from_excel()
    template = get_jinja2_templ(templ='huawei/my_include_demo.j2')
    result = template.render(data=data)
    print(result)


print('='*25 + '过滤器及其定制化' + '='*25)

"""过滤器及其定制化"""
# 如用户未传入或者传入的值为空，则会根据default中传入的默认值返回
from jinja2 import Template

templ = Template("Let's study {{ course| default('NetDevOps') }} now!")
result = templ.render()
print(result)
# 输出Let's study NetDevOps now!
# 像示例中，我们并未向模板中传入course变量的值，但是由于我们调用了default过滤器，并传入了参数其默认值，所以模板会将默认值赋值给course变量。

# 自定义过滤器本质是一个函数，第一个参数约定俗成为value，对应的是模板中定义的变量，
# 在变量后调用过滤器，会将从外部传入的值在模板中进行相关处理（比如取其成员）后传给对应的过滤器，
# 过滤器可以按需添加其他参数，过滤器内部编写逻辑进行一系列操作，然后返回一个值（可以是字符串、也可以是字典、列表等等）

#写一个对端口进行格式化的过滤器，并加载到环境对象中
from jinja2 import Environment, FileSystemLoader
import re

# from my_filters.format import interface_name_filter

INTF_MAPPING = {
    'eth': 'Ethernet',
    'Eth': 'Ethernet',
}

def interface_name_filter(name):
    intf_re = re.compile('(.+?)(\d+[\d/]*)')
    match = intf_re.match(name)
    if match:
        intf_type = match.group(1)
        intf_no = match.group(2)
        intf_type = INTF_MAPPING.get(intf_type, intf_type)
        return f'{intf_type}{intf_no}'
    return name

def get_jinja2_templ(templ, dir='jinja2_templates'):
    # 通过目录创建加载器
    loader = FileSystemLoader(dir)
    # 通过文件系统加载器创建环境
    env = Environment(loader=loader)
    # 添加自定义过滤器
    env.filters['interface_name_format'] = interface_name_filter
    # 获取指定jinja2模板文件
    template = env.get_template(templ)
    return template


if __name__ == '__main__':
    template = get_jinja2_templ(templ='interface_with_filters.j2')
    result = template.render(interface_name='eth1/1')
    print(result)
