from django.db import models

# Create your models here.
"""
1. ORM
    表 --> 类
    字段 --> 属性
2. 模型类需要继承自models.Model
3. 模型类会自动为我们添加一个主键
4. 属性名==属性类型（选项）
    属性名：不要使用 python mysql关键字
           不要使用 连续的下划线
    属性类型：和MySQL类型类似
    选项： charfiled 必须设置 max_length
          varchar(M)
          null  是否为空
          unique 唯一
          default  默认值
          verbose_name  主要是后台显示
"""
# insert into bookinfo(name, pub_date, readcount, commentcount, is_delete) values
# ('射雕英雄传', '1980-5-1', 12, 34, 0),
# ('天龙八部', '1986-7-24', 36, 40, 0),
# ('笑傲江湖', '1995-12-24', 20, 80, 0),
# ('雪山飞狐', '1987-11-11', 58, 24, 0);


# 书籍表：
#   id, name, pub_date, readcount, commentcount, is_delete
class BookInfo(models.Model):

    # objects = models.Manager()
    # 属性名=属性类型（选项）
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    # 发布日期
    pub_date = models.DateField(null=True, verbose_name="发布日期")
    # 阅读量
    readcount = models.IntegerField(default=0, verbose_name="阅读量")
    # 评论量
    commentcount = models.IntegerField(default=0, verbose_name="评论量")
    # 是否逻辑删除
    is_delete = models.BooleanField(default=True, verbose_name="逻辑删除")

    class Meta:
        # 改数据库表名
        db_table = "bookinfo"
        # 修改后台admin的显示信息
        verbose_name = "图书"

    def __str__(self):
        return self.name

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    #on_delete  CASCADE级联，删除主表数据时连通一起删除外键表中数据
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

