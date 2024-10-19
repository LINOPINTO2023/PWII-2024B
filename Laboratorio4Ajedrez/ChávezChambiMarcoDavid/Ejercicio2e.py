from interpreter import draw
from chessPictures import *

linea2 = square.negative().join(square)
linea2 = linea2.horizontalRepeat(2)
draw(linea2)