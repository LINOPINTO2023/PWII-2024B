from interpreter import draw
from chessPictures import *

eb = Picture(SQUARE)
en = eb.negative()

draw(eb.join(en).horizontalRepeat(4))