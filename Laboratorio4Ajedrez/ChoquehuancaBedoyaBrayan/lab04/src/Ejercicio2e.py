from interpreter import draw
from chessPictures import *

eb = Picture(SQUARE)
en = eb.negative()

draw(en.join(eb).horizontalRepeat(4))