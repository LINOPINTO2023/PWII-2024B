from interpreter import draw
from chessPictures import *
from picture import *

draw(knight.negative().up(knight).join(knight.up(knight.negative())))


#draw(knight.verticalRepeat(2).horizontalRepeat(2))
#draw(pawn.join(square.negative()))
#draw(queen.under(pawn.negative()))
#draw(square.join(square.negative()).horizontalRepeat(4))
#draw(pawn.verticalRepeat(3))
