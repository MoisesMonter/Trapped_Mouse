from random import randint
pilha =[]

def Info():
    info = ['top','bootom','left','right']
    return info[randint(0,3)]


class Local_Actions:
    def __init__(self,R,Q,L):
        self.Rato = R
        self.Queijo = Q
        self.Map = L
        self.Mod_Map = L
        self.Pile = []
        pass

    def Top(self):
            #[0]L [0]c    
        if int(self.Rato[0]) != 0: 
            [print(l) for l in self.Map]
            self.Map[int(self.Rato[0])][int(self.Rato[1])]=False 
            self.Rato[0]= int(self.Rato[0]) -1   
            self.Map[int(self.Rato[0])][int(self.Rato[1])]= 'Rato'
            [print(l) for l in self.Map]
            self.pilha.append
        else:
            print("Can't to moove to up")
            

    def Bottom(self):
            #[0]L [0]c    
        if int(self.Rato[0]) != len(self.Map)-1: 
            [print(l) for l in self.Map]
            print('\n')
            self.Map[int(self.Rato[0])][int(self.Rato[1])]=False 
            self.Rato[0]= int(self.Rato[0]) +1   
            self.Map[int(self.Rato[0])][int(self.Rato[1])]= 'Rato'
            [print(l) for l in self.Map]
        else:
            print("Can't to moove to down")

    def Left(self):
        pass

    def Right(self):
        pass

    def main(self):
        pass
if __name__ == "__main__":
    R = [1,0]
    Q = [5,5]
    L = [[False,True,True],['Rato',True,True],[False,False,'Q']]
    print(len(L))
    print(Local_Actions(R,Q,L).Bottom())
    print('\n')
    print(Local_Actions(R,Q,L).Bottom())