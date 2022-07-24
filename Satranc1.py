from barrier import *
from at import knightMovement
from king import kingMovement
from rook import rookMovement
from bishop import bishopMovement
from queen import QueenMovement

x=int(input("X: "))
y=int(input("Y: "))
#At için muhtemel hareket koordinatları

knight_movement=[i for i in knightMovement(x,y) if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]
print("At :",knight_movement)


#Fil için muhtemel hareket koordinatları

bishop_movement=[i for i in bishopMovement(x,y) if all([ 0<i[0]<9 , 0<i[1]<9 ])]
print("Fil :",bishop_movement)


#Şah için muhtemel hareket koordinatları

king_movement=[i for i in kingMovement(x,y) if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]
print("Sah :",king_movement)



#Kale için muhtemel hareket koordinatları

rook_movement=[i for i in rookMovement(x,y) if all([ 0<i[0]<9 , 0<i[1]<9 ])]
print("Kale  :",rook_movement)


#Vezir için muhtemel hareket koordinatları

queen_movement=[i for i in QueenMovement(x,y) if all([ 0<i[0]<9 , 0<i[1]<9 ])]
print("Vezir :",queen_movement)



   
