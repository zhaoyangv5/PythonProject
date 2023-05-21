'''
TextFSM概述

在不支持任何软件接口（API）的网络设备上，通过 CLI 命令返回的是字符串文本。字符串只能说是半结构化数据，
必须处理成其它的Python对象（如字典、列表等），才能方便使用。我们可以利用正则表达式等，对这个返回的字符串逐行读取解析。
燃鹅，我们另外介绍一个神器——TextFSM。TextFSM是谷歌开发的一个用来处理网络设备输出信息的一个库。
它允许你制作模板来处理指令回显。模板对处理套路有沉淀效应，而且很容易分享自己的模板，因此使用TextFSM要比逐行读取解析来得方便太多了。
拿到别人给的模板，等于前人给你造了轮子；分享自己制作的模板，等于你给后人造了轮子
'''

'''
<R1>tracert 192.5.5.5
tracert 192.5.5.5
 traceroute to  192.5.5.5(192.5.5.5), max hops: 30 ,packet length: 40,press CTRL_C to break 
 1 36.1.1.6 60 ms  50 ms  10 ms 
 2 67.1.1.7 100 ms  90 ms  80 ms 
 3 78.1.1.8 90 ms  80 ms  60 ms 
 4 59.1.1.9 100 ms  90 ms  80 ms 
 5 59.1.1.5 90 ms  100 ms  60 ms
'''

'''
1. TextFSM模板变量

Value ID (\d+)
Value Hop (\S+)

Start
  ^ ${ID} ${Hop} +\d+ -> Record

第1行，Value ID (\d+)，Value是关键字，定义1个名叫ID的变量，()小括号里\d+是正则表达式，描述ID的变量是啥结构。
    "\d"表示数字，相当于 [0-9]，+表示前面的\d重复1次或n次。换句话说，\d+可以匹配1,2,3……，也可以匹配123,100000等等，
    但遇到非数字字符的就停下来，比如空格，abc。放在这个traceroute的报文回显例子里，就是匹配路由第几跳。
第2行，Value Hop (\S+)，有了第1行的基础，第2行咱们就熟门熟路了。
    Value是关键字，定义1个名叫Hop的变量，\S是啥？匹配任何非空白字符，相当于 [^ \t\n\r\f\v]，+表示前面的\S重复1次或n次。换句话说，\S+什么非空白的字符都能匹配，
    除了空格、换行等空白字符。放在这个traceroute报文回显例子里，就是匹配路由第几跳的IP地址。

2. TextFSM模板状态

接下来按照语法要求，与变量之间得空一行，一定要空一行，然后来个Start。

我们把TextFSM简单粗暴地叫做“文本有限状态机”。

Start就是一个状态机。大家先这么理解，后面再深入理解。

Start 一下，马上出发！模板正式从这里开始，坐稳了！

^ ${ID} ${Hop} +\d+ -> Record

（1） 对照代码行，解释一下吧！
前面两个空格是固定格式，照抄！
^在正则里面表示一行的开始，这里应该也是吧，照抄！
^和$之间有个空格，是为了匹配" 1 36.1.1.6 60 ms 50 ms 10 ms "中行首的空格，否则一上来就匹配不到了。
${ID}和${Hop}，就是刚才定义的变量，他们中间也有个空格，还是看" 1 36.1.1.6 60 ms 50 ms 10 ms "，${ID}为了匹配1，${Hop}为了匹配36.1.1.6，他们中间存在一个空格。
（2） 再换句话，重新纯文本解释下吧！
【空格】【空格】^【空格】(\d+)【空格】(\S+)【空格(们)】(\d+)【空格】->【空格】Record
${ID}、${Hop}，这两个变量干嘛？就是为了偷偷地在匹配到的文本里面提取了想要的信息，记录起来。【空格(们)】那里我再说一下，它其实是这样" +"，表示一个或者多个空格。
'''

import textfsm

traceroute = '''
<R1>tracert 192.5.5.5
tracert 192.5.5.5
 traceroute to  192.5.5.5(192.5.5.5), max hops: 30 ,packet length: 40,press CTRL_C to break 
 1 36.1.1.6 60 ms  50 ms  10 ms 
 2 67.1.1.7 100 ms  90 ms  80 ms 
 3 78.1.1.8 90 ms  80 ms  60 ms 
 4 59.1.1.9 100 ms  90 ms  80 ms 
 5 59.1.1.5 90 ms  100 ms  60 ms
'''
with open('traceroute.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)
    # result = textfsm.TextFSM(template).ParseText(traceroute)
    print(fsm.header)
    print(result)
