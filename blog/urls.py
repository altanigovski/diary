from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^entry/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
]
