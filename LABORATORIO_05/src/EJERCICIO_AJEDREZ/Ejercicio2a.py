from interpreter import draw
from chessPictures import *

#pruebas de picture
pieza = knight
pieza2 = queen
piezaUp = Picture.under(pieza, pieza2)
draw(piezaUp)