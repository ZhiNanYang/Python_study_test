"""s14day19_2 URL Configuration

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
from django.urls import path, re_path
from app01 import views


urlpatterns = [
    path('login/', views.login),
    # path('index/', views.index),
    path('user_info/', views.user_info),
    re_path('userinfo-detail-(?P<nid>\d+)/', views.user_detail),
    re_path('user-del-(?P<nid>\d+)/', views.user_del),
    re_path('user-edit-(?P<nid>\d+)/', views.user_edit),
    path('orm/', views.orm),
]