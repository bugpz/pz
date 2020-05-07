#coding:utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse

from pztop import settings
from yy import models,views
from .forms import UserForm,RegisterForm
from .models import Article,User
from django.views.generic import View
from django.contrib.auth.hashers import make_password,check_password
import pymysql ,datetime,os,time

# Create your views here.
# def get_loan_number(file):
#     connect = pymysql.Connect(
#         host="139.196.94.33",
#         port=3306,
#         user="root",
#         passwd="bugpz559",
#         db="YY",
#         charset='utf8'
#     )
#     # print("写入中，请等待……")
#     cursor = connect.cursor()
#     usersql = 'select password from auth_user where'
#     sql = "select password from auth_user"
#     cursor.execute(sql)
#     number = cursor.fetchall()
#     fp = open('数据库测试.txt', "w")
#     loan_count = 0
#     for loanNumber in number:
#         loan_count += 1
#         fp.write(loanNumber[0] )
#     fp.close()
#     cursor.close()
#     connect.close()
#     print("写入完成,共写入%d条数据……" % loan_count)


def index(request):
    yy_user = models.User.objects.all().order_by('-id')
    yy_article = models.Article.objects.all().order_by('-id')
    context = {
        'yy_user':yy_user,
        'yy_article':yy_article
    }
    return render(request,'yy/index.html',context)
    # #文件上传
    # if request.method == "GET":
    #     return render(request, 'index.html')
    # else:
    #     # 接受前端传来的文件
    #     xFile = request.FILES["xFile"]
    #     # 将传来的文件保存至/settings.py中自定义设定的MDEIA_ROOT目录upload中，
    #     # 并且文件名用传来的文件名命名
    #     filePath = os.path.join(settings.MEDIA_ROOT, xFile.name)
    #     with open(filePath, 'wb') as fp:
    #         for xFileStream in xFile.chunks():
    #             fp.write(xFileStream)
    #     return HttpResponse("上传成功")

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
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'yy/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'yy/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'yy/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.username = username
                new_user.password = password1  #hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                message = "恭喜你注册成功！"
                return render(request,'yy/login.html',locals())

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
                user = models.User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
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
        #接受前端传来的文件
        xFile = request.FILES["xFile"]
        # 将传来的文件保存至/settings.py中自定义设定的MDEIA_ROOT目录upload中，
        # 并且文件名用传来的文件名命名
        filePath = os.path.join(settings.MEDIA_ROOT, xFile.name)
        with open(filePath, 'wb') as fp:
            for xFileStream in xFile.chunks():
                fp.write(xFileStream)

                return redirect('/index/')


