from archivos_ajedrez.chessPictures import *
from archivos_ajedrez.interpreter import draw
from archivos_ajedrez.picture import *

#Fichas blancas
torre_blanca = square.negative().under(Picture(ROCK))
caballo_blanco = square.under(Picture(KNIGHT))
alfil_blanco = square.negative().under(Picture(BISHOP))
reina_blanca = square.under(Picture(QUEEN))
rey_blanco = square.negative().under(Picture(KING))
alfil_blanco2 = square.under(Picture(BISHOP))
caballo_blanco2 = square.negative().under(Picture(KNIGHT))
torre_blanca2 = square.under(Picture(ROCK))
peon_blanco = square.under(Picture(PAWN))
peon_blanco2 = square.negative().under(Picture(PAWN))

primera_fila_blanca = torre_blanca.join(caballo_blanco).join(alfil_blanco).join(reina_blanca).join(rey_blanco).join(alfil_blanco2).join(caballo_blanco2).join(torre_blanca2)
segunda_fila_blanca = (peon_blanco.join(peon_blanco2)).horizontalRepeat(4)

blancas = primera_fila_blanca.up(segunda_fila_blanca)

#draw(blancas)

#Fichas negras
torre_negra = square.under(Picture(ROCK).negative())
caballo_negro = square.negative().under(Picture(KNIGHT).negative())
alfil_negro = square.under(Picture(BISHOP).negative())
reina_negra = square.negative().under(Picture(QUEEN).negative())
rey_negro = square.under(Picture(KING).negative())
alfil_negro2 = square.negative().under(Picture(BISHOP).negative())
caballo_negro2 = square.under(Picture(KNIGHT).negative())
torre_negra2 = square.negative().under(Picture(ROCK).negative())
peon_negro = square.under(Picture(PAWN).negative())
peon_negro2 = square.negative().under(Picture(PAWN).negative())

primera_fila_negra = peon_negro2.join(peon_negro).horizontalRepeat(4)
segunda_fila_negra = torre_negra.join(caballo_negro).join(alfil_negro).join(reina_negra).join(rey_negro).join(alfil_negro2).join(caballo_negro2).join(torre_negra2)

negras = primera_fila_negra.up(segunda_fila_negra)
#draw(negras)

#squares
casilla_abajo = Picture(SQUARE).negative().join(Picture(SQUARE)).horizontalRepeat(4)
casilla_encima = Picture(SQUARE).join(Picture(SQUARE).negative()).horizontalRepeat(4)
casilla_espacio = casilla_abajo.up(casilla_encima).verticalRepeat(2)
#draw(casilla_espacio)

#Casilla final
casilla_final = blancas.up(casilla_espacio).up(negras)
draw(casilla_final)