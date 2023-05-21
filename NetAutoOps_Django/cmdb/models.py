from django.db import models
from pathlib import Path
from datetime import date
# Create your models here.

# 编写一个Device的类，继承自django.db.models.Model，它是Django ORM的核心所在。我们定义的Device类对应一张数据库表格，
# 默认表名称遵循“{app名称}_{类名称}”的形式，且全部为小写，所以表名称为cmdb_device。
#
# 这张数据库表的字段定义也十分简单，我们直接定义类的属性即可。属性（数据库表字段）的定义分两部分：
#
# 属性名称一般为蛇形命名法，且是小写，属性名一定不要使用双下划线，双下划线是有特殊意义存在的。
# 属性的赋值，即实例化一个Django的Filed类即可

class Device(models.Model):
    # objects = None
    ip = models.CharField(verbose_name='IP地址（fqdn）', max_length=128)
    name = models.CharField(verbose_name='设备名', max_length=128, unique=True)  #将设备名称添加唯一约束，即将name字段的值CharField初始化时赋值unique为True
    vendor = models.CharField(verbose_name='厂商', max_length=128)
    platform = models.CharField(verbose_name='平台(netmiko)', max_length=128)
    model = models.CharField(verbose_name='型号', max_length=128)
    series = models.CharField(verbose_name='系列', max_length=128)
    username = models.CharField(verbose_name='用户名', max_length=128)
    password = models.CharField(verbose_name='密码', max_length=128)
    protocol = models.CharField(verbose_name='管理协议', max_length=32, default='ssh')
    port = models.IntegerField(verbose_name='ssh端口', default=22)
    # 新增字段，secret、conn_timeout、timeout
    secret = models.CharField(verbose_name='enable密码', max_length=128, null=True, blank=True) #两个参数null和blank，且都置为了True，这两个参数的赋值是为了让本字段可以置为空值。因为有的设备有可能有enable密码，有的设备可能没有enable密码
    conn_timeout = models.IntegerField(verbose_name='连接超时时间', default=30)
    timeout = models.IntegerField(verbose_name='CLI执行超时时间', default=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)  #auto_now_add：是否在创建的时候赋值为当前时间，如果为真，则数据在被创建的时候，会自动赋值为当前时间
    update_time = models.DateTimeField('更新时间', auto_now=True)  #auto_now：是否在更新时自动设置为当前时间，如果为真，则数据在被更新的时候，会自动赋值为更新时的时间

    def __str__(self):
        return '<网络设备,IP:{},名称:{}>'.format(self.ip, self.name)



# to，代表这个数据模型与哪个数据模型有一对一的关系，我们赋值to为对应Model的字符串即可，在这里我们关联到了网络设备Device类，所以赋值为字符串“Device”
# on_delete，代表当有关联的数据被删除时，与之关联的这条数据（Version数据）该如何处理，使用内置的models.CASCADE即可，它代表当本条关联的数据被删除时，本条数据也进行删除处理.

class Version(models.Model):
    dev = models.OneToOneField(verbose_name='关联设备', to='Device',on_delete=models.CASCADE)
    version = models.CharField(verbose_name='版本号', max_length=128)
    patch = models.CharField(verbose_name='补丁号', max_length=128)
    series = models.CharField(verbose_name='系列', max_length=128)
    uptime = models.CharField(verbose_name='已运行时间', max_length=128)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return '设备：{}的版本:{}'.format(self.dev, self.version)


class Interface(models.Model):
    # 我们需要在Interface模型中添加一个字段dev将其指向一个Device对象，代表这个端口是属于哪台网络设备。
    # 这里我们使用到的也是一个比较特殊的Field——ForeignKey，它的参数设置与OneToOneField基本类似，to字段指向其关联的模型，
    # on_delete字段赋值为级联删除models.CASCADE即可
    dev = models.ForeignKey(verbose_name='关联设备', to='Device', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='端口名', max_length=128)
    index = models.CharField(verbose_name='端口索引', max_length=128)
    phy_state = models.CharField(verbose_name='物理状态', max_length=128)
    protocol_state = models.CharField(verbose_name='协议状态', max_length=128)
    desc = models.CharField(verbose_name='端口描述', max_length=128, null=True, blank=True)
    last_phy_uptime = models.CharField(verbose_name='端口上次物理up时间', max_length=128)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        # 我们可以访问外键对象的属性，比如取所属设备名self.dev.name
        return '{} {}'.format(self.dev.name, self.name)

    class Meta:
        # 唯一约束，可以添加多组，此处我们约束网络设备和端口名应全局唯一
        unique_together = [('dev', 'name')]

# FileField自定义上传路径
def config_backup_upload_to(instance, fielname):
    dev = instance.dev
    date_str = date.today().strftime('%Y%m%d')
    return str(Path('ConfigBackup', date_str, dev.name, fielname))

class ConfigBackup(models.Model):
    dev = models.ForeignKey(verbose_name='关联设备', to='Device', on_delete=models.CASCADE)
    cmd = models.CharField(verbose_name='执行的命令', max_length=128)
    # config_file这个字段是我们需要关注的，它是一个FileField字段，对应配置文件，我们将upload_to赋值为字符串“ConfigBackup”，
    # 代表后续这个文件会放入的文件夹，这个文件夹的路径也有讲究，目前默认是在我们的工程根目录下，如无会自动创建
    # config_file = models.FileField(verbose_name='配置文件', upload_to='ConfigBackup')
    config_file = models.FileField(verbose_name='配置文件', upload_to=config_backup_upload_to)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


    def __str__(self):
        # 我们可以访问外键对象的属性，比如取所属设备名self.dev.name
        return '{}于{}的"{}"备份'.format(self.dev.name, self.created_time, self.cmd)