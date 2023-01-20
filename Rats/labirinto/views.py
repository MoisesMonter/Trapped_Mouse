from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,AnonymousUser
from . import views
# Create your views here.

class create_lab:
    labirinto_criado=[]
    def __init__(self,info):
        global labirinto_criado

def Home(request):
    return HttpResponse(f"SIM")

def labirinto(request):

    if request.method == 'GET':
        return render(request,"labirinto.html")
    if request.method == 'POST':
        lab= [
            [request.POST.get('l0c0'),request.POST.get('l0c1'),request.POST.get('l0c2'),request.POST.get('l0c3'),request.POST.get('l0c4'),request.POST.get('l0c5')],
            [request.POST.get('l1c0'),request.POST.get('l1c1'),request.POST.get('l1c2'),request.POST.get('l1c3'),request.POST.get('l1c4'),request.POST.get('l1c5')],
            [request.POST.get('l2c0'),request.POST.get('l2c1'),request.POST.get('l2c2'),request.POST.get('l2c3'),request.POST.get('l2c4'),request.POST.get('l2c5')],
            [request.POST.get('l3c0'),request.POST.get('l3c1'),request.POST.get('l3c2'),request.POST.get('l3c3'),request.POST.get('l3c4'),request.POST.get('l3c5')],
            [request.POST.get('l4c0'),request.POST.get('l4c1'),request.POST.get('l4c2'),request.POST.get('l4c3'),request.POST.get('l4c4'),request.POST.get('l4c5')],
            [request.POST.get('l5c0'),request.POST.get('l5c1'),request.POST.get('l5c2'),request.POST.get('l5c3'),request.POST.get('l5c4'),request.POST.get('l5c5')]]
        create_lab.labirinto_criado = [[c == 'on' for c in l] for l in lab]
        print(create_lab.labirinto_criado)
        x = request.POST.get('l3c0')
        print(x)
        return redirect('labirinto2')


def labirinto2(request):
    info= create_lab.labirinto_criado
    if request.method == 'GET':
        return render(request,"labirinto2.html",{'Matriz':info})
    if request.method == 'POST':
        return render(request,"labirinto2.html",{'Matriz':info})



