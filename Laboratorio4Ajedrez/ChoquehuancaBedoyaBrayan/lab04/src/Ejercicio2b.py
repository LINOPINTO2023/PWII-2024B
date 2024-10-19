from chessPictures import *
from interpreter import draw

tab = knight
tab = Picture.join(tab, Picture.negative(knight))
tab = Picture.up(Picture.verticalMirror(tab), tab)
draw(tab)
