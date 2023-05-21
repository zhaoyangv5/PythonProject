import time
import os

def check_folder(ip, path):
    path +=ip
    if not os.path.isdir(path):
        os.mkdir(path)
        print("{} 目录已建立".format(path))
    return path

def create_filename():
    # time_struct = time.localtime()
    # str_year = str(time_struct.tm_year) + "_"
    # str_mon = str(time_struct.tm_mon) + "_"
    # str_mady = str(time_struct.tm_mday) + "_"
    # str_hour = str(time_struct.tm_hour) + "_"
    # str_min = str(time_struct.tm_min) + ".cfg"
    # file_name = str_year + str_mon + str_mady + str_hour + str_min
    file_name = str(time.strftime("%Y_%m_%d_%H_%M_%S.cfg", time.localtime()))
    return file_name

def get_files(path):
    return os.listdir(path)