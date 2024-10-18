from interpreter import draw
from chessPictures import *
from picture import Picture
from colors import *

pieza = knight
dupla = Picture.join(pieza, pieza.negative())
tablero = Picture.under(dupla.negative(), dupla)


draw(tablero)
