from barrier import *

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