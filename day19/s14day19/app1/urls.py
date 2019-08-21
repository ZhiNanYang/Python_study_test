from django.urls import path
from app1 import views
from django.urls import re_path

urlpatterns = [
    path('login/', views.login),
    path('home/', views.home),
    # path('detail/', views.detail),
    re_path('detail-(\d+).html', views.detail),
    # re_path('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
    # re_path('asd/', views.Index.as_view(), name='i1'),
    # re_path('fgh/(\d+)/(\d+)', views.Index.as_view(), name='i2'),
    re_path('jkl/(?P<uid>\d+)/(?P<nid>\d+)/', views.Index.as_view(), name='i3'),
]
