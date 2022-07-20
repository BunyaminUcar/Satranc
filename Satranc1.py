engel=[(5,1),(4,6),(2,6),(1,4),(1,8),(8,1),(8,8)]

deger=63
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


#At için muhtemel hareket koordinatları
x=5
y=4
At=[]
At.append((x + 2, y - 1))
At.append((x + 2, y + 1))
At.append((x - 2, y + 1))
At.append((x - 2, y - 1))
At.append((x + 1, y + 2))
At.append((x + 1, y - 2))
At.append((x - 1, y + 2))
At.append((x - 1, y - 2))

y=[i for i in At if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]



print("At :",y)


#Fil için muhtemel hareket koordinatları

x=1
y=1
fil=[]

for n in range(1,8):
    fil.append((x+n, y+n))
    fil.append((x-n, y-n))
    fil.append((x-n, y+n))
    fil.append((x+n, y-n))


y1=[i for i in fil if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]

print("Fil :",y1)
#Şah için muhtemel hareket koordinatları

x=5
y=4
sah=[]
sah.append((x+1, y))
sah.append((x-1, y))
sah.append((x+1, y+1))
sah.append((x-1, y-1))
sah.append((x-1, y+1))
sah.append((x+1, y-1))
sah.append((x, y+1))
sah.append((x, y-1))

y2=[i for i in sah if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]

print("Sah :",y2)
#Kale için muhtemel hareket koordinatları

x=5
y=4

engel_x=4
engel_y=4

kale=[]
for n in range(1,8):
   
    kale.append((x, y+n))
    kale.append((x, y-n))
    kale.append((x+n, y))
    kale.append((x-n, y))

y3=[i for i in kale if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]
print("Kale  :",y3)



#Vezir için muhtemel hareket koordinatları
x=1
y=1
vezir=[]
for n in range(1,8):
    vezir.append((x+n, y+n))
    vezir.append((x-n, y-n))
    vezir.append((x-n, y+n))
    vezir.append((x+n, y-n))
    vezir.append((x, y+n))
    vezir.append((x, y-n))
    vezir.append((x+n, y))
    vezir.append((x-n, y))

y4=[i for i in vezir if all([ 0<i[0]<9 , 0<i[1]<9 ]) and i not in engel]

print("Vezir :",y4)
