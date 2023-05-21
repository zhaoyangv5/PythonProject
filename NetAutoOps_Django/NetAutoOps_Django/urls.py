"""
URL configuration for NetAutoOps_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve

import cmdb.views as cmdb_views
# import NetAutoOps_Django.cmdb.views as cmdb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cmdb/index/', cmdb_views.index, name='cmdb_index'),
    path('cmdb/', include('cmdb.urls')),
    # 当将DEBUG模式关闭后，之前的路由条目配置也就会失效，这个时候，我们可能要用到另外一个方式了，写明访问资源的路径，
    # 以及用一个专门处理静态文件类的view函数来去寻找文件并返回给调用方。而Django也内置了这样一个view函数，是django.conf.urls.static模块的serve函数。
    # 我们传入一条特定的路由条目，由于访问的文件资源路径不断变化，所以我们需要用到一种具有正则能力的path——re_path，它可以配置一个正则表达式，匹配一类URL，
    # 并通过正则表达式的捕获子表达式方法提取这个URL路径中的一些信息，我们这里是捕获media文件夹后的路径
    # 基于path函数的一种演变，可以识别正则表达式的URL并将其中的一部分识别传给view函数
    # re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
# 我们使用django.conf模块的settings与使用我们自己写的配置文件NetAutoOps\settings.py效果是等价的，对于初学者使用后者也可以。
# 我们调用完static方法后会将访问媒体文件的URL与对应的文件系统路径对应起来，生成一个路由条目，我们一般使用加法追加到原有的列表后面
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)