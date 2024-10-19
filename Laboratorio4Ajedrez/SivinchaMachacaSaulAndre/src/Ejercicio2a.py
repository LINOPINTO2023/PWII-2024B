from chessPictures import *
from interpreter import draw

row1 = knight.join(knight.negative())
row2 = knight.negative().join(knight)
result = row1.up(row2)
draw(result)