from interpreter import draw
from chessPictures import *
cuadrado_gris = square
cuadrado_gris_oscuro = square.negative()
fila1 = cuadrado_gris.join(cuadrado_gris_oscuro).horizontalRepeat(4)
fila2 = cuadrado_gris_oscuro.join(cuadrado_gris).horizontalRepeat(4)
resultado = fila1.up(fila2).verticalRepeat(2)
draw(resultado)
