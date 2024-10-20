from piece import Piece
from player import Player
import numpy

class Board:
    def __init__(self):
        self.table = [["・" for _ in range(8)] for _ in range(8)]
        self.player1 = Player("player1", Player.SENTE)
        self.player2 = Player("player2", Player.GOTE)
        self.table[3][3], self.table[4][4] = self.player1.color(), self.player1.color()
        self.table[3][4], self.table[4][3] = self.player2.color(), self.player2.color()
        # self.piece = Piece


    def __str__(self):
        st = []
        for i in range(8):
            st.append("".join(self.table[i]))
        return "\n".join(st)

    def canput(self, player, x:int, y:int):
        if self.table[y][x] == "・" and bool(self.check_range(player, x, y)):
            return True
        else:
            return False

    def put(self, player, x: int, y: int):
        if self.canput(player, x, y):
            self.table[y][x] = player.color()
            self.turn(player, x, y, self.check_range(player, x, y))
        else:
            print("error")

    def check_range(self, player,  x: int, y: int):
        ans = []
        if player == self.player1:
            opponent = self.player2
        else:
            opponent = self.player1

        # 8方向をチェックする
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),         (0, 1),
                    (1, -1), (1, 0), (1, 1)]

        for yp, xp in directions:
            i = 1
            # 1方向に進みながらチェック
            while True:
                nx, ny = x + xp * i, y + yp * i
                # ボードの範囲外をチェック
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    break
                # 相手の色があるかをチェック
                if self.table[ny][nx] == opponent.color():
                    i += 1
                    continue
                # 自分の色があれば挟んでいるので有効な位置
                elif self.table[ny][nx] == player.color() and i > 1:
                    ans.append([nx, ny])
                    break
                else:
                    break

        print(ans)
        return ans

    def turn(self, player, x, y, putted:list):
        for i, j in putted:
            if x == i:
                sin = numpy.sign(y - j)
                for during in range(1, abs(j - y)+1):
                    self.table[y - sin * during][x] = player.color()

            elif y == j:
                sin = numpy.sign(x - i)
                for during in range(1, abs(i - x)+1):
                    self.table[y][x - sin * during] = player.color()

            else:
                sinx = numpy.sign(x - i)
                siny = numpy.sign(y - j)
                for during in range(1, abs(i - x)+1):
                    self.table[y - siny * during][x - sinx * during] = player.color()












