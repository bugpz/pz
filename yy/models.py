from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# 如果数据库中的UserInfo(用户表)继承django内置AbstractUser 则需要导入下面的包
# from django.contrib.auth.models import AbstractUser
# 并在settings文件添加AUTH_USER_MODEL = "应用名.UserInfo"
# Create your models here.


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    body = RichTextUploadingField('内容', max_length=200, blank=True)
    created_time = models.DateTimeField('发布时间')

    def __str__(self):
        return self.title  # 这段返回为页面显示的值

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

        def __str__(self):
            return self.title


class User(models.Model):
    # 用户表
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    username = models.CharField(verbose_name='昵称', max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True, verbose_name='邮箱')
    sex = models.CharField(max_length=10, choices=gender, default='男')
    creattime = models.DateField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '增加用户'
        verbose_name_plural = '用户管理'

        def __str__(self):
            return self.name
