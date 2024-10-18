from interpreter import draw
from chessPictures import *
from picture import Picture
from colors import *

casB = square
casN = casB.negative()

dupla1 = Picture.join(casN.up(rock), casB.up(knight))
dupla2 = Picture.join(casN.up(bishop), casB.up(queen))
dupla3 = Picture.join(casN.up(king), casB.up(bishop))
dupla4 = Picture.join(casN.up(knight), casB.up(rock))
fila1 = dupla1.join(dupla2).join(dupla3).join(dupla4)
dupla5 = Picture.join(casB.up(pawn), casN.up(pawn))
fila2 = dupla5.horizontalRepeat(4)
fila3 = Picture.join(casN, casB).horizontalRepeat(4)

tablero1 = fila1.negative().under(fila2.negative())
tablero2 = (fila3.negative().under(fila3)).verticalRepeat(2)
tablero3 = fila2.under(fila1)


draw(tablero1.under(tablero2).under(tablero3))
