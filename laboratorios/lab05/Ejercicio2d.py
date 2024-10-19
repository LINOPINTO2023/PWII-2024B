from interpreter import draw
from chessPictures import *
from picture import *
#negamos primero
cuadrado1=square.negative()
cuadrado2=square
a=[]
for i in range(8):
    if i%2!=0:
        a.append(cuadrado1)
    else:
        a.append(cuadrado2)
lista=a[0]
cont=1
while(cont<8):
    lista=lista.join(a[cont])
    cont+=1
draw(lista)
