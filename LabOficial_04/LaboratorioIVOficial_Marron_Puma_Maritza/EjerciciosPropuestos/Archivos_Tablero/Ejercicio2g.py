from interpreter import draw
from chessPictures import *

fila_piezas_negras = rock.negative().join(knight.negative().join(bishop.negative().join(queen.negative().join(king.negative().join(bishop.negative().join(knight.negative().join(rock.negative())))))))
fila_peones_negras = pawn.negative().horizontalRepeat(8)

fila_piezas_blancas = rock.join(knight.join(bishop.join(queen.join(king.join(bishop.join(knight.join(rock)))))))
fila_peones_blancas = pawn.horizontalRepeat(8)

fila_inicial_blanca = square.join(square.negative()).horizontalRepeat(4)
fila_inicial_negra = square.negative().join(square).horizontalRepeat(4)
filas_vacias_repetidas = fila_inicial_blanca.under(fila_inicial_negra).verticalRepeat(2)

fila_superior_piezas = fila_inicial_blanca.up(fila_piezas_negras)
fila_superior_peones = fila_inicial_negra.up(fila_peones_negras)
fila_inferior_peones = fila_inicial_blanca.up(fila_peones_blancas)
fila_inferior_piezas = fila_inicial_negra.up(fila_piezas_blancas)

tablero_ajedrez = fila_superior_piezas.under(fila_superior_peones.under(filas_vacias_repetidas.under(fila_inferior_peones.under(fila_inferior_piezas))))
draw(tablero_ajedrez)
