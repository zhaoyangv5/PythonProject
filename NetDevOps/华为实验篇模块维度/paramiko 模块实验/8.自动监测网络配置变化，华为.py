'''
difflib概述
比较两个字符串列表，然后返回一个Differ-style delta（其实是一个生成器generator）

'''

import difflib

with open('config_new.txt') as new_file, open('config_old.txt') as old_file:
    diff = list(difflib.ndiff(old_file.readlines(), new_file.readlines()))
    print(diff)

for line in diff:
    print(line, end='')

#如果config_new.txt和config_old.txt文件完全一致的话，运行的结果如下
 # interface Vlanif1
 #   description Python_G1
 #   ip address 192.168.11.11 255.255.255.0
 #   arp-proxy enable


# 删
# 我们在 config_new.txt 删掉 description Python_G1 会出现如下效果    -  表示删除
#   interface Vlanif1
# -  description Python_G1
#    ip address 192.168.11.11 255.255.255.0
#    arp-proxy enable

# 增
# 所有文件恢复成初始状态。我们在 config_new.txt 增加 ipv6 enable 会出现如下效果    + 表示增加
#   interface Vlanif1
#    description Python_G1
# +  ipv6 enable
#    ip address 192.168.11.11 255.255.255.0
#    arp-proxy enable

# 改短（含长度不变）
# 所有文件恢复成初始状态。我们在 config_new.txt 中的 description Python_G1 改成 description Python_G2 会出现如下效果
# ^指向被修改的位置

#   interface Vlanif1
# -  description Python_G1
# ?                      ^
# +  description Python_G2
# ?                      ^
#    ip address 192.168.11.11 255.255.255.0
#    arp-proxy enable

# 改长
# 所有文件恢复成初始状态。我们在 config_new.txt 中的 192.168.11.11 改成 192.168.111.111 会出现如下效果
#   interface Vlanif1
#    description Python_G1
# -  ip address 192.168.11.11 255.255.255.0
# +  ip address 192.168.111.111 255.255.255.0
# ?                       +   +
#    arp-proxy enable