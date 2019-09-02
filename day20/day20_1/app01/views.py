from django.shortcuts import render
from app01 import models
# Create your views here.


def business(request):
    v = models.Business.objects.all()
    return render(request, 'business.html', {'v': v})
