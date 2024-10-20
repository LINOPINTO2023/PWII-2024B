from interpreter import draw
from chessPictures import *

row_whiteFirst = square.join(square.negative()).horizontalRepeat(4)
row_blackFirst = square.negative().join(square).horizontalRepeat(4)
chess_board = row_whiteFirst.under(row_blackFirst).verticalRepeat(2)
draw(chess_board)