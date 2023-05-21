"""
用python最基础的语法，大概涉及变量、字符串、分支判断、文件读取、while循环等。

（1）读取配置文件中info-center的源IP地址10.10.10.10，放入变量info_center_ip中；

（2）读取配置文件中LoopBack0口的IP地址10.10.10.10，放入变量inter_loop0_ip中；

（3）比较info_center_ip与inter_loop0_ip两变量是否一致。

"""
"""读取info-center源IP地址"""
# 定义一个变量，等下来放info-center源IP地址，本例目标值是10.10.10.10
info_center_ip = ''

# 打开demo.txt文件代码块，包括open和close
f = open('demo.txt')
found = 0 # 设置一个标识位，1为找到，0为未找到，用于控制while循环

# 进入循环体，开始读取demo.txt
while found==0:
    line = f.readline() #逐行读取，赋值给line
    # 对读取的内容进行判断，以“info-center……”开头，则进入分支
    if line.startswith('info-center loghost 192.168.10.1 source-ip'):
        info_center_ip = line.split()[-1]
        found = 1 # 找到了，修改标志位，跳出循环
        print(info_center_ip) # 调测使用

f.close()

# 1、open()、close()要组合使用。因为用with处理文件打开的话，又得增加缩进，对初学者不是很友好。
# 2、标识变量found经常与while配合使用，用于控制while循环的结束。
# 3、.startswith()是字符串的一个方法，判断是否以某个具体的字符串开头，这里取“info-center loghost 192.168.10.1 source-ip”尽量精确，
#    因为一台设备可能配了多条info-center。（关于多条的怎么处理，后续可再讨论，为控制篇幅，本实验暂不涉及。）
# 4、.split()是字符串的一个方法，对字符串进行“断句”，默认以空格作为分割，分割完以后放入列表中。
# 5、.split()[-1]中的[-1]是对字符串分割后的列表进行定位索引，如下表。
# info-center	loghost	   192.168.10.1	    source-ip	10.10.10.10
# （正序）0	       1	        2	            3	         4
# （倒序）-5	      -4	       -3	           -2	        -1


"""读取LoopBack0口IP地址"""

# 定义一个变量，等下来放LoopBack0口IP地址，本例目标值是10.10.10.10
inter_loop0_ip = ''

# 打开demo.txt文件代码块，包括open和close
f = open('demo.txt')
found = 0 # 设置一个标识位，1为找到，0为未找到，用于控制while循环

while found==0:
    line = f.readline()
    if line.startswith('interface LoopBack0'):
        line = f.readline()
        while line.startswith(' '):
            if line.startswith(' ip address '):
                inter_loop0_ip = line.split()[-2]
                found = 1
                print(inter_loop0_ip)
                #break #配合break则找到了就退出，否则需读完LoopBack0接口下全部配置再退出。
            line = f.readline()
f.close()

"""判断两变量是否一致"""

if info_center_ip==inter_loop0_ip:
    print(f"核查无误，均为{info_center_ip}")
else:print(f"核查有误！！！\
           \ninfo_center_ip：{info_center_ip}\
           \ninter_loop0_ip：{inter_loop0_ip}")