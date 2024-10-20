from interpreter import draw
from chessPictures import *

row_1 = knight.join(knight.negative())
row_2 = row_1.negative()
board = row_1.under(row_2)
draw(board)