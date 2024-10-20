from interpreter import draw
from chessPictures import *

row_1 = square.join(square.negative()).horizontalRepeat(4)
board = row_1
draw(board)