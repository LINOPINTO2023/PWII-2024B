from interpreter import draw
from chessPictures import *

primBlancas = (rock.under(square.negative())).join(knight.under(square)).join(bishop.under(square.negative())) 
repetBlancas = (bishop.under(square)).join(knight.under(square.negative)).join(rock.under(square))
filaBlancas = primBlancas.join(queen.under(square)).join(king.under(square.negative())).join(repetBlancas)
filaNegras = filaBlancas.negative()
filapeonesBlancos = (pawn.under(square)).join(pawn.under(square.negative())).horizontalRepeat(4)
filapeonesNegros = ((pawn.under(square)).join(pawn.under(square.negative())).horizontalRepeat(4)).negative()
filaSinFichas = ((square.join(square.negative())).horizontalRepeat(4))
tabSinFichas = (filaSinFichas.up(filaSinFichas.negative())).verticalRepeat(2)
tablero = (filaNegras.up(filapeonesNegros).up(tabSinFichas).up(filapeonesBlancos).up(filaBlancas))
draw(tablero)
