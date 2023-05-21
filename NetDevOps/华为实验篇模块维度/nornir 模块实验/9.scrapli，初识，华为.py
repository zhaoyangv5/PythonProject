'''
根据作者自己的介绍，Scrapli是一个专注于向网络设备（不支持主机）提供SSH、Telnet协议应用的Python第三方库。
是的，你没听错，这是一个继Paramiko, Netmiko, Telnetlib, Pexpect等等模块之后老外重复造的又一个SSH/Telnet轮子，
既然是重复造的轮子又能在短时间内受到青睐并被Nornir3纳入其插件库，Scrapli必有其过人之处
'''

from scrapli import Scrapli

my_device = {
    "host":  "192.168.31.100",
    "auth_username": "python",
    "auth_password": "Admin@123",
    "auth_strict_key": False,
    "platform": "huawei_vrp",
    "ssh_config_file": "ssh_config"
}

conn = Scrapli(**my_device)
conn.open()

responses = conn.send_commands(["dis clock", "dis ip int brief"])
print(responses)
for response in responses:
    print(response.result)
conn.close()

#Scrapli 给设备下发配置
conn = Scrapli(**my_device)
conn.open()

output = conn.send_configs(["interface Ge 1/0/0", "description Configured by Scrapli"])
print(output.result)
output = conn.send_command("display interface description GigabitEthernet 0/0/1")
print(output.result)
conn.close()