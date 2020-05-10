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
#coding:utf-8
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from yy import views
import xadmin
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    path(r'favicon.ico',RedirectView.as_view(url=r'static/UI/img/favicon.ico')),
    path(r'',views.index),
    path(r'register/',views.register),
    path(r'login/',views.login),
    path(r'logout/',views.logout),
    path(r'index/',views.index),
    path(r'uploadFiles/',views.uploadFiles)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
