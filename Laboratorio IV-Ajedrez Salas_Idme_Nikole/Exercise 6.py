from Modules_Chess.chessPictures import *
from Modules_Chess.interpreter import draw
d = (square.join(square.negative()).horizontalRepeat(4))
draw((d.up(d.negative())).verticalRepeat(2))