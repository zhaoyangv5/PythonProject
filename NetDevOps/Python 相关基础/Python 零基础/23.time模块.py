'''
time模块
'''
import time

print(time.localtime()) #time模块可以获取当前时间，返回一个struct_time时间格式的对象
#time.struct_time(tm_year=2023, tm_mon=3, tm_mday=18, tm_hour=16, tm_min=25, tm_sec=37, tm_wday=5, tm_yday=77, tm_isdst=0)

print(time.time(), type(time.time()))    #1679128027.476968 <class 'float'>


'''格式化'''
print(time.strftime('"%Y-%m-%d %H:%M:%S"'), time.localtime())


'''时间偏移'''
now_list = list(time.localtime())
print(now_list)
now_list[1] = 10
print(time.struct_time(now_list))


'''休眠等待（熟练）'''
time.sleep(2)