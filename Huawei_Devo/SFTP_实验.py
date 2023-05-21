import paramiko
import time
import os

def check_folder(ip, path):
    path +=ip
    if not os.path.isdir(path):
        os.mkdir(path)
        print("{} 目录已建立".format(path))
    return path

def create_filename(time_struct):
    str_year = str(time_struct.tm_year) + "_"
    str_mon = str(time_struct.tm_mon) + "_"
    str_mady = str(time_struct.tm_mday) + "_"
    str_hour = str(time_struct.tm_hour) + "_"
    str_min = str(time_struct.tm_min) + "_"
    str_sec = str(time_struct.tm_sec) + ".cfg"
    file_name = str_year + str_mon + str_mady + str_hour + str_min + str_sec
    return file_name

ip = "192.168.31.100"
port = 22
sock = (ip, port)
backup_path = "./"
folder = check_folder(ip,backup_path)
file_name = create_filename(time.localtime())
local_file = folder + "/" + file_name
device_file = "/vrpcfg.cfg"
sftp_pro = paramiko.Transport(sock=sock)
sftp_pro.connect(username="huawei",password="Admin@123")
sftp_con = paramiko.SFTPClient.from_transport(sftp_pro)
print(sftp_con)
sftp_con.get(remotepath=device_file, localpath=local_file) #下载设备内容
# sftp_con.put(localpath='./192.168.31.100/2021_11_24_21_17_43.cfg', remotepath="/test.cfg")
sftp_pro.close()