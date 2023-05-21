"""
nornir_jinja2有两个task函数：

template_file，通过jinja2的模板文件来渲染
tempalte_string，通过jinja2的字符串模板来渲染
"""
"""
template_file

我们先来看一下template_file，方法还是观察其docstring的文档说明。其模块路径为nornir_jinja2.plugins.tasks.template_file

从task函数的源代码中我们可以读取到docstring，得知其参数及其使用方法：

template，模板文件的路径。
path，模板所在目录路径，建议使用绝对路径。
jinja_filters，jinja2的过滤器，可选参数，类型是字典，key为过滤器名称，value为过滤器函数。
jinja_env，jinja2的环境对象，可选参数，默认值为空，我们也可以利用以前的代码传入我们构建的jinja2环境。
kwargs，模板渲染所需的数据。
"""
import re

from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result

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


filters = {}
filters['interface_name_format'] = interface_name_filter
template_dir_path = 'jinja2_templates'
template = 'interface_with_filters.j2'

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=template_file,
                 template=template,
                 path=template_dir_path,
                 jinja_filters=filters,
                 interface_name='eth1/1')

print_result(results)


"""tempalte_string

template_string是通过jinja2模板的内容（字符串）来进行渲染模板的一个task函数，它的使用与template_file有两点区别：

template参数代表是jinja2模板的内容的字符串，而不再是模板的路径。
无需path参数。
"""

import re

from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_string
from nornir_utils.plugins.functions import print_result

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


filters = {}
filters['interface_name_format'] = interface_name_filter
# 此处是模板内容的字符串，而不再是路径，我们刻意通过变量名着重突出
template_content = '{{ interface_name|interface_name_format() }}'

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=template_string,
                 template=template_content,
                 jinja_filters=filters,
                 interface_name='eth1/1')

print_result(results)