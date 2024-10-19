from archivos_ajedrez.chessPictures import *
from archivos_ajedrez.interpreter import draw
from archivos_ajedrez.picture import *

draw(knight.negative().verticalMirror().join(knight.verticalMirror()).up(knight).join(knight.negative()))