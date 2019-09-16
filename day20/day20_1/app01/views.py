from django.shortcuts import render, HttpResponse, redirect
from app01 import models
import json
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


def test_ajax(request):
    ret = {"status": True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 5:
            models.HOST.objects.create(hostname=h, ip=i, port=p, b_id=b)
        else:
            ret['status'] = False
            ret['error'] = '太短了！'
    except Exception:
        ret['status'] = False
        ret['error'] = '请求错误！'
    return HttpResponse(json.dumps(ret))


def edit_ajax(request):
    ret = {"status": True, 'error': None, 'data': None}
    try:
        print(request.POST)
        h = request.POST.get('hostname')
        d = request.POST.get('id')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        print(d, h, i, p, b)
        if h and len(h) > 5:
            models.HOST.objects.filter(nid=d).update(hostname=h, ip=i, port=p, b_id=b)
        else:
            ret['status'] = False
            ret['error'] = '太短了！'
    except Exception:
        ret['status'] = False
        ret['error'] = '请求错误！'
    return HttpResponse(json.dumps(ret))


def del_ajax(request):
    d = request.POST.get('nid')
    models.HOST.objects.filter(nid=d).delete()
    return HttpResponse()
