from chessPictures import *
from interpreter import draw
from picture import Picture
from colors import *

#Ejercicio g tableor completo

filaInicial = Picture.under(rock, Picture.negative(square))

filaInicial = Picture.join(filaInicial, Picture.under(knight, square))
filaInicial = Picture.join(filaInicial, Picture.under(bishop, Picture.negative(square)))
filaInicial = Picture.join(filaInicial, Picture.under(queen, square))
filaInicial = Picture.join(filaInicial, Picture.under(king, Picture.negative(square)))
filaInicial = Picture.join(filaInicial, Picture.under(bishop, square))
filaInicial = Picture.join(filaInicial, Picture.under(knight, Picture.negative(square)))
filaInicial = Picture.join(filaInicial, Picture.under(rock, square))

filaNegro = Picture.negative(filaInicial)

filaPeon = Picture.under(pawn, square)
filaPeon = Picture.join(filaPeon, Picture.under(pawn, Picture.negative(square)))
filaPeon = Picture.horizontalRepeat(filaPeon, 4)

tabla1 = square
tabla1 = Picture.join(tabla1, Picture.negative(square))
tabla1 = (Picture.horizontalRepeat(tabla1, 4))
tabla2 = Picture.negative(tabla1)
tabla3 = Picture.verticalRepeat(Picture.up(tabla2, tabla1), 2)

tablero = Picture.up(Picture.negative(filaPeon), filaNegro)
tablero = Picture.up(tabla3, tablero)
tablero = Picture.up(filaPeon, tablero)
tablero = Picture.up(filaInicial, tablero)

draw(tablero)