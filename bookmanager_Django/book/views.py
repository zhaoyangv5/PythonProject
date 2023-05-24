from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from book.models import BookInfo, PeopleInfo

# Create your views here.
"""
视图
1. 就是Python函数
2. 函数的第一个参数就是 请求
"""
def index(request):

    books = BookInfo.objects.all()
    peoples = PeopleInfo.objects.all()

    context = {
        'books': books,
        'peoples': peoples
    }
    return render(request, 'index.html', context=context)

# 关联查询
# book = BookInfo.objects.get(id=1)  # 单值
# book.peopleinfo_set.all()  # 列表
# BookInfo.objects.filter(peopleinfo__description__contains='八')
# PeopleInfo.objects.filter(book__readcount__gt=50)

def detail(request, categord_id, book_id):

    # 提取URL的特定部分，如/weather/beijing/2018，可以在服务器端的路由中用正则表达式截取；
    # print(categord_id, book_id)


    # 查询字符串（query string)，形如key1=value1&key2=value2；

    # http://127.0.0.1:8000/1/200/?username=zhaoyang&password=python&username=admin

    # query_params = request.GET
    # # query_params = request.GET.getlist['username']
    # # <QueryDict: {'username': ['zhaoyang'], 'password': ['python']}>
    # # QueryDict 以普通的字典形式来获取  一键多值的时候， 只能获取最后的那个值
    # # 如果想获取一键多值， 就需要使用  QueryDict的 getlist方法
    # print(query_params)
    # username = query_params['username']
    # password = query_params['password']
    # print(username, password)
    # # print(query_params)

    # POST 表单数据
    # data = request.POST
    # print(data)
    # <QueryDict: {'username': ['zhaoyang'], 'password': ['123']}>

    # POST json数据
    """
    {
        "name": "zhaoyang"    
    }
    """
    # print(request.POST)
    # body = request.body
    # print(body) # b'{\n    "username":"zhaoyang",\n    "password":"python"\n}'
    # print(body.decode(), type(body.decode()))   # 得到json形式的字符串，不是字典
    # # json.dumps 将字典 转换为 json形式的字符串
    # # json.loads 将json形式的字符串转为 字典
    # import json
    # print(json.loads(body.decode()))  # 字典形式 {'username': 'zhaoyang', 'password': 'python'}

    # 请求头  是字典数据
    # print(request.META)
    #
    # Content_Type = request.META["CONTENT_TYPE"]
    # print(Content_Type)

    print(request.method)

    # HttpResponse
    # content：表示返回的内容
    # status 只能使用系统规定的
    # content_type 是一个MIME类型，语法形式：大类/小类
    # return HttpResponse('detail', status=400, content_type='')

    # 跳转页面
    path = reverse("book:index")
    return redirect(path)

def login(request):

    return HttpResponse('这是登录页面')

# 类视图

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class CenterView(LoginRequiredMixin, View):  # 多继承，LoginRequiredMixin跳转至登录页面

    def get(self, request):
        return HttpResponse('个人中心展示')

    def post(self, request):
        return HttpResponse('个人中心修改')


class HomeView(View):

    def get(self, request):

        username = request.GET.get('username')

        context = {
            'username': username,
            'age': 14,
            'birthday': datetime.now(),
            'firends': ['tom', 'jack', 'rose'],
            'money': {
                '2019': 5000,
                '2020': 10000,
                '2021': 25000,
            },
            'desc': '<script>alert("hot")</script>'
        }

        # return render(request,'detail.html')
        # return render(request, 'home_django.html', context=context)
        return render(request, 'home_jinja2.html', context=context)


