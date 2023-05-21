from ping3 import ping
from datetime import datetime


def fun_ping3(ih):
    # ih 表示ip或host
    result = ping(ih)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if result is None:
        print(ih + '  不通')
        with open('toping_result.txt', mode='a') as f:
            f.write(f'{now}   {ih},不通\n')

    elif result is False:
        print(ih + '  域名解析失败')
        with open('toping_result.txt', mode='a') as f:
            f.write(f'{now}   {ih},域名解析失败\n')

    else:
        print(ih + '  可达')
        with open('toping_result.txt', mode='a') as f:
            f.write(f'{now}   {ih},可达\n')


if __name__ == '__main__':
    # toping_list.txt存放IP地址或域名，一项一行。
    with open('toping_list.txt') as f:
        toping_list = f.readlines()

    with open('toping_result.txt', mode='a') as f:
        f.write('\n')

    for each in toping_list:
        fun_ping3(each.strip())