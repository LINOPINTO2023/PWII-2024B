from interpreter import draw
from chessPictures import *

box_white = square
box_black = box_white.negative()
box_wb = box_white.join(box_black)
row_1 = box_wb.horizontalRepeat(4)
board = row_1
draw(board)