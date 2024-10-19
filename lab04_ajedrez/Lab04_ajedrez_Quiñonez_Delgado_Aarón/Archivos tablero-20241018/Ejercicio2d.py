from interpreter import draw
from chessPictures import *
from picture import *

#Patron de cuadrado blanco y cuadrado gris
patron = square.join(square.negative())
draw(patron.horizontalRepeat(4))