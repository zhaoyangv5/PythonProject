import re


regex1 = r'(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)'
regex2 = r' +(?P<vlan>\d+)\D+$'

with open('display_arp2.txt') as data:
    for line in data:
        #如果为vlan字段，则追加到result的最后一个元素，然后解析下一行
        match = re.search(regex2, line)
        print(match)