#Başlangıç olarak muhtemel engellerden oluşan bir dizi tanımladık.
engel=[(4,5),(4,3),(6,6),(5,5),(4,6)]


deger=int(input("Bir değer giriniz:"))
while(deger<0):
    deger=int(input("Girdiğiniz değer 0 den büyük olmalıdır.Lütfen tekrar giriniz:"))
x_ekseni=8
y_ekseni=8

x_koordinat=deger%x_ekseni


if x_koordinat==0:
    x_koordinat=x_ekseni
if deger%y_ekseni==0:
    y_koordinat=int(deger/y_ekseni)
else: 
    y_koordinat=int(deger/y_ekseni)+1
print(x_koordinat)
print(y_koordinat)



def knightMovement(x,y):
    At=[]
    At.append((x + 2, y - 1))
    At.append((x + 2, y + 1))
    At.append((x - 2, y + 1))
    At.append((x - 2, y - 1))
    At.append((x + 1, y + 2))
    At.append((x + 1, y - 2))
    At.append((x - 1, y + 2))
    At.append((x - 1, y - 2))     
    return At




def kingMovement(x,y):
    sah=[]
    sah.append((x+1, y))
    sah.append((x-1, y))
    sah.append((x+1, y+1))
    sah.append((x-1, y-1))
    sah.append((x-1, y+1))
    sah.append((x+1, y-1))
    sah.append((x, y+1))
    sah.append((x, y-1))
    return sah




def QueenMovement(x,y):
    vezir=[]
    for n in range(1,8):
        if (x+n, y+n) in engel:
            break
        else:
            vezir.append((x+n, y+n))#sağ-üst çapraz
    for n in range(1,8):
        if (x-n, y-n) in engel:
            break
        else:
            vezir.append((x-n, y-n))#sol-alt çapraz
    for n in range(1,8):    
        if (x+n, y-n) in engel:
            break
        else:
            vezir.append((x+n, y-n))#sağ-alt çapraz
    for n in range(1,8):   
        if (x-n, y+n) in engel:
            break
        else:
            vezir.append((x-n, y+n))#sol-üst çapraz
    for n in range(1,8):
        if (x, y+n) in engel:
            break
        else:
            vezir.append((x, y+n))#üste doğru hareket
    for n in range(1,8):
        if (x, y-n) in engel:
            break
        else:
            vezir.append((x, y-n))#alta doğru hareket
    for n in range(1,8):
        if (x+n, y) in engel:
            break
        else:
            vezir.append((x+n, y))#sağa doğru hareket
    for n in range(1,8):
        if (x-n, y) in engel:
            break
        else:
            vezir.append((x-n, y))#sola doğru hareket

    return vezir


def bishopMovement(x,y):

    fil=[]

    for n in range(1,8):
        if (x+n, y+n) in engel:
            break
        else:
            fil.append((x+n, y+n))#sağ-üst çapraz
    for n in range(1,8):
        if (x-n, y-n) in engel:
            break
        else:
            fil.append((x-n, y-n))#sol-alt çapraz
    for n in range(1,8):
        
        if (x+n, y-n) in engel:
            break
        else:
            fil.append((x+n, y-n))#sağ-alt çapraz
    for n in range(1,8):
       
        if (x-n, y+n) in engel:
            break
        else:
            fil.append((x-n, y+n))#sol-üst çapraz
    return fil


def rookMovement(x,y):
    kale=[]
    for n in range(1,8):
        if (x, y+n) in engel:
            break
        else:
            kale.append((x, y+n))#üste doğru hareket
    for n in range(1,8):
        if (x, y-n) in engel:
            break
        else:
            kale.append((x, y-n))#alta doğru hareket
    for n in range(1,8):
        if (x+n, y) in engel:
            break
        else:
            kale.append((x+n, y))#sağa doğru hareket
    for n in range(1,8):
        if (x-n, y) in engel:
            break
        else:
            kale.append((x-n, y))#sola doğru hareket

    return kale




#Piyon için muhtemel hareketler koordinatları

#At için muhtemel hareket koordinatları

at_liste=[i for i in knightMovement(5,4) if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]
print("At :",at_liste)


#Fil için muhtemel hareket koordinatları

bishopmovement=[i for i in bishopMovement(3,4) if all([ 0<i[0]<9 , 0<i[1]<9 ])]
print("Fil :",bishopmovement)


#Şah için muhtemel hareket koordinatları

sah_liste=[i for i in kingMovement(5,4) if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]
print("Sah :",sah_liste)



#Kale için muhtemel hareket koordinatları

rook_movement=[i for i in rookMovement(5,4) if all([ 0<i[0]<9 , 0<i[1]<9 ])]
print("Kale  :",rook_movement)


#Vezir için muhtemel hareket koordinatları

queenMovement=[i for i in QueenMovement(4,2) if all([ 0<i[0]<9 , 0<i[1]<9 ])]
print("Vezir :",queenMovement)
