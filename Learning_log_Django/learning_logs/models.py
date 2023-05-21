from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   #Topic中添加了字段owner，它建立到模型User的外键关系

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # ForeignKey 外键，引用数据库中另一条记录
    text = models.TextField()     # TextField 字段不需要限制长度
    date_added = models.DateTimeField(auto_now_add=True)   # DateTimeField 记录日期和时间

    class Meta:   # Meta用于管理模型的额外信息 ，这里使用entries 来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
