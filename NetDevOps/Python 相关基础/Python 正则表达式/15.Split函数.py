import re

# 第 1 步，体验字符串split与正则split函数的相似之处
arp_record = '172.29.50.150   4c1f-ccb4-5157            I -  Vlanif41'

print(re.split(r' ', arp_record))
print(arp_record.split(r' '))
#如字符间出现多个空格，我们又以单个空格作为分割条件，就会出现空格分割空格的情况，从而出现很多空字符串

#第 2 步，split函数分割项正则化
print(re.split(r' +', arp_record))      #把正则split函数的分割符参数改成正则模式，使其匹配一个或多个空格

#第 3 步，体验参数maxsplit
#参数maxsplit=2表示匹配空格，分割2次后就停了，源字符往后剩余的字符串就不再处理，当成返回列表的最后一项一并返回。
#默认情况下，参数maxsplit=0，表示能分割多少次就分割多少次
print(re.split(r' +', arp_record, maxsplit=2))      #['172.29.50.150', '4c1f-ccb4-5157', 'I -  Vlanif41']

#第 4 步，不设置捕获组
#'I - Vlanif41'这一项还是有点不伦不类，需要进一步处理下，我们再继续优化调整
print(re.split(r'((I -)| )+', arp_record))

'''
+I - +	空格一个或多个，接着I -，接着空格一个或多个
+	空格一个或多个
'''
print(re.split(r' +I - +| +', arp_record))

#第 5 步，设置捕获组
print(re.split(r'((I -)| )+', arp_record))
print(re.split(r'(?:(?:I -)| )+', arp_record))
#我们的思路源字符串不是被'I -'分割就是被空格分割。我们用小括号()来辅助我们匹配思路，
#但这过程中因为小括号有捕获组的概念，所以会惹来些空匹配项。不过我们用?:即可轻松地取消捕获功能
