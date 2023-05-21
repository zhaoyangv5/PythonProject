from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))

def register(request):
    """注册新用户"""
    if request.method != "POST":
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            # 让用户自动登录，这包含两个步骤。首先，我们调用authenticate()，并将实参new_user.username和密码传递给它
            # 用户注册时，被要求输入密码两次；由于表单是有效的，我们知道输入的这两个密码是相同的，因此可以使用其中任何一个
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)    #调用函数login()，并将对象request和authenticated_user传递给它
            return HttpResponseRedirect(reverse('learning_logs:index'))   # 新用户创建有效的会话。最后，我们将用户重定向到主页

    context = {'form': form}
    return render(request, 'users/register.html', context=context)