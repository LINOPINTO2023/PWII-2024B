"""Author: JP-777"""

from interpreter import draw
from chessPictures import *

figura1 = knight.join(knight.negative()).verticalMirror()
fila2 = knight.join(knight.negative())
figura1 = figura1.up(fila2)
draw(figura1)