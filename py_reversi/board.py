from piece import Piece
from player import Player

class Board:
    def __init__(self):
        self.table = [["・"]*8]*8
        self.player = Player
        self.piece = Piece


    def __str__(self):
        st = []
        for i in range(8):
            st.append("".join(self.table[i]))
        return "\n".join(st)

    def canput(self, x:int, y:int):
        if self.table[y][x] == "・" and check_range(x, y):
            return True
        else:
            return False

    def put(self, player, x: int, y: int):
        if self.canput():
            self.table[y][x] = player.color
        else:
            print("error")
