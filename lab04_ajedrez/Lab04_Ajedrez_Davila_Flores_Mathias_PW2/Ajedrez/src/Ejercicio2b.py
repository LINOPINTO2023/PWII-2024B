from interpreter import draw
from chessPictures import *

horse_white = knight
horse_black = horse_white.negative()

row_1 = horse_white.join(horse_black)
row_2 = row_1.verticalMirror()

board = row_1.under(row_2)

draw(board)

