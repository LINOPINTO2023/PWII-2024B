from interpreter import draw
from chessPictures import *

row1 = knight.join(knight.negative())
row2 = row1.verticalMirror()
draw(row2.up(row1))