import keyboard  # using module keyboard
from labirinto import Labirinto

class Select_Position():

    def __init__(self):
        self.__labirint = Labirinto()

    def Move(self):
        if keyboard.is_pressed('left'):  #<- if key 'q' is pressed 

            return 4
        if keyboard.is_pressed('right'):  #-> if key 'q' is pressed 

            return 6 
        if keyboard.is_pressed('up'):  #-> if key 'q' is pressed 

            return 8  
        if keyboard.is_pressed('down'):  #-> if key 'q' is pressed 

            return 2
        if keyboard.is_pressed('esc'):  #-> if key 'q' is pressed 

            return 'esc'
        if keyboard.is_pressed('enter'):  #-> if key 'q' is pressed 

            return 5




'''while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('left'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break



while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.get_hotkey_name():  # if key 'q' is pressed 
            print(keyboard.get_hotkey_name())
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
'''

