
import keyboard as kb
pressionou = False

while pressionou == False:
    if kb.is_pressed('e'):
        pressionou = True
        print('Pressionou e')

