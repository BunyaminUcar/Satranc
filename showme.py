import colorama
from colorama import Fore
from Satranc1 import *
from barrier import *

tas=input("Tasınızı giriniz: ")



def showme(movement_list,x,y):
    for i in range(8,0,-1):
        for j in range (1,9):      
            if (j,i) in movement_list:
                print(Fore.GREEN+"◯",end=" ")   
            elif (j,i) in (engel):
                print(Fore.RED+"◯",end=" ")
            elif (x,y)==(j,i):
                print(Fore.LIGHTCYAN_EX+"◯",end=" ")
            else:
                print(Fore.WHITE+"◯",end=" ")
        print()


if(tas=="at"):
    showme(knight_movement,x,y)
elif(tas=="fil"):
    showme(bishop_movement,x,y)
elif(tas=="sah"):
    showme(king_movement,x,y)
elif(tas=="kale"):
    showme(rook_movement,x,y)
elif(tas=="vezir"):
    showme(queen_movement,x,y)
    
