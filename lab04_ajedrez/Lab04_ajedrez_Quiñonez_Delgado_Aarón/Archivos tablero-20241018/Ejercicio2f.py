from interpreter import draw
from chessPictures import *

#Patron de cuadrado blanco y cuadrado gris
patron = square.join(square.negative())
#Patron de linea completo
patronLinea = patron.horizontalRepeat(4)
#Patron de linea completo negativo
patronLineaNegativo = patronLinea.negative()
draw((patronLineaNegativo.up(patronLinea)).verticalRepeat(2))