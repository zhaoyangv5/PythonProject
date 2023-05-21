"""
我们在解析模板的第一行定义开始定义Value，可以是多个，每一个Value定义占用一行，Value之间不要有空白行。
Value用来描述要提取信息字段名、此字段的一些可选项、此字段信息的正则表达式。其格式如下：

Value [option[,option...]] name regex
Value开头代表这是一个Value的定义，固定格式。全部的Value定义了我们要提取的所有字段。对应的是字典列表中的一个字典即一个record（记录）。

name是字段名称，对应的是提取信息后（我们之前提到的字典的列表）字典中的key，这个字段名称的定义，一定要符合变量的命名规范，
官网使用了大驼峰命名法（每个单词的首字母），有些人推荐使用全大写，而笔者根据情况也会使用蛇形命名法（主要是受Python变量的书写风格影响的）。
且名称不能是Option中的任意一种。

regex是这个字段必须符合的正则表达式，必须用括号圈起来正则，在学习了正则表达式的相关知识后，我们就知道，这其实是一个子模式在其中我们也可以继续用子模式，
但最终提取的信息是最外侧的子模式。正则表达式一般使用粗颗粒度的即可，因为受到上下文的约束，这种颗粒度是可以满足需求的。如果涉及到一些特殊字符，一定要进行转义。

option是一些关于字段可选项，可选项可以对提取的字段进行一些约束或者声明。可选项可以为空也可以是多个，多个的时候之间用逗号隔开。

可选项	         说明
Required	代表此字段必须识别捕获到。一个record才会被认为有效，然后记录，反之则会被丢弃
List	    这个字段是列表值，比如allow vlan等 port-channel member等字段
Filldown	如果本条record这个字段的值未被识别，用前一条record对应字段的值来填充本条记录这个字段的值
Key	        每条记录的这个字段作为唯一标识
Fillup	    Filldown的逆操作，如果本条record这个字段的值未被识别，用下一条record对应字段的值来填充本条记录这个字段的值
Option是可以叠加的，我们只需要用逗号隔开即可。

Option可选项本身并不常用，笔者写的80%甚至90%的解析模板中，可能都未使用这些可选项，笔者认为大家了解Required、List、Filldown，这些可能还有10%—20%的可能使用。

Key是官方文档中做了说明，但是并未做任何实现，即我们目前看来它可能只是起到了官方文档中声明（declare）唯一标识的作用，并未起到真正约束的作用，我们识别多条record记录，它们的某个声明了Key的Value仍然可以重复。

Fillup在网络配置解析中极其少遇到，在另外一个有着400左右解析模板库中，可能只有1个用了Fillwup。

以上是Value的基本定义，我们一定要注意，一个Value定义中，一定用且只用一个空格隔开Value、option、name、regex。option之间用且只用一个逗号隔开。

所有定义了的Value，出于各种原因如果识别不到，且没有使用Filldown、Fillup等Option，TextFSM将其置为空字符串（注意是空字符串，而不是None）。

比如我们通过对华为交换机的display interface brief输出进行解析，我们确定了要提取的字段，定义好Value即可。我们先观察一下display interface brief的文本

PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(e): ETHOAM down
(d): Dampening Suppressed
(p): port alarm down
(dl): DLDP down
(c): CFM down
InUti/OutUti: input utility rate/output utility rate
Interface                  PHY      Protocol  InUti OutUti   inErrors  outErrors
GE1/0/0                    up       up           0%     0%          0          0
GE1/0/1                    up       up           0%     0%          0          0
GE1/0/2                    up       up           0%     0%          0          0
GE1/0/3                    up       up           0%     0%          0          0
GE1/0/4                    up       up           0%     0%          0          0
GE1/0/5                    up       up           0%     0%          0          0
GE1/0/6                    up       up           0%     0%          0          0
GE1/0/7                    up       up           0%     0%          0          0
GE1/0/8                    up       up           0%     0%          0          0
GE1/0/9                    *down    down         0%     0%          0          0
MEth0/0/0                  up       up           0%     0%          0          0
NULL0                      up       up(s)        0%     0%          0          0
我们要提取的就是这段输出的表头信息，按照Value [option[,option...]] name regex格式进行定义编写即可。

Value Name (\S+)
Value PhyState (\S+)
Value ProtocolState (\S+)
Value InUti (\S+)
Value OutUti (\S+)
Value InErrors (\S+)
Value OutErrors (\S+)
这里面的字段都无需添加option可选项，命名方法我们参考了官方的命名方法，使用了大驼峰。
"""