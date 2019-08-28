from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        psw = request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username, password=psw)
        if obj:
            return render(request, 'index.html')
            # return redirect('/cmdb/index/')
        else:
            error_msg = "用户名或密码错误！"
    return render(request, 'login.html', {'error_msg': error_msg})


def user_info(request):
    userset = models.UserInfo.objects.all()
    return render(request, 'user_info.html', {'userset': userset})


def user_detail(request, nid):
    user = models.UserInfo.objects.filter(id=nid).first()
    return render(request, "userinfo_detail.html", {'user': user})


# def index(request):
#     return render(request, 'index.html')


def orm(request):
    models.UserInfo.objects.create(username='root', password='123')
    return HttpResponse("orm")
