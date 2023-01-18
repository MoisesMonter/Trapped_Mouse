from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,AnonymousUser
from . import views
# Create your views here.


def Home(request):
    return HttpResponse(f"SIM")

def labirinto(request):

    if request.method == 'GET':
        return render(request,"labirinto.html")
    if request.method == 'POST':
        return render(request,"labirinto.html")