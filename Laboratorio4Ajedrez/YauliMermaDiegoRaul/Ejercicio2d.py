from interpreter import draw
from chessPictures import *
casilla = square
duo=Picture.join(casilla, Picture.negative(casilla))
fila1=Picture.horizontalRepeat(duo, 4)
draw(fila1)
