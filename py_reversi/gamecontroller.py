from board import Board
from gameview import GameView

class GameController:

    def __init__(self):
        self.board = Board()
        self.view = GameView()

    def start_game(self):
        put_positions = self.board.select_list(self.board.who_turn)
        while True:
            self.view.display(self.board, put_positions)
            if self.check_game_over():
                break
            key = self.view.get_key()
            if key == "q":
                break
            elif key == " ":
                put_positions.append(put_positions.pop(0))
            elif key == "\n":
                x, y = put_positions.pop(0)
                self.board.put(self.board.who_turn, x, y)
                self.board.next_turn()
                put_positions = self.board.select_list(self.board.who_turn)
                if not put_positions:
                    self.board.next_turn()
            if self.check_game_over():
                break

    def check_game_over(self):
        for yline in self.board.table:
            if  "・" in yline:
                return False
        self.view.write_message(f"{self.board.count_piece().name}")
        return True


    def will_quit(self):
        while True:
            key = self.view.get_key()
            if key == 'q':
                self.view.finish_curses()
                return True
            elif key == ' ':
                self.board = Board()
                return False
