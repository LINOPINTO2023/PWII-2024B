from interpreter import draw
from chessPictures import *


firstWhiteRow = (rock.under(square.negative())).join(knight.under(square)).join(bishop.under(square.negative()))
repeatWhiteRow = (bishop.under(square.negative())).join(knight.under(square)).join(rock.under(square.negative()))
whitePiecesRow = firstWhiteRow.join(queen.under(square)).join(king.under(square.negative())).join(repeatWhiteRow)
blackPiecesRow = whitePiecesRow.negative()
whitePawnsRow = (pawn.under(square)).join(pawn.under(square.negative())).horizontalRepeat(4)
blackPawnsRow = whitePawnsRow.negative()
emptyRow = (square.join(square.negative())).horizontalRepeat(4)
emptyRows = emptyRow.up(emptyRow.negative()).verticalRepeat(2)

chessBoard = blackPiecesRow.up(blackPawnsRow).up(emptyRows).up(whitePawnsRow).up(whitePiecesRow)

draw(chessBoard)
