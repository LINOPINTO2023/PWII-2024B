from interpreter import draw
from chessPictures import *
from picture import *

figura1 = knight.negative().join(knight)
fila2 = knight.join(knight.negative())
figura1 = figura1.up(fila2)
draw(figura1)