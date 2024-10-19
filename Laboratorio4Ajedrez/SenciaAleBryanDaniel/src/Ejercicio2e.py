from interpreter import draw
from chessPictures import *
from picture import Picture

tableroDos = ((square.negative()).join(square)).horizontalRepeat(4)
draw(tableroDos)