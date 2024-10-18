from interpreter import draw
from chessPictures import *

#pruebas de picture
pieza = knight
pieza2 = queen
piezaRepeat = Picture.verticalRepeat(pieza, 6)
draw(piezaRepeat)