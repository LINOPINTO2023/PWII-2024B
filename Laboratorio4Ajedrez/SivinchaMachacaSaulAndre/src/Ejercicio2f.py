from interpreter import draw
from chessPictures import *

neg = square.negative()
row = square.join(neg).join(square).join(neg)
row = row.join(row)

negativeRow = row.negative()

draw(row.up(negativeRow).verticalRepeat(2))