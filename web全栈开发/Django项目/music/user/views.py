from django.shortcuts import render, redirect
from django.shortcuts import reverse
from user.models import *
from .form import MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
# Create your views here.

# 用户注册与登录
def loginView(request):
    # 创建一个表单对象
    user = MyUserCreationForm()

    if request.method == 'POST':
        # 登录
        if request.POST.get('loginUser', ''):
            u = request.POST.get('loginUser', '')
            p = request.POST.get('password', '')
            if MyUser.objects.filter(Q(mobile=u) | Q(username=u)):
                u1 = MyUser.objects.filter(Q(mobile=u) | Q(username=u)).first()
                if check_password(p, u1.password):
                    login(request, u1)
                    return redirect(reverse('home', kwargs={'page': 1}))
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        # 注册
        else:
            u = MyUserCreationForm(request.POST)
            if u.is_valid():
                u.save()
                tips = '注册成功'
            else:
                if u.errors.get('username', ''):
                    tips = u.errors.get('username', '注册失败')
                else:
                    tips = u.errors.get('mobile', '注册失败')
    return render(request, 'user.html', locals())

