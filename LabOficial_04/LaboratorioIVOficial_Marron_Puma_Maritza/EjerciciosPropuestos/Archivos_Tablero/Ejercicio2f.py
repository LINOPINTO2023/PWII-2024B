from interpreter import draw
from chessPictures import *

box_white = square
box_black = box_white.negative()
box_wb = box_white.join(box_black)
box_bw = box_wb.negative()
row_firstWhite = box_wb.horizontalRepeat(4)
row_firstBlack = box_bw.horizontalRepeat(4)
union_of_rows = row_firstWhite.under(row_firstBlack)
board = union_of_rows.verticalRepeat(2)
draw(board)