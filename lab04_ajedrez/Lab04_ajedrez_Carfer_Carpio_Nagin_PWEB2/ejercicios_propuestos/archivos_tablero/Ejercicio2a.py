from interpreter import draw
from chessPictures import *
# Aqui la primera fila, caballo blanco y caballo negro
row1 = knight.negative().join(knight)


# Aqui la segunda fila, caballo negro y caballo blanco
row2 = knight.join(knight.negative())

# aqui unimos las anteriores filas verticalmente
row3= row2.under(row1)

# Dibujamos, ademas de haber puesto la dimension de 120 x 120 para que se acomode al dibujo
draw(row3, 120, 120)