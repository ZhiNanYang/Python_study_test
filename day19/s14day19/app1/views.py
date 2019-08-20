from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
import os
from django.shortcuts import HttpResponse


USER_LIST = [
    {"username": "", "email": "", "gender": ""},
]

# USER_DICT = {
#     'k1': "root1",
#     'k2': "root2",
#     'k3': "root3",
#     'k4': "root4",
# }
USER_DICT = {
    '1': {'name': 'root1', 'email': 'root1@live.com'},
    '2': {'name': 'root2', 'email': 'root2@live.com'},
    '3': {'name': 'root3', 'email': 'root3@live.com'},
    '4': {'name': 'root4', 'email': 'root4@live.com'},
}


# def detail(request, *args, **kwargs):
#     print(kwargs.get('uid'))
#     return HttpResponse(args, kwargs)


# def detail(request, nid, uid):
#     print(nid, uid)
#     detail_info = USER_DICT[nid]
#     return render(request, "detail.html", {"detail_info": detail_info})


def detail(request, nid):
    # return HttpResponse(nid)
    detail_info = USER_DICT[nid]
    return render(request, "detail.html", {"detail_info": detail_info})


# def detail(request):
#     nid = request.GET.get("nid")
#     detail_info = USER_DICT[nid]
#     return render(request, "detail.html", {"detail_info": detail_info})


def login(request):
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

    def dispatch(self, request, *args, **kwargs):
        print("before dispatch")
        result = super(Index, self).dispatch(request, *args, ** kwargs)
        print("after dispatch")
        return result

    def get(self, request, nid):
        print(request.method)
        return render(request, 'index.html')

    def post(self, request, nid):
        print(request.method)
        return render(request, 'index.html', {"user_dict": USER_DICT})
