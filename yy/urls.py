# from django.conf.urls import url
from django.urls import path
from . import views
from yy.API import user

app_name = 'yy'
urlpatterns = [
    # url(r'^article/(?P<article_id>[0-9]+)$', views.articleinfo, name='page'),
    # path('register', views.register, name='register'),
    path('test', views.test, name='test'),
    path('test1', views.test1, name='t1'),
    path('t2', views.Test1.as_view()),
    path('register', user.Register.as_view()),
    path('login', user.Login.as_view())
    # path(r'^ register/', user.Register.as_view(), name='task')
]
