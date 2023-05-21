"""为应用程序users定义URL模式"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    path('logout/', views.logout_view, name='logout' ),
    path('register/', views.register, name='register'),

]