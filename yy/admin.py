from django.contrib import admin
# from .models import User
from . import models


# Register your models here.


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'base_field',)
    list_display_links = ('type',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'sex')
    list_display_links = ('username',)


# admin.site.register(Article,ArticleAdmin)
# admin.site.register(Test,TestAdmin)
# admin.site.register(User,UserAdmin)
admin.site.register(models.User)
admin.site.site_header = '后台管理'
admin.site.site_title = 'BUG.TOP'
