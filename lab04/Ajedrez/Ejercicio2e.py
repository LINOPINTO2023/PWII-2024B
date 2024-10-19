from interpreter import draw
from chessPictures import *
cuadrado_gris = square
cuadrado_gris_oscuro = square.negative()
fila = cuadrado_gris_oscuro.join(cuadrado_gris)
resultado = fila.horizontalRepeat(4)
draw(resultado)