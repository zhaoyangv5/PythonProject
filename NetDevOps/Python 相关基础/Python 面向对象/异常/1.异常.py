
"""
异常语法
try:
    可能发⽣生错误的代码
except:
    如果出现异常执⾏行行的代码
"""

# 体验
# 需求：尝试以r模式打开文件，如果文件不存在，则以w方式打开
try:
    f = open('test.txt', 'r')
except:
    f = open('text.txt', 'w')