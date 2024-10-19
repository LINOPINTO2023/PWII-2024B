from interpreter import draw
from chessPictures import *

#Primer patrón (alfil, caballo y torre)
patron1 = bishop.join(knight).join(rock)
#Segundo patrón (reyna y rey)
patron2 = queen.join(king)
#Tercer patrón (8 peones)
patron3 = pawn.horizontalRepeat(8)

#Patrón de cuadrados (blanco y gris)
patronTablero1 = (square.join(square.negative())).horizontalRepeat(4)
#Patrón de cuadrados (gris y blanco)
patronTablero2 = patronTablero1.negative()
#Patrón unido
patronTableroUnido = patronTablero2.up(patronTablero1)

#PIEZAS BLANCAS
filaPeonesBlancos = patron3.under(patronTablero1)
filaBlancos = ((patron1.verticalMirror()).join(patron2).join(patron1)).under(patronTablero2)
grupoBlanco = filaBlancos.up(filaPeonesBlancos)

#PIEZAS NEGRAS
filaPeonesNegros = filaPeonesBlancos.negative()
filaNegros = filaBlancos.negative()
grupoNegro = filaPeonesNegros.up(filaNegros)

#Imprimimos tablero
draw(grupoBlanco.up(patronTableroUnido.verticalRepeat(2)).up(grupoNegro))