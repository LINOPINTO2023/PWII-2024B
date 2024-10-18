from interpreter import draw
from chessPictures import *
from picture import Picture
from colors import *

casilla = square
dupla = Picture.join(casilla, casilla.negative())
tablero = Picture.horizontalRepeat(dupla, 4)
tablero2 = Picture.negative(tablero)
tablero3 = Picture.under(tablero, tablero2)

draw(tablero3.verticalRepeat(2))
