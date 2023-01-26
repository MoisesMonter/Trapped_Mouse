from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,AnonymousUser
from . import views
from .forms import Matriz2 
# Create your views here.

class create_lab:
    labirinto_criado=[]
    labirinto_Rato=[]
    labirinto_completo=[]
    Rato_Position= []
    Queijo_Position=[]
    def __init__(self,info):
        global labirinto_criado
        global labirinto_Rato
        global labirinto_completo
        global Rato_Position
        global Queijo_Position

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
    x = Matriz2(request.POST)
    print(create_lab.labirinto_criado)
    if request.method == 'GET':
        return render(request,"labirinto2.html",{'Matriz':info,'Matriz2':x})
    if request.method == 'POST':
        if request.POST.get('back') == None:
            if x.is_valid:
                create_lab.Rato_Position = request.POST.get('object_lab').split(' ')
                print(create_lab.Rato_Position)
                create_lab.labirinto_Rato = [[x for x in l]for l in create_lab.labirinto_criado]
                create_lab.labirinto_Rato[int(create_lab.Rato_Position[0])][int(create_lab.Rato_Position[1])] = 'Rato'
                print(create_lab.Rato_Position)
                print( create_lab.labirinto_Rato)
                return redirect('labirinto3')
        else:
            return redirect('labirinto')

        return render(request,"labirinto2.html",{'Matriz':info,'Matriz2':x})

def labirinto3(request):
    info= create_lab.labirinto_criado
    info= create_lab.labirinto_Rato
    x = Matriz2(request.POST)

    if request.method == 'GET':
        return render(request,"labirinto3.html",{'Matriz':info,'Matriz2':x})
    if request.method == 'POST':
        if request.POST.get('back') == None:
            if x.is_valid:
                create_lab.Queijo_Position = request.POST.get('object_lab').split(' ')
                print(create_lab.Queijo_Position)
                create_lab.labirinto_completo = [[x for x in l]for l in create_lab.labirinto_Rato]
                create_lab.labirinto_completo[int(create_lab.Queijo_Position[0])][int(create_lab.Queijo_Position[1])]='Queijo'
                print(create_lab.Queijo_Position)
                print(create_lab.labirinto_completo)
                x = Matriz2(request.POST)
                return render(request,"labirinto4.html",{'Matriz':create_lab.labirinto_completo,'Matriz2':x})
        else:
            return redirect('labirinto2')
        return render(request,"labirinto3.html",{'Matriz':info,'Matriz2':x})

