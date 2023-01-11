from labirinto import Labirinto
from select_position import Select_Position


import platform
import os
class Config:
    def __init__(self):
        pass


    def Limpar(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')




class Trapped_Mouse(Select_Position,Config):
    def __init__(self):
        self.labirint = Labirinto()

    def __str__(self):
        
        while True:
            self,
            info =Select_Position().Move()
            if info == 'esc':
                break
            elif info == '5':
                print('enter')
                break

            if info != None:
                self.Limpar()
                print(info)
        return '0'


if __name__ == "__main__":
    Trapped_Mouse().__str__()


