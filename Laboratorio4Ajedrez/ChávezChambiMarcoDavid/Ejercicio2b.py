from interpreter import draw
from chessPictures import *

knightWhite = knight.verticalMirror()
knightBlack = knight.negative().verticalMirror()
row1=knight.join(knight.negative())
row2=knightBlack.join(knightWhite)
matriz = row2.up(row1)
draw(matriz)