from labirinto import Labirinto
from select_position import Select_Position
class Trapped_Mouse(Select_Position):
    def __init__(self):
        self.labirint = Labirinto()

    def __str__(self):
        #[print(x,'\n') for x in self.labirint]
        print(Trapped_Mouse())
        return '0'


if __name__ == "__main__":
    
    Select_Position().Move('x')
    
