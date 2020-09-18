from django.shortcuts import render
from datetime import  datetime as b
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    dt = b.now()
    return render(request,'home.html', context={'date':dt})