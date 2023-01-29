from random import randint
import time
pilha =[]

def Info():
    info = ['top','bootom','left','right']
    return info[randint(0,3)]


class Local_Actions:
    def __init__(self,R,Q,L):
        info = ['top','bootom','left','right']
        self.Dicionario = {}
        self.Rato = R
        self.Queijo = Q
        self.Map = L
        self.Mod_Map = L
        self.Pile = []

    def Wall(self,location):
        try:
            if location == 'Top':
                if(self.Map[int(self.Rato[0])-1][int(self.Rato[0])] == True or self.Map[int(self.Rato[0])-1][int(self.Rato[0])] == 'Q'):
                    return True
            if location == 'Bottom':
                if (self.Map[int(self.Rato[0])+1][int(self.Rato[0])] == True or self.Map[int(self.Rato[0])+1][int(self.Rato[0])] == 'Q') :
                    return True
            if location == 'Left':
                if (self.Map[int(self.Rato[0])][int(self.Rato[0]-1)] == True or self.Map[int(self.Rato[0])-1][int(self.Rato[0])] == 'Q'):
                    return True
            if location == 'Right':
                if (self.Map[int(self.Rato[0])][int(self.Rato[0]+1)] == True or self.Map[int(self.Rato[0])+1][int(self.Rato[0])] == 'Q'):
                    return True
        except:
            print("Can't to moove to left")
    def Top(self):
        info = 'Top'
            #[0]L [0]c    
        if int(self.Rato[0]) != 0: 
            if self.Wall(info) != True:   
                [print(l) for l in self.Map]
                self.Map[int(self.Rato[0])][int(self.Rato[1])]=False 
                self.Rato[0]= int(self.Rato[0]) -1   
                self.Map[int(self.Rato[0])][int(self.Rato[1])]= 'Rato'
                [print(l) for l in self.Map]
                self.Pile.append('Top')
            else:
                print("have an Wall")
        else:
            print("Can't to moove to up")
            

    def Bottom(self):
        info ='Bottom'
            #[0]L [0]c    
        if int(self.Rato[0]) != len(self.Map)-1: 
            if self.Wall(info) != True:        
                [print(l) for l in self.Map]
                print('\n')
                self.Map[int(self.Rato[0])][int(self.Rato[1])]=False 
                self.Rato[0]= int(self.Rato[0]) +1   
                self.Map[int(self.Rato[0])][int(self.Rato[1])]= 'Rato'
                [print(l) for l in self.Map]
                self.Pile.append('Bottom')
            else:
                print("have an Wall")
        else:
            print("Can't to moove to down")

    def Left(self):
        info ='left'
        #[0]L [0]C
        if int(self.Rato[1]) <= len(self.Map)-1 and int(self.Rato[1]) > 0: 
            if self.Wall(info) != True:            
                [print(l) for l in self.Map]
                print('\n')
                self.Map[int(self.Rato[0])][int(self.Rato[1])]=False 
                self.Rato[1]= int(self.Rato[0]) -1   
                self.Map[int(self.Rato[0])][int(self.Rato[1])]= 'Rato'
                [print(l) for l in self.Map]
                self.Pile.append('Left')
            else:
                print("have an Wall")
        else:
            print("Can't to moove to left")

    def Right(self):
        info ='Right'
        #[0]L [0]C
        if int(self.Rato[1]) != len(self.Map)-1: 
            
            if self.Wall(info) != True:
                [print(l) for l in self.Map]
                print('\n')
                self.Map[int(self.Rato[0])][int(self.Rato[1])]=False 
                self.Rato[1]= int(self.Rato[1]) +1   
                self.Map[int(self.Rato[0])][int(self.Rato[1])]= 'Rato'
                [print(l) for l in self.Map]
                self.Pile.append('Right')
            else:
                print("have an Wall")
        else:
            print("Can't to moove to Right")

    def Cheese_End(self):
        return self.Rato == self.Queijo

    def main(self):
        info = self.Cheese_End()
        cont =0
        while True:
            info = self.Cheese_End()
            print('passo =',cont,'\n',self.Rato,'\n',self.Queijo)
            cont+=1
            if info == True:
                print('achou')
                break
            else:
                randomic=Info()
                time.sleep(2)
                if randomic == 'top':
                    print('TOP')
                    self.Top()
                elif randomic == 'bootom':
                    print('Bottom')
                    self.Bottom()
                elif randomic == 'left':
                    print('Left')
                    self.Left()
                elif randomic == 'right':
                    print('Right')
                    self.Right()
        print(self.Pile)

if __name__ == "__main__":
    R = [0,0]
    Q = [2,2]
    L = [['Rato',True,True],[False,True,True],[False,False,'Q']]
    print(Local_Actions(R,Q,L).main())
    #print(Info())
    '''print(Local_Actions(R,Q,L).Right())
    print('\n')
    print(Local_Actions(R,Q,L).Right())
    print('\n')
    print(Local_Actions(R,Q,L).Bottom())
    print('\n')
    print(Local_Actions(R,Q,L).Left())
    print('\n')
    print(Local_Actions(R,Q,L).Left())
    print('\n')
    print(Local_Actions(R,Q,L).Right())
    print('\n')
    print(Local_Actions(R,Q,L).Right())
    print('\n')
    print(Local_Actions(R,Q,L).Right())
    print('\n')'''