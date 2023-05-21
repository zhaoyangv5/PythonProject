from napalm import get_network_driver
import json

#get类获取设备信息

driver = get_network_driver('ios')
sw1 = driver('192.168.2.11', 'python', '123')
sw1.open()

ouput = sw1.get_arp_table()
print(json.dumps(ouput))

#config类应用
#config类实际就是给设备做配置，需要先创建.cfg文件
#例如 napalm_config.cfg
#line vty 5 15
#transport in ssh
#transport out ssh
#login local

sw1.load_merge_candidate(filename='napalm_config.cfg')  #加载创建好的文件
sw1.commit_config()                         #执行命令

#config类的对比

differences = sw1.compare_config()
if len(differences)> 0:
    print(differences)
    sw1.commit_config()
else:
    print('no changes needed')
    sw1.discard_config()  #如果对比结果一样，则放弃通过sw1.load_merge_candidate(filename='napalm_config.cfg')对文件的加载


