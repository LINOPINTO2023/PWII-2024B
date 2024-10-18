"""Author: JP-777"""

from interpreter import draw
from chessPictures import *

blancoYnegro = square.join(square.negative())
fila_casillas = blancoYnegro.horizontalRepeat(4)
draw(fila_casillas)