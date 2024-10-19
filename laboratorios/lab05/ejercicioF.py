from interpreter import draw
from chessPictures import *
from picture import *

cuaB=square
cuaN=square.negative()
tot=[]
for i in range(8):
    if(i%2==0):
        tot.append(cuaN)
    else:
        tot.append(cuaB)

nuevo=tot[0]
con=1
while(con<8):
    nuevo=nuevo.join(tot[con])
    con+=1
draw(nuevo.up(nuevo.negative()).verticalRepeat(2))