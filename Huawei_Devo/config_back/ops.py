import paramiko
from helper import *
from device_info import *

class Ops():
    def __init__(self,BACKUP_BASE, IPS, PORT, USERNAMES, PASSWORDS):
        self.backup_base = BACKUP_BASE
        self.ips = IPS
        self.port = PORT
        self.usernames = USERNAMES
        self.passwords = PASSWORDS

    def _back_cfg(self, ip, username, password):
        folder = check_folder(ip, self.backup_base)
        file_name = create_filename()
        local_file = folder + "/" + file_name
        device_file = "/vrpcfg.cfg"

        sftp_pro = paramiko.Transport(sock=(ip,self.port))
        sftp_pro.connect(username=username, password=password)
        sftp_con = paramiko.SFTPClient.from_transport(sftp_pro)
        print(sftp_con)
        sftp_con.get(remotepath=device_file, localpath=local_file) #下载设备内容
        sftp_pro.close()
        print("配置文件已备份在：{}".format(local_file))

    def _update_cfg(self, ip, username, password, remote_file):
        local_path = self.backup_base + ip +'/'
        local_file_name = get_files(local_path)[-1]
        local_file = local_path + local_file_name
        print("已找到配置文件:{}".format(remote_file))

        sftp_pro = paramiko.Transport(sock=(ip,self.port))
        sftp_pro.connect(username=username, password=password)
        sftp_con = paramiko.SFTPClient.from_transport(sftp_pro)
        # print(sftp_con)
        sftp_con.put(localpath=local_file, remotepath=remote_file)
        sftp_pro.close()
        print("配置文件已上传至：{}".format(remote_file))

    def backup_cfg(self):
        for index in range(len(self.ips)):
            ip = self.ips[index]
            username = self.usernames[index]
            password = self.passwords[index]
            self._back_cfg(ip, username, password)
            print("所有设备已完成配置备份!")

    def updata_cfg(self):
        for index in range(len(self.ips)):
            ip = self.ips[index]
            username = self.usernames[index]
            password = self.passwords[index]
            self._update_cfg(ip, username, password, "/test.cfg")
            print("所有设备上传最新配置！")

if __name__ == "__main__":
    ops_server = Ops(BACKUP_BASE, IPS, PORT, USERNAMES, PASSWORDS)
    ops_server.backup_cfg()
    ops_server.updata_cfg()