from interpreter import draw
from chessPictures import *

# Crear cuadros del tablero
casilla = square
casillaNegativa = square.negative()

# Fila de piezas blancas (parte inferior del tablero)
filaPiezasBlancas = rock.under(casilla).join(knight.under(casillaNegativa)).join(bishop.under(casilla)).join(queen.under(casillaNegativa)).join(king.under(casilla)).join(bishop.under(casillaNegativa)).join(knight.under(casilla)).join(rock.under(casillaNegativa))

# Fila de peones blancos
filaPeonesBlancos = pawn.under(casillaNegativa).join(pawn.under(casilla)).join(pawn.under(casillaNegativa)).join(pawn.under(casilla)).join(pawn.under(casillaNegativa)).join(pawn.under(casilla)).join(pawn.under(casillaNegativa)).join(pawn.under(casilla))

# Fila de piezas negras (parte superior del tablero)
filaPiezasNegras = filaPiezasBlancas.negative()
# Fila de peones negros
filaPeonesNegros = filaPeonesBlancos.negative()

# Crear las filas vacías del tablero (parte central del tablero)
cuadro = square.join(casillaNegativa)
row1 = cuadro.horizontalRepeat(2)
cuadro = casillaNegativa.join(square)
row2 = cuadro.horizontalRepeat(2)
patron = row2.up(row1)
patron = patron.verticalRepeat(1)

# Combinar todas las filas para formar el tablero completo con piezas
tablero = (filaPiezasNegras.up(filaPeonesNegros).up(patron).up(filaPeonesBlancos).up(filaPiezasBlancas))

# Dibujar el tablero con las piezas
draw(tablero)
