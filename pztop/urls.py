"""pztop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# coding:utf-8
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from yy import views
import xadmin
from rest_framework import routers  # 路由配置模块

# 路由
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'groups', views.GroupViewSet)

# 重要的是如下三行
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  path('xadmin/', xadmin.site.urls),
                  path(r'favicon.ico', RedirectView.as_view(url=r'static/UI/img/favicon.ico')),
                  # path(r'', views.index),
                  path('', include(router.urls)),
                  path(r'wait/', views.wait),
                  path(r'register/', views.register),
                  path(r'login/', views.login),
                  path(r'logout/', views.logout),
                  path(r'index/', views.index),
                  path(r'uploadFiles/', views.uploadFiles),
                  path(r'robots.txt/', views.robots),
                  path(r'Navigation/', views.Navigation),
                  path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
                  path('swagger', schema_view, name='docs'),

                  # 富文本编辑器
                  path('ckeditror/', include('ckeditor_uploader.urls')),
                  # path(r'article/',views.article),
                  url(r'^blog/', include('yy.urls', namespace='yy')),
                  path('api/', include('yy.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
