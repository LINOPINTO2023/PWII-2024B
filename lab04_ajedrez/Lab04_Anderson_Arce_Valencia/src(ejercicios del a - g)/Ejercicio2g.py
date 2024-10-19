from interpreter import draw
from chessPictures import *

Piezas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock) #Union de fichas torre/caballo/alfil/reina/rey/..
peones= pawn.horizontalRepeat(8) #Peones
tablero = square.under(square.negative()).join(square.negative().under(square)).horizontalRepeat(4) #Tablero 8x2

filanegro = tablero.verticalRepeat(1).superponer(peones.negative().under(Piezas.negative()))
filablanca = tablero.verticalRepeat(3).superponer(Piezas.under(peones))
tablero_de_Ajedrez = filablanca.under(filanegro)

draw(tablero)