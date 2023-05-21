# Generated by Django 4.2 on 2023-04-15 08:25

import cmdb.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_configbackup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configbackup',
            name='config_file',
            field=models.FileField(upload_to=cmdb.models.config_backup_upload_to, verbose_name='配置文件'),
        ),
    ]