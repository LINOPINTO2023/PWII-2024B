from interpreter import draw
from chessPictures import *
caballo = knight
fila = Picture.join(caballo, Picture.negative(caballo)) 
draw(Picture.up(Picture.negative(fila), fila))
