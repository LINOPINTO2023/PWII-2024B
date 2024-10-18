from interpreter import draw
from chessPictures import *

#pruebas de picture
pieza = knight
pieza2 = queen
piezaJoin = Picture.join(pieza, pieza2)
draw(piezaJoin)