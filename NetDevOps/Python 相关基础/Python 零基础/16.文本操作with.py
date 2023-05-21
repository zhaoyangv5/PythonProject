'''
在我们自己编写的代码体系里一定要用utf8字符集
读取别人的文本的时候选择utf8字符集另存为一个新文件供程序使用，后续讨论不再赘述其他字符集
一定要用上下文管理关键字with来打开文件对象
一定要显式的赋值读写的模式以及字符集名称

'r'，以只读模式打开，默认模式。
'r+'，打开文件进行读写。
'w'，以写入模式打开，此时读取不了，只能写入。
    如果这文件已存在，则会删掉原先的文件内容。
    如果这个文件不存在，则会新创建一个。
'w+'，打开文件进行读写。
    如果这文件已存在，则会删掉原先的文件内容。
    如果这个文件不存在，则会新创建一个。
'a'，打开文件，并在文末追加数据。
'a+'，打开文件进行读写，写的内容追加在文末。

read - 将文件内容读取到字符串中（一次性操作）
readline - 按行读取文件（一行一行读，分布操作）
readlines - 读取所有行，按行形成一个列表（一次性操作）

'''
'''
对文件操作我们使用open函数创建一个文件对象，实际上是一个句柄指向了操作系统的文件对象，我们执行read方法，
可以对文本文件进行读取内容的操作，返回一个字符串。在操作完成后，我们需要关闭文件句柄（调用文件对象的close方法），以防止读写冲突之类的事情放生。
'''
# 我们用IDE创建一个文件，叫做netdevops.txt，编码采用utf8字符集
#文本的读取
f = open('NetDevOps.txt', mode='r', encoding='utf8')
print(f, type(f))
# 上述会输出<_io.TextIOWrapper name='netdevops.txt' mode='r' encoding='utf8'> <class '_io.TextIOWrapper'>
content = f.read()
print(content)  # 输出我们文件的内容，字符串
f.close()  # 关闭文件对象

print('*'*50)

with open('NetDevOps.txt', mode='r', encoding='utf8') as f:
    content = f.read()
    print(content)  # 输出我们文件的内容，字符串

print('*'*50)

#大文本读取
with open('NetDevOps.txt', mode='r', encoding='utf8') as f:
    for line in f:
        print(line)

with open('NetDevOps.txt', mode='r', encoding='utf8') as f:
    wenben = f.readlines()
    print(wenben[0].strip())

with open('sw1.txt', mode='r', encoding='utf8') as f:
    for line in f:
        # print(line)       #直接打印会出现空行
        # print(line.strip())       #第一种方法：strip去除空行
        # print(line, end=' ')      #第二种方法：end=''
        print(f.read())             #第三中方法：read一次性读取



#文本的写入
with open('netdevops_w.txt', mode='w', encoding='utf8') as f:
    content = '''this is a book about “NetDevOps”!
这是一本关于NetDevOps的书！'''
    f.write(content)

#write方法负责将字符串写入到指定的文本文件中，若文本不存在则创建，若文件存在w模式会覆盖，a模式会追加。
#以上代码会创建一个netdevops_w.txt的文本文件

#seek
#因为 read 和 readlines 操作后，文件的光标已经移到文末了，于是后面再次读就出现了空字符串的情况了。前面也提到了指针的移动可以用方法 seek 来辅助
#seek(0)                    # 我们把指针做一个调整，移到文首（0）位置

'''
with 语法巧用
来个是实战场景，我们有时候必须同时打开两个文件，比如打开A文件，读取信息处理，之后写入B文件
'''
with open('sw1.txt', 'r', encoding='utf8') as src:
    with open('result.txt', 'w', encoding='utf8') as dest:
        for line in src:
            if not line.startswith('#'):
                dest.write(line)