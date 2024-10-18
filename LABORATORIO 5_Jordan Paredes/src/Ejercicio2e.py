"""Author: JP-777"""

from interpreter import draw
from chessPictures import *

negroYblanco = square.negative().join(square)
fila_casillas = negroYblanco.horizontalRepeat(4)
draw(fila_casillas)