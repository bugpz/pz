from django.contrib import admin
from .models import Article, User
from . import models
# Register your models here.
import xadmin
from xadmin import views


class ArticleAdmin(object):
    list_display = ('id', 'title', 'created_time',)
    list_display_links = ('title',)


class TestAdmin(object):
    list_display = ('id', 'type', 'base_field',)
    list_display_links = ('type',)


class UserAdmin(object):
    list_display = ('id', 'username', 'password', 'email', 'sex')
    list_display_links = ('username',)


class GlobalSetting(object):
    site_title = 'BUGPZ'
    site_footer = 'BUGPZ.XYZ'


# admin.site.register(Article,ArticleAdmin)
# admin.site.register(Test,TestAdmin)
# admin.site.register(User,UserAdmin)
# xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.site_header = 'BUGPZ后台'
xadmin.site.site_title = 'BUGPZ.TOP'
