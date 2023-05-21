



#获取目标设备的基本信息

from pyntc import ntc_device as NTC
import json

sw1 = NTC(host='192.168.2.11', username='python',password='123',device_type='cisco_ios_ssh')
sw1.open()                      #完成设备SSH操作



print(json.dumps(sw1.facts(), indent=4))   #facts方法用来获取设备厂商，设备型号，版本，序列号，主机名，端口等基本信息及配置，为了具有可读性，调用json
sw1.close()

#对目标设备进行配置
sw1.config('hostname pyntc_sw1')
sw1.config_list(['router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0'])
sw1.close()

#获取目标设备runing-config
run = sw1.running_config
print(run)
sw1.close()

#对目标设备进行runing-config备份
sw1.backup_running_config('sw1_config.cfg')
sw1.close()

#重启目标设备
sw1.save()
sw1.reboot(confirm=True)  #True表示确认对设备进行重启

