from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def login(request):
    # models.UserGroup.objects.create(caption='DBA')
    # models.UserGroup.objects.filter(uid="1").update(caption="DBB")
    # obj = models.UserGroup.objects.filter(uid="1").first()
    # obj.caption="DBB"
    # obj.save()
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
    if request.method == "GET":
        userset = models.UserInfo.objects.all()
        return render(request, 'user_info.html', {'userset': userset})
    elif request.method == "POST":
        user = request.POST.get("username")
        psw = request.POST.get("password")
        models.UserInfo.objects.create(username=user, password=psw)
        return redirect("/cmdb/user_info")


def user_detail(request, nid):
    user = models.UserInfo.objects.filter(id=nid).first()
    return render(request, "userinfo_detail.html", {'user': user})


def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info')


def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    if request.method == 'POST':
        nid = request.POST.get('id')
        user = request.POST.get('user')
        psw = request.POST.get('psw')
        models.UserInfo.objects.filter(id=nid).update(
            username=user, password=psw)
        return redirect('/cmdb/user_info')


def orm(request):
    models.UserInfo.objects.create(username='root', password='123')
    return HttpResponse("orm")
