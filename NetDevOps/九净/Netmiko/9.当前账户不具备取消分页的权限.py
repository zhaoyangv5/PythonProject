'''
有时候当前用户不具备取消分页的权限时，也会导致send_command报错，从错误堆栈来看与执行时间较长的情况没有差别，即使调整timeout也无济于事。
这个时候我们可以看看debug信息，netmiko帮助我们执行取消分页命令的时,是否命令正确，是否权限足够，这些在log和debug信息中通过回显都可以观察到。
其中绝大多数情况是，出于安全考虑。当前账户不具备执行取消分页命令的权限。所以在后面执行一些命令的时候，会卡在--more--类似的回显上，需要我们输入回车才能继续回显。
这个是由netmiko的机制决定的，出于各种考虑，netmiko的驱动基本在登录设备后都会自动取消分页，以便发送命令回显完整，不需要人为干预

在我们仍坚持使用netmiko的前提下，一个是给用户权限进行调整，一个是自己写代码实现这种分页的交互，自己判断，自动输入回车。
在条件允许的前提下，个人建议使用第一种方案，如果受制于各种因素，确实无法对用户权限调整，
我们也可以通过一些netmiko的底层方法write_channel与read_channel为大家解决

'''

'''基于这两个方法，我们对分页进行了处理，同时模仿send_command的pattern机制进行了主体逻辑的设计'''
import re
import time

from netmiko import ConnectHandler


def send_command_for_uer_no_disable_paging(dev, cmd):
    with ConnectHandler(**dev) as conn:
        # 存放回显的变量
        output = ''
        # 判断回显结束的正则
        output_end_pattern = r'<\S+>'
        # 判断分页交互的正则
        more_pattern = '  ---- More ----'

        # 超时时间，隧道中读取内容的间隔时间，根据二者计算的循环次数
        timeout = conn.timeout
        loop_delay = 0.2
        loops = timeout / loop_delay
        i = 0
        # 通过write_channel发送命令，命令后追加一个回车换行符
        conn.write_channel('{}{}'.format(cmd, conn.RETURN))
        # 进入循环，读取隧道中信息
        while i <= loops:
            # 读取隧道中的信息，放入chunk_output
            chunk_output = conn.read_channel()
            # 判断是否有分页交互提示
            if more_pattern in chunk_output:
                # 回显中的分页提示去除,去除一些影响回显展示的空格
                chunk_output = chunk_output.replace(more_pattern, '').replace('               ','')
                # 拼接回显
                output += chunk_output
                # 发送回车换行符
                conn.write_channel(conn.RETURN)
            # 根据提示符判断是否回显结束
            elif re.search(output_end_pattern, chunk_output):
                # 拼接回显 并跳出循环
                output += chunk_output
                break
            # 停顿loop_delay秒
            time.sleep(loop_delay)
            # 计数器i加一 类似其他语言中的i++
            i += 1
        # 如果超过了，则证明超时，我们可以自己抛出异常
        if i > loops:
            raise Exception('执行命令"{}"超时'.format(cmd))
        return output


if __name__ == '__main__':
    dev = {'device_type': 'huawei',
           'host': '192.168.31.100',
           'username': 'python',
           'password': 'Admin@123',
           'port': 22,
           'session_log': 'session.log'
           }
    output = send_command_for_uer_no_disable_paging(dev, 'display current-configuration')
    print(output)
