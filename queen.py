from barrier import *
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

