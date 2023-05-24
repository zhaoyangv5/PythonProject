from django.urls import path
from book import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('rece/', views.ReceiveView.as_view(), name='receive'),

]