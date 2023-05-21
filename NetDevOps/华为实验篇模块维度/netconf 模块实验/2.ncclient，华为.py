

from ncclient import manager
from lxml import etree

m = manager.connect(host='192.168.31.100',
                    port=830,
                    username='netconf',
                    password='Admin@1234',
                    hostkey_verify=False,
                    device_params={'name':'huawei'},
                    timeout=300)

print(m.server_capabilities)

# for capability in m.server_capabilities:
#     print(capability)

"""get_config() - 全量提取"""
running_config = m.get_config('running')
# print(running_config)



"""get_config() - 过滤提取"""
FILTER ='''
<filter>
    <system xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0">
        <systemInfo>
            <sysName></sysName>
        </systemInfo>
    </system>
</filter>
'''
filtered = m.get_config('running', FILTER)
# print(filtered)
# print(type(filtered))

hostname = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}sysName')
# print(hostname.text)


"""get_config() - 取单接口多信息"""
FILTER = """
    <filter>
      <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <interfaces>
          <interface>
            <ifName>GE1/0/5</ifName>
            <ifDescr></ifDescr>
          <ipv4Config>
            <am4CfgAddrs>
              <am4CfgAddr>
                <ifIpAddr></ifIpAddr>
                <subnetMask></subnetMask>
                <addrType>main</addrType>
              </am4CfgAddr>
            </am4CfgAddrs>
          </ipv4Config>                
          </interface>
        </interfaces>
      </ifm>
    </filter>"""

FILTER1 = """
    <filter>
      <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <interfaces>
          <interface>
          <ifName>GE1/0/5</ifName>
          </interface>
        </interfaces>
      </ifm>
    </filter>"""

# filtered = m.get_config('running', FILTER)
filtered = m.get_config('running', FILTER1)
ip = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}ifIpAddr')
ifDescr = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}ifDescr')
subnetMask = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}subnetMask')
# print(ip, ifDescr, subnetMask)
# print(ip.text, ifDescr.text, subnetMask.text)

"""get_config() - 取多接口单信息"""
FILTER2 = """
    <filter>
      <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <interfaces>
          <interface>
          <ifName></ifName>
          </interface>
        </interfaces>
      </ifm>
    </filter>"""

filtered = m.get_config('running', FILTER2)
# print(filtered)

interface_container = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}interfaces')
print(interface_container)
for ifName in interface_container.iter('{http://www.huawei.com/netconf/vrp}ifName'):   # 放入一个迭代器
        print(ifName.text)


FILTER3 = """
    <filter>
      <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <interfaces>
          <interface>
          <ifName></ifName>
          <ifDescr></ifDescr>
          </interface>
        </interfaces>
      </ifm>
    </filter>"""

filtered = m.get_config('running', FILTER3)
interface_container = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}ifDescr')
# print(filtered)
for ifDescr in interface_container.iter('{http://www.huawei.com/netconf/vrp}ifDescr'):
        print(ifDescr.text)


m = manager.connect(host='192.168.31.100',
                    port=830,
                    username='netconf',
                    password='Admin@1234',
                    hostkey_verify=False,
                    device_params={'name':'huawei'},
                    timeout=300)



interface_container = filtered.data.find('.//{http://www.huawei.com/netconf/vrp}interfaces')

for ifName in interface_container.iter('{http://www.huawei.com/netconf/vrp}ifName'):
    print(ifName.text)

print('\n ==== \n')
for ifIpAddr in interface_container.iter('{http://www.huawei.com/netconf/vrp}ifIpAddr'):
    print(ifIpAddr.text)

print('\n ==== \n')
for ifDescr in interface_container.iter('{http://www.huawei.com/netconf/vrp}ifDescr'):
    print(ifDescr.text)

print('\n ==== \n')
for subnetMask in interface_container.iter('{http://www.huawei.com/netconf/vrp}subnetMask'):
    print(subnetMask.text)


