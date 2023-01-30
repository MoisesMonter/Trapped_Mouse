from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,AnonymousUser
from . import views
from .forms import Matriz2
from .Pile import *
# Create your views here.

class create_lab:
    labirinto_criado=[]
    labirinto_Rato=[]
    labirinto_completo=[]
    Rato_Position= []
    Queijo_Position=[]
    Start = False
    Compile = False
    Pile = []
    def __init__(self,info):
        global labirinto_criado
        global labirinto_Rato
        global labirinto_completo
        global Rato_Position
        global Queijo_Position
        global Start
        global Compile
        global Pile



def corrindo_erro():
    print(int(len(create_lab.labirinto_criado)))
    if int(len(create_lab.labirinto_criado)) < int(1):
        return redirect('labirinto')
    return None

def labirinto(request):
    create_lab.Compile = False
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
    create_lab.Compile = False
    if int(len(create_lab.labirinto_criado)) < int(1):
        return redirect('labirinto')
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
    create_lab.Compile = False
    if int(len(create_lab.labirinto_criado)) < int(1):
        return redirect('labirinto')
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
                return redirect('labirinto4')
        else:
            return redirect('labirinto2')

        return render(request,"labirinto3.html",{'Matriz':info,'Matriz2':x})




def labirinto4(request):
    if int(len(create_lab.labirinto_criado)) < int(1):
        return redirect('labirinto')
    corrindo_erro()
    print('chegooo')
    info= create_lab.labirinto_completo
    Interaction = create_lab.Start
    if request.method == 'GET':
        if create_lab.Compile == True:
            list_Pile = [int(z) for z in range(int(len(create_lab.Pile))-1,-1,-1)]
            broke_Piles = len(list_Pile)//7+(int(len(list_Pile)%7)!=0)
            return render(request,"labirinto4.html",{'Matriz':info,'Interaction':Interaction,'Pile':create_lab.Pile,'Posi_Pile':list_Pile})
        return render(request,"labirinto4.html",{'Matriz':info,'Interaction':Interaction})
    if request.method == 'POST':
        if request.POST.get('Start') == 'Start':
            if create_lab.Compile == False:
                create_lab.Compile = True
                print()
                Rato =create_lab.Rato_Position
                Queijo =create_lab.Queijo_Position
                print(Rato,Queijo,info)
                create_lab.Pile = Main_pile().main(Rato,Queijo,create_lab.labirinto_completo)
            create_lab.Start= True
        elif request.POST.get('Start') == 'Back':
            return redirect('labirinto3')
        elif request.POST.get('Start') == 'Next':
            if len(create_lab.Pile) <=0:
                create_lab.Compile = False
                create_lab.Start= False
                return redirect('labirinto4')
            else:
                create_lab.Pile.pop()
            
        return redirect('labirinto4')
