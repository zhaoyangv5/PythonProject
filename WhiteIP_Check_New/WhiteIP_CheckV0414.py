from IPy import IP
import os
import time

def Check_ip(target_ip, WhiteIP_lst):
    for dic in WhiteIP_lst:
        # print(dic)
        for item in dic.items():
            # print(item[1])   # item[0]就是key  item[1]就是value
            for WhiteIP in item[1]:
                # print(WhiteIP)
                # 判断target_ip是否存在于白名单中
                try:
                    if IP(target_ip) in IP(WhiteIP):
                        print(f"{target_ip}")
                        # print(f"{target_ip}  存在于--->  {item[0]}")
                except:
                    pass
                    # print(f"请检查ip合法性  --> {WhiteIP}  -->{item[0]}")

def get_TargetIP_lst():
    TargetIP_lst = []
    with open("./target.txt", mode='r', encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        for target_ip in IP(line.replace("\n", "")):
            # print(target_ip)
            TargetIP_lst.append(target_ip)
    # print(TargetIP_lst)
    return TargetIP_lst


def get_WhiteIP_lst():
    WhiteIP_file_list = os.listdir("./source/")
#   print("\n", "已获取到白名单ip文件有: ", WhiteIP_file_list)
#   print("\n")
    WhiteIP_lst = []
    for WhiteIP_file in WhiteIP_file_list:
        dic = {}
        # 循环获取白名单文件中的ip
        lst = []
        with open(f"./source/{WhiteIP_file}", mode='r', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                WhiteIP = line.replace("\n", "")  # print(WhiteIP,"   ",WhiteIP_file)
                # 检查ip是否合法,不合法即不会检查
                try:
                    IP(WhiteIP).version()
                    lst.append(WhiteIP)
                except:
                    print(f"请检查ip合法性  --> {WhiteIP}  -->{WhiteIP_file}")

        dic[f"{WhiteIP_file}"] = lst
        WhiteIP_lst.append(dic)
    # print(WhiteIP_lst)
    # print("\n")
    return WhiteIP_lst


def main():
    # 1.获取白名单文件列表
    WhiteIP_lst = get_WhiteIP_lst()
    # 2.循环获取需要检查目标ip
    TargetIP_lst=get_TargetIP_lst()
    # with open("./target.txt", mode='r', encoding="utf-8") as f:
    #     lines = f.readlines()
    # for line in lines:
    #     target_ip = line.replace("\n", "")
        # 3.检查目标ip是否存在于白名单
    for target_ip in TargetIP_lst:
        Check_ip(target_ip, WhiteIP_lst)


if __name__ == '__main__':
    # get_TargetIP_lst()
    main()
time.sleep(10)