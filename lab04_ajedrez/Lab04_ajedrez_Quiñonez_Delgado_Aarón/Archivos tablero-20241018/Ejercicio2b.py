from interpreter import draw
from chessPictures import *

#Caballo blanco con caballo negro
caballos = knight.join(knight.negative())

draw(caballos.verticalMirror().up(caballos))