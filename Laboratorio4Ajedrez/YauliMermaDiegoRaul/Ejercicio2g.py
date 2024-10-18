from interpreter import draw
from chessPictures import *
torreBlanca = rock
caballoBlanco = knight
alfilBlanco = bishop
reinaBlanca = queen
reyBlanco = king
peonBlanco = pawn
peonNegro = pawn.negative()
casilla = square

# Posición de las piezas blancas
primBlancas = (torreBlanca.under(casilla.negative())).join(caballoBlanco.under(casilla)).join(alfilBlanco.under(casilla.negative()))
filaBlancas = primBlancas.join(reinaBlanca.under(casilla)).join(reyBlanco.under(casilla.negative()))

# Repetir torres y caballos en la fila
repetBlancas = (alfilBlanco.under(casilla)).join(caballoBlanco.under(casilla.negative())).join(torreBlanca.under(casilla))

# Colocar las piezas blancas completas
filaBlancas = filaBlancas.join(repetBlancas)

# Crear la fila de piezas negras
filaNegras = filaBlancas.negative()

# Crear filas de peones
filapeonesBlancos = (peonBlanco.under(casilla)).join(peonBlanco.under(casilla.negative())).horizontalRepeat(4)
filapeonesNegros = ((peonBlanco.under(casilla)).join(peonBlanco.under(casilla.negative())).horizontalRepeat(4)).negative()

# Crear filas vacías
filaSinFichas = (casilla.join(casilla.negative())).horizontalRepeat(4)
tabSinFichas = (filaSinFichas.up(filaSinFichas.negative())).verticalRepeat(2)

# Combinar todo el tablero
tablero = (filaNegras.up(filapeonesNegros).up(tabSinFichas).up(filapeonesBlancos).up(filaBlancas))

draw(tablero)

