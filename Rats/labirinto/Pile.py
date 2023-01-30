from random import randint
from time import sleep
from os import system,name


Repeticoes = 100



def Info():
    info = ['top','bottom','left','right']
    return info[randint(0,3)]

def Limpar():
    system('cls' if name == 'nt' else 'clear')


class Main_pile:
    def __init__(self):
        self.Save= {}

    def Desempilhar_Dict(self):
        info = []

        for desempilhar in range(int(len(self.Save))-1,-1,-1): #desempilhando lista de opções
            #print(desempilhar)
            if len(info) == 0:
                info =  self.Save[desempilhar]
                self.Save.popitem()
            elif len(info) >= len(self.Save[desempilhar]):
                info =  self.Save[desempilhar]
                self.Save.popitem()
        try:
            info = [info[dp] for dp in range(int(len(info))-1,-1,-1)] #pilha do caminho
        except:
            pass
        return info
                                                                            
    def main(self,Rato,Queijo,Mapa):
        print(Rato,'quist')
        for loop in range(Repeticoes):
            self.Save[int(len(self.Save))] = Local_Actions([Rato[info] for info in range(2)],[Queijo[info] for info in range(2)],[[Mapa[x][y] for y in range(len(Mapa[x]))]for x in range(len(Mapa))]).run()
        #print([print(x) for x in self.Save.items()])
        Pile = self.Desempilhar_Dict()    
        print(Pile)
        return Pile

class Local_Actions:
    def __init__(self,R,Q,L):
        self.info = ['top','bottom','left','right']
        self.Dicionario = {}
        self.__Rato = R
        self.__Queijo = Q
        self.__Map = L
    

    def Dict_is_Zero(self):
        if len(self.Dicionario) <1:
            wind_rose  =  [direcitons for direcitons in self.info]
            self.Dicionario[int(len(self.Dicionario))] = [wind_rose,None]

    def Cheese_End(self):
        convert1  = [int(x) for x in self.__Rato] 
        convert2  = [int(x) for x in self.__Queijo] 
        return convert1 == convert2

    def Wall(self,direction):
        try:
            if direction == 'top':
                if(self.__Map[int(self.__Rato[0])-1][int(self.__Rato[1])] == True or self.__Map[int(self.__Rato[0])-1][int(self.__Rato[1])] == '.' or self.__Map[int(self.__Rato[0])][int(self.__Rato[1])] == 'Queijo'):
                    return True
        except:
            pass
        try:
            if direction == 'bottom':
                if (self.__Map[int(self.__Rato[0])+1][int(self.__Rato[1])] == True or self.__Map[int(self.__Rato[0])+1][int(self.__Rato[1])] == '.' or self.__Map[int(self.__Rato[0])][int(self.__Rato[1])] == 'Queijo') :
                    return True
        except:
            pass 
        try:
            if direction == 'left':
                if (self.__Map[int(self.__Rato[0])][int(self.__Rato[1])-1] == True  or self.__Map[int(self.__Rato[0])][int(self.__Rato[1])-1] == '.' or self.__Map[int(self.__Rato[0])][int(self.__Rato[1])] == 'Queijo'):

                    return True
        except:
            pass 
        try:
            if direction == 'right':
                if (self.__Map[int(self.__Rato[0])][int(self.__Rato[1])+1] == True or self.__Map[int(self.__Rato[0])][int(self.__Rato[1])+1] == '.' or self.__Map[int(self.__Rato[0])][int(self.__Rato[1])] == 'Queijo'):
                    return True
        except:
            pass

    def Move(self,direction):
        #[0]L [0]c    
        move_l_c=None
        if direction == 'top' or direction == 'bottom': #manipular linha   /\  .  \/
            move_l_c=0
        elif direction == 'left' or direction == 'right':#manipular coluna <-- . -->
            move_l_c=1
        if int(self.__Rato[move_l_c]) <= len(self.__Map)-1 : 
            #Verificar se há parede
            if self.Wall(direction) != True:
                if  direction == 'top' and int(self.__Rato[move_l_c])   >0 :  # linha /\
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]='.'
                    self.__Rato[0]= int(self.__Rato[0]) -1   
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
                    self.Dicionario[len(self.Dicionario)] = [[direcitons for direcitons in self.info],'top']
                elif direction == 'bottom'   and int(self.__Rato[0]) < len(self.__Map)-1:  #linha \/ and self.__Map[self.__Rato[0+1]][self.__Rato[1]] == False or self.__Map[int(self.__Rato[0])-1][int(self.__Rato[1])] == 'Queijo'
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]='.'
                    self.__Rato[0]= int(self.__Rato[0]) +1      
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
                    self.Dicionario[len(self.Dicionario)] = [[direcitons for direcitons in self.info],'bottom']
                elif direction == 'left'   and int(self.__Rato[1])   >0:  #coluna >   and self.__Map[self.__Rato[0]][self.__Rato[1]-1] == False or self.__Map[int(self.__Rato[0])-1][int(self.__Rato[1])] == 'Queijo'
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]='.'
                    self.__Rato[1]= int(self.__Rato[1]) -1
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
                    self.Dicionario[len(self.Dicionario)] = [[direcitons for direcitons in self.info],'left']
                elif direction == 'right'  and int(self.__Rato[1])   < len(self.__Map)-1:  #coluna <   and self.__Map[self.__Rato[0]][self.__Rato[1]+1] == False or self.__Map[int(self.__Rato[0])-1][int(self.__Rato[1])] == 'Queijo'
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]='.'
                    self.__Rato[1]= int(self.__Rato[1]) +1
                    self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
                    self.Dicionario[len(self.Dicionario)] = [[direcitons for direcitons in self.info],'right']
                else:
                    print("Can't to moove to",direction)

                
            else:
                print("have an Wall in",direction)
        else:
            print("Can't to moove to",direction)

    def Next_Step(self):
        '''
        -1 definir se a lista de direções esteja vazia
        '''
        aux_step = self.Dicionario[len(self.Dicionario)-1][0]


        if aux_step.count(None) == 4:
            aux_prev = self.Dicionario[len(self.Dicionario)-1][1] #pegando elemento utilizado na casa anteriro
            self.Dicionario.popitem() #removendo ultima posição do dic

            if  aux_prev == 'top' :  # linha /\
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]=False
                self.__Rato[0]= int(self.__Rato[0]) +1   
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
            elif aux_prev == 'bottom' :  #linha \/
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]=False
                self.__Rato[0]= int(self.__Rato[0]) -1      
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
            elif aux_prev == 'left'   :  #coluna >   
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]=False
                self.__Rato[1]= int(self.__Rato[1]) +1
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
            elif aux_prev == 'right':  #coluna <   
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]=False
                self.__Rato[1]= int(self.__Rato[1]) -1
                self.__Map[int(self.__Rato[0])][int(self.__Rato[1])]= 'Rato'
            else:
                return -1

        else:
            while True:
                try:
                    position = Info()
                    position_remove = aux_step.index(position) #verifica posição
                    if aux_step[position_remove] != None:
                        aux_step[position_remove] = None
                        self.Dicionario[len(self.Dicionario)-1][0] = aux_step
                        return position
                except:
                    pass

    def Save_Pile(self):
        local_list = [self.Dicionario[x][1] for x in self.Dicionario]
        return local_list[1:] #ignorar none

    
    
    def run(self):
        self.Dict_is_Zero()
        while True:
            if self.Cheese_End():
                print('ops')
                return self.Save_Pile()

            local_action = self.Next_Step()
        
            if local_action == -1:
                print("Final inconclusivo")
                break


            elif local_action in ['top','left','right','bottom']:
                #print(local_action)
                self.Move(local_action)
            print(self.Dicionario)
            [print(l) for l in self.__Map]

        print("end")



'''if __name__ == "__main__":
    R = [0,0]
    Q = [2,5]
    L = [['Rato' ,True ,False ,False ,False ,False],
         [False ,True  ,False ,True  ,False ,True],
         [False ,True  ,False ,True  ,False ,'Queijo'],
         [False ,True  ,False ,True  ,False ,True],
         [False ,True  ,False ,False ,False ,False],
         [False ,False ,False ,True  ,False ,False]]
    Main_pile().main(R,Q,L)
'''

