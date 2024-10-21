from interpreter import draw
from chessPictures import *

eb = Picture(SQUARE)
en = eb.negative()
fila1 = eb.join(en).horizontalRepeat(4)
fila2 = en.join(eb).horizontalRepeat(4)
imagen = fila2.up(fila1).verticalRepeat(2)
draw(imagen)