from interpreter import draw
from chessPictures import *

filanegro = square.under(square.negative()).join(square.negative().under(square)).horizontalRepeat(4).verticalRepeat(1).superponer(pawn.negative().horizontalRepeat(8).under(rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock).negative()))

filablanca = square.under(square.negative()).join(square.negative().under(square)).horizontalRepeat(4).verticalRepeat(3).superponer(rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock).under(pawn.horizontalRepeat(8)))

tablero_de_Ajedrez = filablanca.under(filanegro)
draw(tablero_de_Ajedrez)