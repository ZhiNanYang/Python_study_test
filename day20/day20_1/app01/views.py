from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.


def business(request):
    v = models.Business.objects.all()
    return render(request, 'business.html', {'v': v})


def host(request):
    v1 = models.HOST.objects.all()
    v2 = models.HOST.objects.filter(nid__gt=0).values('hostname', 'ip', 'port', 'b__caption')
    # for row in v2:
    #     print(row['b__caption'])
    v3 = models.HOST.objects.filter(nid__gt=0).values_list('hostname', 'ip', 'port', 'b__caption')
    # for row in v3:
    #     print(row[3])
    return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3})
