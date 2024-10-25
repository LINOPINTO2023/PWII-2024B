from interpreter import draw
from chessPictures import *
#Fila de cuadrados blancos y negros, segunda forma
row= square.negative().join(square).horizontalRepeat(4)

draw(row, 463, 55)