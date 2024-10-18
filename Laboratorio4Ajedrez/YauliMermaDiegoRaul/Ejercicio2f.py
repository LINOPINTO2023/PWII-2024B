from interpreter import draw
from chessPictures import *
casilla = square
duo=Picture.join(Picture.negative(casilla), casilla)
fila1=Picture.horizontalRepeat(duo, 4)
fila2=Picture.negative(fila1)
fila12=Picture.up(fila1, fila2)
draw(Picture.verticalRepeat(fila12, 2))