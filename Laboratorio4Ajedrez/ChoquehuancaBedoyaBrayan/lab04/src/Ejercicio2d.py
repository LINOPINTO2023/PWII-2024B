from interpreter import draw
from chessPictures import *

eb = Picture(SQUARE)
en = eb.negativo()

draw(eb.join(en).horizontalRepeat(4))