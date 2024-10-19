from interpreter import draw
from chessPictures import *
#Fila de cuadrados blancos y negros, primera forma
row= square.join(square.negative()).horizontalRepeat(4)

draw(row, 463, 58)