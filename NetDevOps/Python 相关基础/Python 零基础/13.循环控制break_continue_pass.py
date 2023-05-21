
'''
操作符 break 允许循环提前结束。

操作符 break 结束本次循环，并继续执行后续代码。
嵌套循环中，操作符 break 跳出其所在的本层循环，其外层循环不受影响。
操作符 break 即可用在 for 结构中，也可用在 while 结构中。
'''

for num in range(5):
    if num < 3:
        print(num)
    else:
        break

print('*'*20+'while的break'+'*'*25)

i = 0
while i < 5:
    if i == 3:
        break
    else:
        print(i)
        i += 1

'''实例演示'''
# username = input('Enter username: ')
# password = input('Enter password: ')
#
# while True:
#     if len(password) < 8:
#         print('Password is too short\n')
#     elif username in password:
#         print('Password contains username\n')
#     else:
#         print(f'Password for user {username} is set')
#         # 密码正确，跳出循环。
#         break
#     password = input('Enter password once again: ')


'''
continue
操作符 break 是结束循环，跳出循环结构体；
操作符 continue 则是结束本轮循环，重新开始下一轮循环。两者容易混淆，我们需要在这里“咬文嚼字”，两者都很重要！
'''
print('*'*20+'continue'+'*'*25)

for num in range(5):
    if num == 3:
        continue    #012345中的3哪里去了？为啥3被跳过了呢？因为num为3的时候，它continue了一下，进入了下一次循环，所以没有被print出来
    else:
        print(num)  #0 1 2 4

i = 0
while i < 5:
    i += 1
    if i == 3:
        print('Skip')
        continue
    else:
        print('Current value: ',i)

'''实例演示'''
# username = input('Enter username: ')
# password = input('Enter password: ')
#
# password_correct = False
#
# while not password_correct:
#     if len(password) < 8:
#         print('Password is too short\n')
#     elif username in password:
#         print('Password contains username\n')
#     else:
#         print(f'Password for user {username} is set')
#         password_correct = True
#         continue      #跳出循环
#     password = input('Enter password once again: ')

print('*'*20+'pass'+'*'*25)
'''
pass
基本上它没什么作用，就是一个占位符。在循环分支等结构中，我们可以适当使用 pass 操作符，在构建并预留这个结构，但暂时不书写这部分的内容。
打个比方，你装修一个房子，有个位置未来要放一台钢琴，但现在钢琴还没买，你拿个箱子想放在那里，假装是台钢琴
'''
for num in range(5):
    if num < 3:
        pass    # 我暂时不干嘛，晚些具体要干嘛再来写。
    else:
        print(num)