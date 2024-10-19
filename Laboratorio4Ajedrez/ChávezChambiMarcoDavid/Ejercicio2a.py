from interpreter import draw
from chessPictures import *

row1 = knight.join(knight.negative())
row2 = knight.negative().join(knight)
matriz = row2.up(row1)
draw(matriz)
