
from platform import system as S_op
from os import system as Varrer

def Limpar(plataforma):
    if len(plataforma) >0:
        Varrer(plataforma)
    if plataforma == "Windows":
        Varrer('cls')
    else:
        Varrer('clear')
    return plataforma


class Node:
    def __init__(self,element):
        self.prev = None
        self.element = element
        self.nex  = None



class LDE:
    def __init__(self):
        self.inicio = None
        self.final  = None

    def Vazio(self):
        return self.inicio == None

    def Cheio(self):
        return self.inicio != None




    def InsereInicio(self,element):
        node = Node(element)

        if self.Vazio():
            self.final = node 
        else:
            self.inicio.prev = node
        node.nex = self.inicio
        self.inicio = node


    def InsereFinal(self,element):
        node = Node(element)
        if self.Vazio():
            self.final= node
        else:
            self.final.nex =node
        node.prev = self.final
        self.final = node


    '''def Deleteinicio(self):
        aux = self.head
        if aux.next != None:
            self.head = self.head.next
            self.head.previous = None

    def Deletefim(self):
        aux = self.end
        if aux.previous != None:
            self.end = self.end.previous
            self.end.previous = None
            self.end.next = self.end.previous'''
            

    def Imprimir(self):
        aux = self.inicio       
        while aux != None:
            if aux.nex != None:
                print(aux.element,end=',')
            else:
                print(aux.element,end='\n')
            aux = aux.next

    def Imprimir_inverso(self):
        aux = self.inicio    
        while aux != None:
            if aux.prev != None:
                print(aux.element,end=',')
            else:
                print(aux.element,end='\n')
            aux =aux.prev


if __name__ == "__main__":
    lista =LDE()
    lista.InsereInicio(4)
    lista.InsereFinal(3)
    lista.Imprimir()

    lista.Imprimir_inverso()
    