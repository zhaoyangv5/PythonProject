
'''
常规 for-else
如果在for循环结构中，该遍历（也叫“迭代”）的元素都处理完了，如若还有else代码块，则执行它。这种结构中，for和else是在一个级别的缩进中
'''
print('*'*20+"\''for-else\''"+'*'*25)

devs = ['router','switch']
for each in devs:
    print(each)
else:
    print("Run out of devs")

print('*'*20+' for-break-else '+'*'*25)

'''
for-break-else
for循环正常结束后，Python会执行else代码块。那我们怎么让循环非正常结束呢？答案就是我们上节课提到的break
'''
devs = ['router','switch']
for each in devs:
    if each == 'router':   # 如果出现'router'，则打印后跳出for循环。
        print(each)
        break
else:
    print("Run out of devs")

print('*'*20+' for-continue-else '+'*'*25)

'''
for-continue-else
如果我们用continue来干预for循环呢，会不会影响else？答案是不会的，该干嘛还干嘛！
'''
devs = ['router','switch']
for each in devs:
    if each == 'router':
        print(each,each)
        continue    # 如果出现'router'，打印2次后进入下一次循环。
    print(each)     # 普通情况只打印一次。
else:
    print("Run out of devs")

#常规 while-else
print('*'*20+' while-else '+'*'*25)

devs = ['router','switch']
print(len(devs))
i = 0
while i!=len(devs):
    print(devs[i])
    i += 1
else:
    print("Run out of devs")

'''
while-break-else
一旦循环非正常结束，中途跳出终结了，else的代码块就不会被执行
'''

print('*'*20+' while-break-else '+'*'*25)

devs = ['router','switch']
i = 0
while i!=len(devs):
    if(devs[i]=='router'):
        print(devs[i])
        break
    print(devs[i])
    i += 1
else:
    print("Run out of devs")

'''
while-continue-else
加入continue的话，我想大家应该都能猜出该干嘛还干嘛吧
'''
print('*'*20+' while-continue-else '+'*'*25)

devs = ['router','switch']
i = 0
while i!=len(devs):
    if(devs[i]=='router'):
        print(devs[i],devs[i])
        i += 1
        continue
    print(devs[i])
    i += 1
else:
    print("Run out of devs")
