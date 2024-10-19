from interpreter import draw
from chessPictures import *
caballo_blanco = knight
caballo_negro = knight.negative()
fila = caballo_blanco.join(caballo_negro)
caballo_espejado_blanco = knight.verticalMirror()
caballo_espejado_negro = knight.negative().verticalMirror()
fila_invertida = caballo_espejado_blanco.join(caballo_espejado_negro)
resultado = fila.up(fila_invertida)
draw(resultado)