# from django.contrib import auth
# from yy.forms import RegisterForm, UserForm
# from rest_framework import viewsets
# from django.contrib.auth.models import User, Group
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from pztop import settings
from django.contrib.auth.hashers import make_password, check_password
import json
from django.http import JsonResponse
from yy import models
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from yy.serializers import YYUserSerializer, YYUserLogin
import hashlib


# class Register(GenericAPIView):
#     """
#         post:
#             注册接口
#     """
#     serializer_class = YYUserSerializer
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         username = json.loads(request.body.decode("utf-8")).get("username")
#         password = json.loads(request.body.decode("utf-8")).get("password")
#         email = json.loads(request.body.decode("utf-8")).get("email")
#         # sex = json.loads(request.body.decode("utf-8")).get("sex")
#         password = make_password(password)
#         same_name_user = User.objects.filter(username=username)
#         if same_name_user:  # 用户名唯一
#             return JsonResponse({
#                 'message': '用户已存在,请重新输入'
#             })
#         same_email_user = User.objects.filter(email=email)
#         if same_email_user:  # 邮箱地址唯一
#             return JsonResponse({
#                 'message': '该邮箱地址已被注册，请使用别的邮箱！'
#             })
#
#         # 当一切都OK的情况下，创建新用户
#
#         new_user = User()
#         new_user.username = username
#         new_user.password = password  # hash_code(password1)  # 使用加密密码
#         new_user.email = email
#         # new_user.sex = sex
#         # new_user.is_active = True 活跃用户默认
#         new_user.is_staff = True  # 是否可以登录后台
#         new_user.save()
#         return JsonResponse({
#             'message': '注册成功'
#         })


class Register(GenericAPIView):
    """
        post:
            注册接口
    """
    serializer_class = YYUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        md5 = hashlib.md5()
        username = json.loads(request.body.decode("utf-8")).get("username")
        password = json.loads(request.body.decode("utf-8")).get("password")
        email = json.loads(request.body.decode("utf-8")).get("email")
        sex = json.loads(request.body.decode("utf-8")).get("sex")
        phone = json.loads(request.body.decode("utf-8")).get("phone")
        md5.update(password.encode(encoding='utf-8'))  # 密码md5加密
        password = md5.hexdigest()
        password = make_password(password)
        same_name_user = models.User.objects.filter(username=username)
        if same_name_user:  # 用户名唯一
            return JsonResponse({
                'message': '用户已存在,请重新输入'
            })
        same_phone_user = models.User.objects.filter(phone=phone)
        if same_phone_user:
            return JsonResponse({
                'message': '该手机号已注册，请使用其他手机号'
            })
        same_email_user = models.User.objects.filter(email=email)
        if same_email_user:  # 邮箱地址唯一
            return JsonResponse({
                'message': '该邮箱地址已被注册，请使用别的邮箱！'
            })

        # 当一切都OK的情况下，创建新用户

        new_user = models.User()
        new_user.username = username
        new_user.password = password  # hash_code(password1)  # 使用加密密码
        new_user.email = email
        new_user.sex = sex
        new_user.phone = phone
        # new_user.is_active = True 活跃用户默认
        # new_user.is_staff = True  # 是否可以登录后台
        new_user.save()
        return JsonResponse({
            'message': '尊敬的' + username + ',恭喜你注册成功'
        })


class Login(GenericAPIView):
    serializer_class = YYUserLogin
    permission_classes = (AllowAny,)

    def post(self, request):
        md5 = hashlib.md5()
        phone = json.loads(request.body.decode('utf-8')).get('phone')
        password = json.loads(request.body.decode('utf-8')).get('password')
        md5.update(password.encode(encoding='utf-8'))
        password = md5.hexdigest()
        same_phone = models.User.objects.filter(phone=phone).exists()  # exists()返回bool类型
        if same_phone:
            user = models.User.objects.get(phone=phone)
            if check_password(password, user.password):
                return JsonResponse({
                    'message': '欢迎登录'
                })
            else:
                return JsonResponse({
                    'message': '密码错误，请重新输入'
                })
        else:
            return JsonResponse({
                'message': '此手机号尚未注册，请先注册'
            })
