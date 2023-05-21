from django.urls import path

from cmdb import views

urlpatterns = [
    path('index/', views.index, name='cmdb_index')
]