"""定义learning_logs的URL模式"""

from django.urls import path
from learning_logs import views


urlpatterns = [
    #主页
    path(r'index/', views.index, name='index'),

    #显示所有的主题
    path(r'topics/', views.topics, name='topics'),
    #特定主题的详细页面
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    #用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

]