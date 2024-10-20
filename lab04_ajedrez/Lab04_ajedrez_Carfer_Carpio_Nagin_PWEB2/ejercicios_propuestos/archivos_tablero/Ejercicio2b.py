from interpreter import draw
from chessPictures import *
# primera fila
row1 = knight.join(knight.negative())

# segunda fila pero con verticalmirror
row2 = knight.join(knight.negative())
row3= row2.verticalMirror()

# union de las filas
final_pattern = row1.under(row3)

# dibujo
draw(final_pattern, 120, 120)