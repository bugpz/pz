# from django.contrib import admin
from .models import User
# from . import models
# Register your models here.
import xadmin
from xadmin import views


class ArticleAdmin(object):
    list_display = ('id', 'title', 'creatTime',)
    list_display_links = ('title',)


class TestAdmin(object):
    list_display = ('id', 'type', 'base_field',)
    list_display_links = ('type',)


class UserAdmin(object):
    list_display = ('id', 'username', 'password', 'email', 'sex')
    list_display_links = ('username',)


class GlobalSetting(object):
    site_title = 'BUG'
    site_footer = 'BUG.XYZ'


# admin.site.register(Article,ArticleAdmin)
# admin.site.register(Test,TestAdmin)
# admin.site.register(User,UserAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(User, UserAdmin)
xadmin.site.site_header = '后台管理'
xadmin.site.site_title = 'BUG.TOP'
