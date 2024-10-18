from interpreter import draw
from chessPictures import *
from picture import Picture
from colors import *

casilla = square
dupla = Picture.join(casilla.negative(), casilla)
tablero = Picture.horizontalRepeat(dupla, 4)

draw(tablero)
