from interpreter import draw
from chessPictures import *
#Fila primera forma
row= square.join(square.negative()).horizontalRepeat(4)
#Fila segunda forma
row2= square.negative().join(square).horizontalRepeat(4)
#Union de filas
row3 = row.under(row2).verticalRepeat(2)
draw(row3, 463, 232 )