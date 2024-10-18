from interpreter import draw
from chessPictures import *
from picture import Picture
from colors import *

pieza = queen
tablero = Picture.horizontalRepeat(pieza, 4)


draw(tablero)
