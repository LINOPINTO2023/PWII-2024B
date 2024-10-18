from interpreter import draw
from chessPictures import *

tableroUno = (square.join(square.negative())).horizontalRepeat(4)
draw(tableroUno)