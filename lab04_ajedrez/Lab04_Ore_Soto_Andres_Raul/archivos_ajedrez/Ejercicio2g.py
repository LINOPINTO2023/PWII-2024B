from archivos_ajedrez.chessPictures import *
from archivos_ajedrez.interpreter import draw
from archivos_ajedrez.picture import *

#Fichas blancas
torre_blanca = square.under(Picture(ROCK))
caballo_blanco = square.under(Picture(KNIGHT))
alfil_blanco = square.under(Picture(BISHOP))
reina_blanca = square.under(Picture(QUEEN))
rey_blanco = square.under(Picture(KING))
peon_blanco = square.under(Picture(PAWN))

#Fichas negras
torre_negra = s