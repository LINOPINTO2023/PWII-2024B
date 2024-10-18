from interpreter import draw
from chessPictures import *
caballo = knight #Para tener mas familiaridad 
fila = Picture.join(caballo, Picture.negative(caballo)) 
draw(Picture.up(Picture.verticalMirror(fila), fila))
