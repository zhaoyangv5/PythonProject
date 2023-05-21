'''
Jinja2不仅仅是Python独有，Jinja2也不仅仅是个模板语言。我们一起来慢慢学习，先看看它的日常应用场景：

作为生成HTML页面的模板
作为生成Unix/Linux系统中配置文件的模板
作为生成网络设备配置文件的模板（或脚本）

为S系列交换机的配置，然后在特定位置上，用{{xx}}替换一些特性数据。这便是一个Jinja2模板模板了。
sysname {{name}}
观察上述模板特征，我们梳理一下：

Jinja中，双花括符内为变量。
执行脚本的时候，这些位置变量将变真实的数据所替换。
使用这个模板，我们就能通过替换一组变量的形式来为不同的设备制作不同的配置脚本
'''

'''
实验目的
假设实验拓扑中的设备为初始状态，还没有相关配置。

YAML文件配合Jinja2模板，生成配置脚本。（本文重点）
生成的配置脚本手工刷入对应设备。（联机也行，非本文重点。）
'''

from jinja2 import Environment, FileSystemLoader
import yaml


# FileSystemLoader： 文件系统加载器
# 指定jinja2模板存在哪个具体位置。
# 此例中，模板在文件目录中。
# Environment ：环境参数描述类
# 此例中，我们只指定了加载器（Loader），其实还可以指定如何处理模板.

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('sw_template.jinja2')

with open('yaml_data/sw_info.yaml') as f:
    sws = yaml.safe_load(f)

    print(sws)
    print(type(sws))
for sw in sws:
    swx_conf = sw['name'] + 'txt'
    with open(f'results/{swx_conf}', 'w') as f:
        f.write(template.render(sw))