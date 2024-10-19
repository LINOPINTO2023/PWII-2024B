from interpreter import draw
from chessPictures import *
from picture import *

cuadrilla1 = square.join(square.negative()).horizontalRepeat(4)
cuadrilla2 = square.negative().join(square).horizontalRepeat(4)
#fichas negras
peonesN = pawn.negative().horizontalRepeat(8)
fichasN = rock.join(knight.join(bishop.join(queen.join(king.join(bishop.join(knight.join(rock))))))).negative()
cuadroPeonN = cuadrilla2.under(peonesN)
cuadroFichasN = cuadrilla1.under(fichasN)
#fichas blancas
peonesB = pawn.horizontalRepeat(8)
fichasB = rock.join(knight.join(bishop.join(queen.join(king.join(bishop.join(knight.join(rock)))))))
cuadroPeonB = cuadrilla1.under(peonesB)
cuadroFichasB = cuadrilla2.under(fichasB)
#tablero de guerra
accion = cuadrilla2.up(cuadrilla1).verticalRepeat(2)
#tableronegro
tablaN = cuadroPeonN.up(cuadroFichasN)
#tableroblanco
tablaB = cuadroFichasB.up(cuadroPeonB)
#tablero de ajedrez
ajedrez = tablaB.up(accion.up(tablaN))
draw(ajedrez)