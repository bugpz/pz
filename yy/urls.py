from django.conf.urls import url,include
from . import views

app_name = 'yy'
urlpatterns = [
    url(r'^article/(?P<article_id>[0-9]+)$', views.articleinfo, name='page'),
]