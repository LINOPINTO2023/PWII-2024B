from interpreter import draw
from chessPictures import *
from picture import *

fila1 = knight.join((knight).negative())
fila2 = fila1.verticalMirror()
draw(fila1.up(fila2))