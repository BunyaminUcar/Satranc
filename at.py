
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