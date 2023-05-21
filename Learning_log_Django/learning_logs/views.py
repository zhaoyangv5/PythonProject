from django.shortcuts import render

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token

# Create your views here.
def index(request):
    """学习笔记主页"""
    return render(request, "learning_logs/index.html")

@login_required()           # 装饰器 login_required()的代码检查用户是否已登录，仅当用户已登录时，Django才运行topics()的代码
def topics(request):
    """显示所有主题"""
    # 用户登录后，request对象将有一个user属性，这个属性存储了有关该用户的信息
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")   # 让Django只从数据库中获取owner属性为当前用户的Topic对象
    # topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context=context)


# @login_required()
def topic(request, topic_id):
    """显示单个主题及所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    # if topic.owner != request.user:
    #     raise Http404
    # print(topic.id)
    entries = topic.entry_set.order_by("-date_added")
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context=context)


# @login_required()
def new_topic(request):
    """添加新主题"""
    if request.method != "POST":    #判断是get还是post请求，如果get，则返回一个空表单
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)  #请求是post，使用用户输入的数据创建一个TopicForm的表单
        if form.is_valid():     #函数is_valid()核实用户填写了所有必不可少的字段（表单字段默认都是必不可少的），且输入的数据与要求的字段类型一致，models.py中指定的
            new_topic = form.save(commit=False)  # 首先调用form.save()，并传递实参commit=False，这是因为我们先修改新主题，再将其保存到数据库中
            new_topic.owner = request.user    #将新主题的owner属性设置为当前用户
            new_topic.save()
            return HttpResponseRedirect(reverse("learning_logs:topics"))    # 使用reverse()获取页面topics的URL，并将其传递给HttpResponseRedirect()，后者将用户的浏览器重定向到页面topics。在页面topics中，用户将在主题列表中看到他刚输入的主题
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context=context)


# @login_required()
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',
                                        args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# @login_required()
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)    #获取用户要修改的条目对象
    topic = entry.topic
    # if topic.owner != request.user:
        # raise Http404
    if request.method != "POST":
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)    #使用实参instance=entry创建一个EntryForm实例
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)     #处理POST请求时，我们传递实参instance=entry和data=request.POST
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("topic",
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context=context)