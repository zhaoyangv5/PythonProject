from django.contrib import admin, messages
from django.db import models
# Register your models here.
# from cmdb.models import Device, Version
from cmdb.models import Device, Version, Interface, ConfigBackup


# 引入我们的批量收集更新软件版本的函数
# from tools.tasks.collect_version import batch_collect_version
from tools.tasks.collect_version import batch_collect_version
from tools.tasks.collect_interfaces import batch_collect_interfaces
from tools.tasks.backup_config import batch_backup_config



#  编写一个Action函数，有三个参数是Django规定的标准
def update_version(modeladmin, request, queryset):
    # 调用批量更新软件版本的函数
    result = batch_collect_version(queryset)
    # 组织返回给用户的信息
    success_num = result['success_num']
    fail_num = result['fail_num']
    fail_dev = result['fail_dev']
    messages.info(request, '更新软件版本成功{}台,失败{}台，失败名单如下：{}'.format(success_num, fail_num, fail_dev))


# 我们通过对Action函数的short_description赋值，可以修改其在下拉框中的显示名称
update_version.short_description = '更新软件版本'

def update_interfaces(modeladmin, request, queryset):
    # 调用批量更新软件版本的函数
    result = batch_collect_interfaces(queryset)
    # 组织返回给用户的信息
    success_num = result['success_num']
    fail_num = result['fail_num']
    fail_dev = result['fail_dev']
    messages.info(request, '更新端口信息成功{}台,失败{}台，失败名单如下：{}'.format(success_num, fail_num, fail_dev))


# 我们通过对Action函数的short_description赋值，可以修改其在下拉框中的显示名称
update_interfaces.short_description = '更新端口列表'

def backup_config(modeladmin, request, queryset):
    # 调用批量配置备份的函数
    result = batch_backup_config(queryset)
    # 组织返回给用户的信息
    success_num = result['success_num']
    fail_num = result['fail_num']
    fail_dev = result['fail_dev']
    messages.info(request, '配置备份成功{}台,失败{}台，失败名单如下：{}'.format(success_num, fail_num, fail_dev))


# 我们通过对Action函数的short_description赋值，可以修改其在下拉框中的显示名称
backup_config.short_description = '配置备份'


# 使用内联管理类将配置项与设备关联
class VersionInline(admin.TabularInline):
    # 关联的模型
    model = Version
    fields = ['version', 'patch', 'series', 'update_time']
    # 只读字段配置
    readonly_fields = fields
    # 是否可以删除条目的设置
    can_delete = False
    # 单独形式的名称，对应内联管理左下角的添加按钮显示名称
    verbose_name = '版本'
    # 复数形式的名称，对应列表名称
    verbose_name_plural = '软件版本'
    # 配置折叠的样式
    classes = ['collapse']

class InterfaceInline(admin.TabularInline):
    # 关联的模型
    model = Interface
    fields = ['name', 'protocol_state', 'phy_state', 'desc']
    # 只读字段配置
    readonly_fields = fields
    # 是否可以删除条目的设置
    can_delete = False
    # 额外添加的空白条目
    extra = 0
    # 单独形式的名称，对应内联管理左下角的添加按钮显示名称
    verbose_name = '端口'
    # 复数形式的名称，对应列表名称
    verbose_name_plural = '端口列表'
    # 是否展示超链接
    show_change_link = True
    # 配置折叠的样式
    classes = ['collapse']

class ConfigBackupInline(admin.TabularInline):
    # 关联的模型
    model = ConfigBackup
    # 只读字段配置
    fields = ['cmd', 'config_file']
    readonly_fields = ['cmd']
    # 是否可以删除条目的设置
    can_delete = False
    # 额外添加的空白条目
    extra = 0
    # 复数形式的名称，对应列表名称
    verbose_name_plural = '配置备份'
    # 配置折叠的样式
    classes = ['collapse']

# 创建Device的Admin管理类
class DeviceAdmin(admin.ModelAdmin):
    # 将我们创建的内联管理类注册到设备管理界面，可以追加多个
    inlines = [VersionInline, InterfaceInline, ConfigBackupInline]
    # 将之前编写的Action函数追加到actions属性中
    actions = [update_version, update_interfaces, backup_config]
    list_display = ['id', 'name', 'ip', 'vendor', 'platform', 'created_time', 'update_time']  #页面 device 显示的内容
    list_per_page = 15                                 # 页面显示数量
    search_fields = ['name', 'ip', 'vendor']            # 增加搜索栏，基于name ip vendor的搜索
    list_display_links = ['id', 'name', 'ip']           # 鼠标变小手，并提示超链接
    list_editable = ['vendor', 'platform']              # 在页面就可以修改参数，不用跳转进里面
    date_hierarchy = 'created_time'                     # 日期按照created time进行层级管理
    ordering = ['-update_time', 'ip']                   # 以更新时间递减，ID递增进行排序
    list_filter = ['vendor', 'platform']                # 列表页面侧边筛选

    # 将密码置为只读状态，将其追加到Admin管理类的readonly_fields属性中，其值为字段的列表，可以将多个字段置为只读。
    # 综上，我们通过fields属性指定显示的字段和其顺序。然后编辑readonly_fields属性，首先将一些不可编辑的字段（id、created_time、update_time）追加进去，
    # 然后将一些可编辑字段置为只读属性，将password字段追加到readonly_fields的列表中

    #     fields = ['id', 'name', 'ip', 'vendor', 'platform', 'model', 'series', 'username',
    #               'password', 'protocol', 'port', 'created_time', 'update_time']
    readonly_fields = ['id', 'update_time', 'created_time', 'password']

    # Django Admin提供了一种详情页布局的定制方式，可以将一些字段合并到一块区域显示，同时添加一些摘要信息。
    # 这个就是由Admin管理类中的fieldsets属性决定的，它与fields是互斥的
    # fieldsets = [
    #     ('基本信息', {'fields': ['id', 'ip', 'name']}),
    #     ('型号信息', {'fields': ['vendor', ('series', 'model')]}),
    #     ('登录信息', {'fields': [('username', 'password'), 'platform', ('protocol', 'port')]}),
    #     ('其他信息', {'fields': [('created_time', 'update_time')]}),
    # ]
    fieldsets = [
        ('基本信息', {'fields': ['id', 'ip', 'name']}),
        ('型号信息', {'fields': ['vendor', ('series', 'model')]}),
        ('登录信息', {'fields': [('username', 'password'),
                                 ('secret', 'platform'),
                                 ('protocol', 'port'),
                                 ('conn_timeout', 'timeout')
                                 ],
                      }
         ),
        ('其他信息', {'fields': [('created_time', 'update_time')]}),
        ]

# 将Device Admin管理类与Device Model绑定注册到Admin管理后台
admin.site.register(Device, DeviceAdmin)

class VersionAdmin(admin.ModelAdmin):
    list_display = ['id', 'dev', 'version', 'patch', 'series', 'update_time']
    list_per_page = 15
    search_fields = ['dev', 'version', 'patch', 'series']
    list_display_links = ['id', 'version', 'patch']
    ordering = ['dev__name']
    list_filter = ['version', 'patch', 'series']
    readonly_fields = ['id', 'update_time', 'created_time']


admin.site.register(Version, VersionAdmin)


class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['dev', 'name', 'desc', 'phy_state', 'protocol_state', 'update_time']
    list_per_page = 15
    # 希望对外键的某个字段进行搜索的时候，可以使用外键字段双下划线连接外键模型中某字段的方式
    # 如想在搜索中可以查找设备名，则使用dev__name
    search_fields = ['dev__name', 'dev__ip', 'name', 'desc']
    list_display_links = ['dev', 'name']
    ordering = ['dev', 'name']
    date_hierarchy = 'update_time'
    fields = ['id', 'dev', 'name', 'desc', 'phy_state', 'protocol_state', 'created_time', 'update_time']
    readonly_fields = ['id', 'created_time', 'update_time']


admin.site.register(Interface, InterfaceAdmin)


class ConfigBackupAdmin(admin.ModelAdmin):
    list_display = ['dev', 'cmd', 'config_file', 'created_time']
    search_fields = ['dev__name', 'dev__ip', 'cmd']
    date_hierarchy = 'created_time'
    fields = ['id', 'dev', 'cmd', 'config_file', 'created_time']
    # 配置备份实际修改字段的需求不大，所以我们全部设置为只读字段。
    readonly_fields = fields
    list_per_page = 15
    # 侧边标签快捷搜索我们使用命令和设备所属平台，这个属性中我们也可对外键属性的字段进行搜索
    list_filter = ['cmd', 'dev__platform']


admin.site.register(ConfigBackup, ConfigBackupAdmin)