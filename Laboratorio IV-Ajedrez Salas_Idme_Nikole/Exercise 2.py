from Modules_Chess.chessPictures import *
from Modules_Chess.interpreter import draw
a = knight.join(knight.negative())
draw(a.up(a.horizontalMirror()))