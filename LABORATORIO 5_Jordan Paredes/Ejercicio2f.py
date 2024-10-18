"""Author: JP-777"""

from interpreter import draw
from chessPictures import *

blancoYnegro = square.join(square.negative())
fila_casillas2 = blancoYnegro.horizontalRepeat(4)
negroYblanco = square.negative().join(square)
fila_casillas1 = negroYblanco.horizontalRepeat(4)

tablero_mitad = fila_casillas1.up(fila_casillas2).verticalRepeat(2)
draw(tablero_mitad)