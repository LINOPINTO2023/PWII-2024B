from interpreter import draw
from chessPictures import *

#Patron de cuadrado gris y cuadrado blanco
patron = square.negative().join(square)
draw(patron.horizontalRepeat(4))