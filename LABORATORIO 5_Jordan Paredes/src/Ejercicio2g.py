"""Author: JP-777"""

from interpreter import draw
from chessPictures import *

blanca = square
negra = square.negative()

fila_casillas = blanca.join(negra).horizontalRepeat(4)
fila_casillas_invertida = fila_casillas.negative()

fila_piezas_blancas = rock.superponer(blanca).join(knight.superponer(negra)).join(bishop.superponer(blanca)).join(queen.superponer(negra)).join(king.superponer(blanca)).join(bishop.superponer(negra)).join(knight.superponer(blanca)).join(rock.superponer(negra))

fila_peones_blancos = pawn.superponer(negra).join(pawn.superponer(blanca)).horizontalRepeat(4)

fila_piezas_negras = fila_piezas_blancas.negative()

fila_peones_negras = fila_peones_blancos.negative()

tablero_mitad = fila_casillas.up(fila_casillas_invertida).verticalRepeat(2).negative()

tablero_completo = fila_piezas_negras.up(fila_peones_negras).up(tablero_mitad).up(fila_peones_blancos).up(fila_piezas_blancas)

draw(tablero_completo)

