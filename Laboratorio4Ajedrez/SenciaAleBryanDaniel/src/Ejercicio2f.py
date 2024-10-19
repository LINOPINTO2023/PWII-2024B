from interpreter import draw
from chessPictures import *

filaUno = (square.join(square.negative())).horizontalRepeat(4)
filaDos = filaUno.negative()
tablero = filaUno.up(filaDos).verticalRepeat(2)
draw(tablero)
