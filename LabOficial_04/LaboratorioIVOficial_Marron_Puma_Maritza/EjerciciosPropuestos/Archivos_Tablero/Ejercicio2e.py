from interpreter import draw
from chessPictures import *

box_white = square
box_black = box_white.negative()
box_bw = box_black.join(box_white)
row_1 = box_bw.horizontalRepeat(4)
board = row_1
draw(board)