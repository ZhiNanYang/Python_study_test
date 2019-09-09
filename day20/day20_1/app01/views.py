from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def business(request):
    v = models.Business.objects.all()
    return render(request, 'business.html', {'v': v})


def host(request):
    if request.method == "GET":
        v1 = models.HOST.objects.all()
        v2 = models.HOST.objects.filter(nid__gt=0).values(
            'hostname', 'ip', 'port', 'b__caption')
        # for row in v2:
        #     print(row['b__caption'])
        v3 = models.HOST.objects.filter(nid__gt=0).values_list(
            'hostname', 'ip', 'port', 'b__caption')
        # for row in v3:
        #     print(row[3])
        b_list = models.Business.objects.all()
        return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3, 'b_list': b_list})
    elif request.method == "POST":
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.HOST.objects.create(hostname=h, ip=i, port=p, b_id=b)
        return redirect('/cmdb/host/')
