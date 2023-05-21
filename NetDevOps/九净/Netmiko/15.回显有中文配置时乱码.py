'''
这个问题如果要解决，有两种途径，一种是修改配置为英文。另外一种就是要修改代码，修改部分比较多，对新手并不是很友好，不推荐。

Netmiko3.4.0版本读取配置时的字符集无法控制，但是推送配置时的命令如果存在中文，是可以进行控制的，需在初始化连接的时候赋值encoding参数为对应的字符集，
这样发送的命令才会以指定的字符集编码，发送给网络设备。这个参数的赋值同时会影响session_log日志保存时的编码，这点需要大家注意
'''