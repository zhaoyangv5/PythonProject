"""
读取表格，然后对每个 IP 地址使用 ping3 进行 ping 检测。对每个 IP 进行 ping 检测的时候，
为了提高效率，我们在此使用多线程的并发技术，因为 ping 操作是占用 I/O 的一种行为，比较适合使用多线程。
这里我们用到的是 Python 内置的 threading 模块，用它的 Thread 类创建一个线程对象，然后执行这个线程，这个线程对象的创建有两部分，
第一部分是 target，即要执行的目标函数，第二部分是 args 即参数列表，执行的时候就会将 args 传入到 target 指向的函数
"""
import ping3
import threading
import pandas as pd


def single_ping(ip, timeout, ping_results):
   """
  ping 一个单独的IP地址
  :param ip: 要ping的IP地址
  :param timeout: ping的超时时间
  :param ping_results: 所有IPping的结果，字典格式，key是IP，value是ping的结果。
  """
   ping_time = ping3.ping(ip, timeout=timeout)
   # print(ping_time)
   ping_results[ip] = ping_time


def batch_ping(file='ping.xlsx', result_file='ping_result.xlsx', timeout=4):
   """
  从文件中读取待ping的列表，然后使用多线程批量去ping，结果再到一个表格文件中
  :param file: 待ping的表格文件
  :param timeout: 超时时间
  """
   # 通过pandas读取ip列表
   df = pd.read_excel(file)
   ip_items = df.to_dict(orient='records')
   print(ip_items)   #[{'ip': '172.16.25.12'}, {'ip': '172.16.25.38'},
   ip_list = []
   # 将字典的列表转换为字符串的列表
   for i in ip_items:
       ip_list.append(i['ip'])
   # 用于存储ping结果的字典
   ping_results = {}

   # 使用多线程进行批量的ping操作
   threads = []
   # 循环读取IP
   for ip in ip_list:
       # 将每个IP地址传、超时时间和存放结果的字典，通过多线程方式传给目标函数，创建一个线程
       t = threading.Thread(target=single_ping, args=(ip, timeout, ping_results))
       # 线程追加到线程池
       threads.append(t)
       # 启动此线程任务
       t.start()
   # 阻塞多线程任务，即当所有的线程执行完成后再继续主程序的余下部分代码
   for t in threads:
       t.join()
   # 将ping的结果再写会到原来的字典列表中去
   # 以从表格中读取到的字典列表作为数据源，以保证顺序一致
   for i in ip_items:
       # 根据 IP 地址获取其结果
       item_ping_result = ping_results[i['ip']]
       # 对情况进行判断，以文字的方式编写结果
       if item_ping_result is None:
           i['result'] = '超时失败'
           print('ping {} 超时失败'.format(i['ip']))
       elif item_ping_result is False:
           i['result'] = '域名解析失败'
           print('ping {} 域名解析失败'.format(i['ip']))
       else:
           i['result'] = '成功'
           print('ping {} 正常'.format(i['ip']))
   # 极简表格操作法，写入表格
   # print(ping_results)
   new_df = pd.DataFrame(ip_items)
   new_df.to_excel(result_file, index=False, columns=['ip', 'result'])


if __name__ == '__main__':
   batch_ping()