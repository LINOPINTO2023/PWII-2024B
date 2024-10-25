from interpreter import draw
from chessPictures import *

fila1 = square.negative().join(square).horizontalRepeat(4).up(square.join(square.negative()).horizontalRepeat(4))
fila2 = square.negative().join(square).horizontalRepeat(4).up(square.join(square.negative()).horizontalRepeat(4))
mtablero = fila2.up(fila1)
draw(mtablero)