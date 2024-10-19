from interpreter import draw
from chessPictures import *

cuadro = square.join(square.negative())
row1 = cuadro.horizontalRepeat(2)
cuadro = square.negative().join(square)
row2 = cuadro.horizontalRepeat(2)
patron = row2.up(row1)
patron = patron.verticalRepeat(1)
draw(patron)