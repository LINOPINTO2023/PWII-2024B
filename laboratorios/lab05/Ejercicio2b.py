from interpreter import draw
from chessPictures import *
from picture import *

draw(knight.verticalMirror().negative()
     .up(knight).join(knight.verticalMirror().up(knight.negative())))

#draw(knight.verticalMirror())