from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
import os
# from django.shortcuts import HttpResponse


USER_LIST = [
    {"username": "", "email": "", "gender": ""},
]


def login(request):
    error_msg = ""
    if request.method == "POST":

        # radio
        gend = request.POST.get('gend', None)
        print("性别：" + gend)

        # checkbox
        aihao = request.POST.getlist('aihao', None)
        print("爱好：" + str(aihao))

        # file
        obj = request.FILES.get('fafafa')
        file_path = os.path.join("upload", obj.name)
        f = open(file_path, mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()

        # select one
        city = request.POST.get("city1")
        print('city ' + city)

        # select multi
        city = request.POST.getlist("city2")
        print('citylist ' + str(city))

        # login
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == "root" and pwd == "123":
            return redirect('/home')
        else:
            error_msg = "用户名或密码错误"

    return render(request, "login.html", {"error_msg": error_msg})


def home(request):
    if request.method == "POST":
        u = request.POST.get('username', None)
        e = request.POST.get('email', None)
        g = request.POST.get('gender', None)
        temp = {"username": u, "email": e, "gender": g}
        USER_LIST.append(temp)
    return render(request, "home.html", {"user_list": USER_LIST})


class Index(View):
    """docstring for Index"""

    def get(self, request):
        print(request.method)
        return render(request, 'index.html')

    def post(self, request):
        print(request.method)
        return render(request, 'index.html')
