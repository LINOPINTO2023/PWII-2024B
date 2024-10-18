from interpreter import draw
from chessPictures import *

#pruebas de picture
pieza = knight
pieza2 = queen
piezaUp = Picture.up(pieza, pieza2)
draw(piezaUp)