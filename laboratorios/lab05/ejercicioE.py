from interpreter import draw
from chessPictures import *
from picture import *

cuadradoB=square
cuadradoN=square.negative()
total=[]
for i in range(8):
    if(i%2==0):
        total.append(cuadradoN)
    else:
        total.append(cuadradoB)
nuevo3=total[0]
cont=1
while(cont<8):
    nuevo3=nuevo3.join(total[cont])
    cont+=1
draw(nuevo3)