from jinja2 import Environment
from django.template.defaultfilters import date

def environment(**options):

    # 创建Environment实例
    env = Environment(**options)
    # 指定（更新）jinja2的函数指向Django的指定过滤器
    env.globals.update(
        {
            "date": date,
        }
    )
    # 返回Environment实例
    return env