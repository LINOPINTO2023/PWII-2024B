from interpreter import draw
from chessPictures import *

tablero = square.under(square.negative()).join(square.negative().under(square)).horizontalRepeat(4).verticalRepeat(4)
draw(tablero)