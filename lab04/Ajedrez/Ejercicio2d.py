from interpreter import draw
from chessPictures import *
cuadrado_gris = square
cuadrado_gris_oscuro = square.negative()
fila = cuadrado_gris.join(cuadrado_gris_oscuro)
resultado = fila.horizontalRepeat(4)
draw(resultado)