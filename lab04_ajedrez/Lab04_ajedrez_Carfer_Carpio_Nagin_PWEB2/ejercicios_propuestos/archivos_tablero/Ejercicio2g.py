from interpreter import draw
from chessPictures import *
#Fila de rey y reina torre caballo
row01= rock.negative().superponer().join(knight.superponer().negative()).join(bishop.negative().superponer()).join(queen.superponer().negative()).join(king.negative().superponer()).join(bishop.superponer().negative()).join(knight.negative().superponer()).join(rock.superponer().negative())
#Fila de peones
row02= pawn.superponer().negative().join(pawn.negative().superponer()).horizontalRepeat(4)

row03= row01.superponer().negative()
row04= row02.superponer().negative()
row06= square.join(square.negative()).horizontalRepeat(4)

row07= square.negative().join(square).horizontalRepeat(4)

row08 = row06.under(row07).verticalRepeat(2)

rowfinal=row01.under(row02).under(row08).under(row04).under(row03)


draw(rowfinal, 600, 500)