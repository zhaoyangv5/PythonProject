from netmiko import ConnectHandler

dev = {'device_type': 'huawei',
       'host': '192.168.31.102',
       'username': 'python',
       'password': 'Admin@123',
       'port': 22,
       'session_log': '192.168.31.102.log'
       }

with ConnectHandler(**dev) as conn:
    print("已经成功登陆交换机" + dev['host'])
    # 调用send_config_from_file，赋值config_file为写有我们预下发配置的文本文件即可。
    # 文本文件一定要用utf8的字符集。
    config_output = conn.send_config_from_file(config_file='config.txt')
    print('config_output:')
    print(config_output)
    # save_config,无需赋值，netmiko已经处理好它所支持的厂商型号的保存过程,返回整个交互过程的回显
    save_output = conn.save_config()
    print('save_output:')
    print(save_output)