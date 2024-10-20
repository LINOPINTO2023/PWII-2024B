from interpreter import draw
from chessPictures import *

# ESCUADRA DEL TABLERO
cuadrado_gris = square
cuadrado_gris_oscuro = square.negative()
fila1 = cuadrado_gris.join(cuadrado_gris_oscuro).horizontalRepeat(4)
fila2 = cuadrado_gris_oscuro.join(cuadrado_gris).horizontalRepeat(4)
tablero = fila1.up(fila2).verticalRepeat(4)

# PIEZAS BLANCAS
caballo_blanco = knight
reina_blanco = queen
peon_blanco = pawn
alfil_blanco = bishop
rey_blanco = king
torre_blanco = rock

# PIEZAS NEGRAS
caballo_negro = knight.negative()
reina_negra = queen.negative()
peon_negro = pawn.negative()
alfil_negro = bishop.negative()
rey_negro = king.negative()
torre_negra = rock.negative()

# Fila de piezas negras
fila_negras = torre_negra.join(caballo_negro).join(alfil_negro).join(reina_negra).join(rey_negro).join(alfil_negro).join(caballo_negro).join(torre_negra)

# Fila de peones negros
fila_peones_negras = peon_negro.horizontalRepeat(8)

# Fila de piezas blancas
fila_blancas = torre_blanco.join(caballo_blanco).join(alfil_blanco).join(reina_blanco).join(rey_blanco).join(alfil_blanco).join(caballo_blanco).join(torre_blanco)

# Fila de peones blancas
fila_peones_blancas = peon_blanco.horizontalRepeat(8)

# Dibujar el tablero completo con todas las piezas
fila_tablero_negras = fila1.under(fila_negras)
fila_tablero_peones_negras = fila2.under(fila_peones_negras)
fila_tablero_blancas = fila1.under(fila_blancas)
fila_tablero_peones_blancas = fila2.under(fila_peones_blancas)
tablero_sin_piezas = fila1.up(fila2).verticalRepeat(2)
tablero_completo = fila_tablero_negras.up(fila_tablero_peones_negras).up(tablero_sin_piezas).up(fila_tablero_peones_blancas).up(fila_tablero_blancas)

draw(tablero_completo)
