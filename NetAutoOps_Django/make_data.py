import os

#制造数据
import os


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetAutoOps_Django.settings')
    import django
    django.setup()
    from cmdb.models import Device
    Device.objects.all().delete()
    for i in range(100, 112):
        dev = Device(ip='192.168.31.{}'.format(i),
                     name='netdevops{}'.format(i),
                     vendor='Huawei',
                     platform='huawei',
                     model='CE12800',
                     series='CE12800',
                     username='python',
                     password='Admin@123',
                     protocol='ssh',
                     port=22)
        dev.save()


if __name__ == '__main__':
    main()
