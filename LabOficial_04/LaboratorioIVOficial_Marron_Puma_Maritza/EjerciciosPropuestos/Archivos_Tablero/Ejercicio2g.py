from interpreter import draw
from chessPictures import *  

pawn_white = pawn
tower_white = rock
horse_white = knight
bishop_white = bishop
king_white = king
queen_white = queen

royalty_white = queen_white.join(king_white)
special_tokens_white = (tower_white.join(horse_white.join(bishop_white.join(royalty_white.join(bishop_white.join(horse_white.join(tower_white)))))))
pawn_row_white = pawn_white.horizontalRepeat(8)

pawn_black = pawn_white.negative()
tower_black = tower_white.negative()
horse_black = horse_white.negative()
bishop_black = bishop_white.negative()
king_black = king_white.negative()
queen_black = queen_white.negative()
royalty_black = queen_black.join(king_black)
special_tokens_black = (tower_black.join(horse_black.join(bishop_black.join(royalty_black.join(bishop_black.join(horse_black.join(tower_black)))))))
pawn_row_black = pawn_black.horizontalRepeat(8)

box_white = square
box_black = box_white.negative()
box_wb = box_white.join(box_black)
box_bw = box_wb.negative()
row_firstWhite = box_wb.horizontalRepeat(4)
row_firstBlack = box_bw.horizontalRepeat(4)
union_of_rows = row_firstWhite.under(row_firstBlack)

row_1 = row_firstWhite.up(special_tokens_black)
row_2 = row_firstBlack.up(pawn_row_black)
no_tokens = union_of_rows.verticalRepeat(2)
row_7 = row_firstWhite.up(pawn_row_white)
row_8 = row_firstBlack.up(special_tokens_white)
board = row_1.under(row_2.under(no_tokens.under(row_7.under(row_8))))
draw(board)