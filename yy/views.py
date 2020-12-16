# coding:utf-8
import datetime
import os

from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from pztop import settings
from yy import models
from .forms import UserForm, RegisterForm


def index(request):
    art = models.Article.objects.all().order_by('id')
    artlist = {
        'art': art
    }
    return render(request, 'yy/index.html', artlist)


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        # message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            password = make_password(password1)
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'yy/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'yy/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'yy/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.username = username
                new_user.password = password  # hash_code(password1)  # 使用加密密码
                new_user.email = email
                # new_user.sex = sex
                # new_user.is_active = True 活跃用户默认
                new_user.is_staff = True  # 是否可以登录后台
                new_user.save()
                message = "恭喜你注册成功！3秒后跳转"
                return redirect('/wait/')

                # code = make_confirm_string(new_user)
                # send_email(email, code)

                # message = '请前往注册邮箱，进行邮件确认！'
                # return render(request, 'yy/confirm.html', locals())  # 跳转到等待邮件确认页面。
    register_form = RegisterForm()
    return render(request, 'yy/register.html', locals())


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                # user = models.User.objects.get(username=username)
                user = auth.authenticate(username=username, password=password)
                if user.check_password(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except AttributeError:
                message = "登陆信息有误，请重新输入！"
        return render(request, 'yy/login.html', locals())

    login_form = UserForm()
    return render(request, 'yy/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())


def uploadFiles(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        # 接受前端传来的文件
        upfiles = request.FILES.getlist('xFile')  # ["xFile"]
        # 将传来的文件保存至/settings.py中自定义设定的MDEIA_ROOT目录upload中，
        # 并且文件名用传来的文件名命名
        for i in upfiles:
            saveurl = os.path.join(settings.MEDIA_ROOT, i.name)
            with open(saveurl, 'wb') as fp:
                for j in i.chunks():
                    fp.write(j)
                fp.close()
        return render(request, 'yy/uploadfiles.html')


def robots(request):
    return HttpResponse(
        '<span>User-agent:BaiduSpider</span><br>'
        '<span>Disallow:</span><br>'
        '<br>'
        '<span>User-agent:Googlebot</span><br>'
        '<span>Disallow:</span><br>'
        '<br>'
        '<span>User-agent:*</span><br>'
        '<span>Disallow:/</span><br>'
    )


def articleinfo(request, article_id):
    article = models.Article.objects.values('body', 'id', 'title', 'created_time').filter(id=article_id)
    articlelist = {
        'article': article
    }
    return render(request, 'yy/article.html', articlelist)


def Navigation(request):
    return render(request, 'yy/Navigation.html')


def wait(request):
    return render(request, "yy/wait.html")
