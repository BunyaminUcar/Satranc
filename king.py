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


