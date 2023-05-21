"""
nornir_table_inventory是 Nornir的一个Inventory插件，它可以通过表格（csv、Excel）文件来管理nornir的设备清单。
它甚至提供了一种隐藏的方法，可以让你的数据库或者自动化系统作为Nornir的inventory数据源。由于是表格承载，所以只支持扁平化的数据，对于groups和defaults目前不支持

nornir_table_inventory 提供3种 Inventory插件 类 .

CSVInventory 支持通过csv文件进行设备清单管理
ExcelInventory 支持通过Excel（xlsx）文件进行设备清单管理
FlatDataInventory 使用python的列表对象（成员是字典）进行设备清单管理
"""

"""基本使用"""
"""ExcelInventory，CSVInventory"""
#对于表格中的数据，插件是有一定需求的，name、hostname、platform、username、password这些基础属性与yaml文件中的完全一致
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result



runner = {
    "plugin": "threaded",
    "options": {
        "num_workers": 100,
    },
}
# inventory = {
#     "plugin": "ExcelInventory",
#     "options": {
#         "excel_file": "inventory.xlsx",
#     },
inventory = {
    "plugin": "CSVInventory",
    "options": {
        "csv_file": "inventory.csv",
    },
}

nr = InitNornir(runner=runner, inventory=inventory)

# 对于表格中的数据，插件是有一定需求的，name、hostname、platform、username、password这些基础属性与yaml文件中的完全一致。
# 由于笔者对网络工程师而言，推荐使用netmiko，所以我们对应使用了nornir_netmiko这个Python包，底层使用了Netmiko作为connection的插件，
# 基础属性中有一些与设备登录相关的字段，nornir_netmiko插件会自动传入底层的Netmiko的ConnectHandler，一些ConnectHandler需要的其他参数，
# 插件支持以netmiko作为前缀，下划线连接后面变量名的方式透传给ConnectHandler，比如我们想传入一个执行超时时间，ConnectHandler中对应的是timeout参数，
# 我们只需要在表格中定义一个netmiko_timeout参数即可，其他的ConnectHandler的参数也是这种形式，比如提权的密码我们可以使用netmiko_secret。
# 除此以外的任何参数，nornir_table_inventory插件都会将其 作为Host对象的自定义字段，放入其data字段中。我们以一个表格数据作为示例：
#
# name	hostname	platform	port	username	password	city	model	netmiko_timeout	netmiko_secret
# netdevops01	192.168.137.201	cisco_ios	22	netdevops	admin123!	bj	catalyst3750	60	admin1234!
# netdevops02	192.168.137.202	cisco_ios	22	netdevops	admin123!	shanghai	catalyst3750	60	admin1234!

"""将任意数据源作为设备清单"""
# 上述的两种方法都是基于表格数据进行资产清单的加载，实际这两个插件使用了一个共同的资产插件FlatDataInventory。
# 它允许我们通过函数对接到我们的系统，将数据获取后，加工成为字典的列表，进而加载到Nornir当中去。
# 通过这个函数，我们可以使用任意数据源来加载Nornir，可以是数据库、可以是我们自动化系统的api等等。
# 有了它，你就不需要其他的sql或者csv的Nornir插件了。大家可以参考如下代码：

def get_nornir_in_your_way(some_args=None, num_workers=100):
    """Use any way to get some data(such as sql or restful api), and transform them into form as follwing"""
    data = [{'name': 'netdevops01',
             'hostname': '192.168.137.201',
             'platform': 'cisco_ios',
             'port': 22,
             'username': 'netdevops',
             'password': 'admin123!',
             'city': 'bj',
             'model': 'catalyst3750',
             'netmiko_timeout': 180,
             'netmiko_secret': 'admin1234!',
             'netmiko_banner_timeout': '30',
             'netmiko_conn_timeout': '20'},
            {'name': 'netdevops02',
             'hostname': '192.168.137.202',
             'platform': 'cisco_ios',
             'port': 22,
             'username': 'netdevops',
             'password': 'admin123!',
             'city': 'bj',
             'model': 'catalyst3750',
             'netmiko_timeout': 120,
             'netmiko_secret': 'admin1234!',
             'netmiko_banner_timeout': 30,
             'netmiko_conn_timeout': 20}
            ]
    runner = {
        "plugin": "threaded",
        "options": {
            "num_workers": num_workers,
        },
    }
    inventory = {
        "plugin": "FlatDataInventory",
        "options": {
            "data": data,
        },
    }
    nr = InitNornir(runner=runner, inventory=inventory)
    return nr


if __name__ == '__main__':
    nr = get_nornir_in_your_way()
    bj_devs = nr.filter(city='bj')
    r = bj_devs.run(task=netmiko_send_command, command_string='display version')
    print_result(r)
# 封装一个函数get_nornir_in_your_way（此函数名大家可以任意命名），写一段代码用于对接数据库或者是系统平台，将获取的数据按照类似表格中的规范进行转换，
# 当然示例代码中是直接给了一个符合标准的数据，数据标准与表格中的数据标准一致。然后加载Nornir时指定FlatDataInventory插件，
# 将转换后的数据赋值给插件的data字段即可


