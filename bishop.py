from barrier import *
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


