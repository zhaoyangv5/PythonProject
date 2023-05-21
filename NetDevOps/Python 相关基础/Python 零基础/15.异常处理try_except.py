'''
try-except结构
执行try代码块中的表达式，如果try代码块中未发生异常（即“没有捕获到异常”），则程序会跳过except代码块而继续执行！
执行try代码块中的表达式，如果try代码块中发生了异常（即“已经捕获到异常”），则程序会跳过try代码块剩余的代码。
如果except代码块包含了捕获的那个异常，则执行except代码块内容。
如果except代码块未包含捕获的那个异常，则程序中断，并抛出异常。
'''
try:
    100/0
except ZeroDivisionError:
    print("You can't divide by zero")


# 22222没有被打印出来，因为在执行它之前，已经捕获异常了。也就是说，try模块一旦捕获到异常了，程序是不会再继续执行该try代码块中的后续内容了
try:
    print('11111')  # 可能发生异常之前。
    100/0
    print('22222')  # 可能发生异常之后。
except ZeroDivisionError:
    print("You can't divide by zero")


# 一try多except
# 如果除数为0，则需要捕获ZeroDivisionError异常；如果除数或被除数有一个非数字类型，则需要捕获ValueError异常
print('*'*20+' 一try多except '+'*'*25)
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print("Result: ", int(a)/int(b))
except ValueError:
    print("Please enter only numbers")
except ZeroDivisionError:
    print("You can't divide by zero")


#一except多异常
print('*'*20+' 一except多异常 '+'*'*25)
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print("Result: ", int(a)/int(b))
except(ValueError,ZeroDivisionError):
    print("Something went wrong...")


#一except无异常
# 在except代码块中如果不指定任何任何异常的话，它会捕获和处理任意异常，但是，通常我们不这么做.
print('*'*20+' 一except无异常 '+'*'*25)

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print("Result: ", int(a)/int(b))
except:
    print("Something went wrong...")

#try-except-else结构
#在try-except结构的基础上，我们增加一个else代码块，以确保在代码正常情况下继续执行
print('*'*20+' try-except-else结构 '+'*'*25)

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Something went wrong...")
else:
    print(f"Result is : {result}")

#try-except(-else)-finally结构
'''
在try-except结构的基础上，我们增加一个finally代码块，以确保代码无论抛出异常与否，最后都要执行finally代码块中的动作。
这有什么用？比如文件打开过程中出错了，那最后还是有必要把这个文件给关闭。关闭文件的这个动作，就可以放置在finally代码块中
'''
print('*'*20+' try-except(-else)-finally结构 '+'*'*25)

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Something went wrong...")
else:
    print(f"Result is : {result}")
finally:
    print("All is OK！")


#组合使用
'''
针对处理异常的try-except-else-finally结构，我们常常会配合while、for、if等本部分前序小节的内容，综合应用，才有效果
'''
print('*'*20+' 组合使用 '+'*'*25)

while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    try:
        result = int(a)/int(b)
    except ValueError:
        print("Only digits are supported")
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(result)
        break


#另一种写法
while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("You can't divide by zero")
        else:
            print(int(a)/int(b))
            break
    else:
        print("Only digits are supported")