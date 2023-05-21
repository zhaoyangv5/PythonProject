"""
状态State内进行Rule的定义，每个状态由1个及以上Rule组成。EOF和End中不允许定义Rule。

TextFSM会从配置文本中逐行读取文本，并将文本与当前状态的每一行的Rule进行匹配：

如果匹配成功，会执行当前Rule中定义的相关Action（比如进行记录或者状态转移），然后读取下一行从当前状态的第一个Rule继续循环匹配，
某种特殊情况下，我们可以继续使用当前行。
如果匹配失败，会将当前行文本与下一个Rule继续进行匹配。
Rule的书写格式如下：

^regex [-> action]
左侧的是Rule中的正则表达式，右侧的Action实现相关动作，是可选项，他通过“->”连接，且要注意，这个连接符号的左右各有一个空格，且只有这一个空格。

Rule正则表达式的编写

regex即正则表达式，用来与当前文本行进行识别匹配。这种匹配行为是从文本行的开头去匹配的，虽然底层使用了re.match的方法，
但是出于书写规则有一定区分度，会强制我们写一个“^”的正则表达式中代表文本开头的元字符。

正则表达式中可以有零个或者多个在解析模板定义的Value标识，零个的使用场景是为了找到有特征的一些文本行，
为下一步进行准备的，很多情况下都是有相关Value的标识。Value的标识书写规则为"${ValueName}"或者"$ValueName"，
其中ValueName代表的是Value中字段的名称即name，格式上一般使用"${ValueName}"。
这种Value定义中的regex正则表达式部分在实际底层使用中会被展开成子模式，放入到rule中的标识符位置，TextFSM会去匹配每行，
如果有Value标识符且本行匹配到，则将子模式提取的整体放放入当前识别记录的指定字段。在rule中如果要表示文本行结尾话，正则表达式需要使用“$$”，
而不是正则表达式的“$”元字符，主要是Value标识中的“$”区别开。

比如我们之前的软件版本解析模板：

Value version (\S+)

Start
 ^VRP \(R\) software, Version ${version} -> Record
模板中唯一一条Rule，将${version}替换为(\S+)后结果为：

^VRP \(R\) software, Version (\S+)
Text FSM底层会用这个正则表达式去匹配每行，在对应行“VRP (R) software, Version 8.180 (CE6800 V200R005C10SPC607B607)”匹配到后，将“8.180 ”赋值给“version”字段。

一个Rule中可以有多个Value。比如我们之前定义的端口简表的Value，我们可以写一条Rule用于匹配识别相关信息：

^${Name}\s+${PhyState}\s+${ProtocolState}\s+${InUti}\s+${OutUti}\s+${InErrors}\s+${OutErrors}
当然这条Rule并不完整，因为它还缺少一些Action，让状态机更加“灵动”。

Rule action详解

编写完Rule内正则表达式部分之后，在一些关键的Rule中我们还需要添加一些Action，实现诸如信息的记录、状态的转移，甚至还可以继续使用当前文本行进行一些相关处理、主动抛出错误等等。

我们通过"->"来连接rule中的正则表达式与Action，Action的格式为"LineAction.RecordAction StateTransitionAction"。

它们的主要作用如下：

Action	说明
LineAction	    对读取文本逻辑进行控制，决定是读取下一行文本，还是仍使用当前行文本
RecordAction	对提取识别到的信息进行控制，决定是不做记录、进行记录、清空值等
StateTransitionAction	进行状态转移
这三种Action可以组合使用，也可以单独使用，根据实际情况来进行安排。LineAction、RecordAction 是有默认值，即代表我们可以不写，
所以实际使用中上述格式可能是Action部分为空，而这些TextFSM都可以自动识别到。

LineAction

当我们讨论LineAction的时候，有一个大前提，是指当前文本行匹配到了这条Rule。

LineAction是指对文本行的相关动作，取值有两种：

Next，这个是默认值，当rule后面没有LineAction的话，LineAction实际采用了Next这个值。
它会结束当前行文本，读取新的一行文本，并在State中从头开始再去循环每条Rule进行匹配，这个State要具体结合StateTransitionAction来看，
如果无状态转移，默认是在当前状态进行，如果有了状态转移，则会去新的状态中进行。

Continue，它会保留当前行的文本，继续使用当前文本行，在当前状态中继续下一个Rule的匹配。
请注意Continue不能和状态转移StateTransitionAction结合使用，这样可能会导致死循环，所以TextFSM会进行相关检查，如果出现了则会报错提示给用户。
它的使用场景非常多，后续我们会结合示例展开来分析。
RecordAction

RecordAction是针对当前识别到的信息进行的相关处理，我们每条Rule中都可能提取到某个字段的信息，这些放到一条record中，record官方也称row，
笔者之前提过的包含字段信息的字典。通过整个状态机会有一个待返回给用户的列表，我们针对这条记录可以有以下几种操作：

NoRecord：默认值，识别提取信息后，不做任何操作。
Record： 很重要的一个动作，将当前的所提取的所有字段，打包成一个字典追加到返回的列表中。其中Value中没标记Filldown可选项的字段被清理掉。如果required的字段没有找到，此条record不会追加到返回列表中。
Clear：清理Value中定义的非Filldown的字段值
Clearall：清理所有的字段的值
在实际使用中，我们一般只会显式调用Record，在适当的Rule中，确定有关字段信息已经收集完整进行相关保存，将record追加到待返回给用户的列表中。

由于以上两种Action都有默认值，“LineAction.RecordAction StateTransitionAction”中相关位置不填即会补充为默认值Next和NoRecord。

之前的软件版本解析模板：

Value version (\S+)

Start
 ^VRP \(R\) software, Version ${version} -> Record
这里面通过“->”我们会发现它有Action，LineAction默认取Next，即当文本挪到下一行，RecordAction为Record，即将当前识别的信息追加到列表中。

StateTransitionAction

StateTransitionAction是代表状态转移的Action，是可选项，在需要进行状态转移的地方添加此Action，
我们直接写要跳转的、定义好的或者是之前提到的保留状态（Start、EOF）。
如果前面有LineAction或者RecordAction要添加一个空格。在当前Rule与当前文本匹配后，如果有RecordAction，则先执行RecordAction，再执行状态转移Action。
状态转移Action与Continue无法同时使用，因为这可能引起一个死循环，我们有可能一直用当前文本行在在不同的状态间转来转去。

绝大部分的解析模板都只写一个Start就可以轻松捕获到相关信息，当文本读取到最后一行转移到EOF状态。

ErrorAction

除了以上三种Action，实际上还有一种隐藏的Action——ErrorAction，这个Action会终止当前的一切行为，不返回任何数据（即使已经识别到的），同时抛出一个异常Exception。其语法规则如下：

^regex -> Error [word|"string"]
后面的异常信息是可选的，如果填写异常信息用于提示给用户。请注意，如果提示信息是多个单词，即中间有空格之类的，一定要用双引号给引起来，如果只是单词，可以不引起来。
"""