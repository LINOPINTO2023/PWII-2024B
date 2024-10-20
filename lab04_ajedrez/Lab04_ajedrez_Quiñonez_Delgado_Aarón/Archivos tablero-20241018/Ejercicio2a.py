from interpreter import draw
from chessPictures import *
from picture import *

#Caballo blanco con caballo negro
caballos = knight.join(knight.negative())
draw(caballos.negative().up(caballos))