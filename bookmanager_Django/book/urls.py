from django.urls import path, re_path
from book import views

urlpatterns = [
    # 主页
    # name 就是给url起个名字
    # 可以通过name找到这个路由
    path(r'index/', views.index, name='index'),
    path(r'home/', views.HomeView.as_view(), name='home'),

    # 根据关键字参数来获取url参数，推荐使用
    re_path(r'^(?P<categord_id>\d+)/(?P<book_id>\d+)/', views.detail, name='detail'), # 利用re_path 正则分组

    path(r'center/', views.CenterView.as_view(), name='center'),

    path(r'accounts/login/', views.login, name='login'),

]