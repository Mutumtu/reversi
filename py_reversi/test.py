from board import Board
from player import Player

ttt = Board()

# print(ppp.color())

# for i in range(8):
#     for j in range(8):
#         ttt.check_range(ttt.player1, i, j)
# ttt.check_range(ttt.player1, 4, 2)
# ttt.table[2][4] = ttt.player2.color()
# ttt.put(ttt.player1, 4, 1)

ttt.table[5][4] = ttt.player1.color()
# ttt.table[2][5] = ttt.player2.color()
# ttt.check_range(ttt.player1, 2, 5)
ttt.put(ttt.player2, 4, 6)

print(ttt)
