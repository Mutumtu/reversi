from pyreversi.board import Board
from pyreversi.gameview import GameView

class GameController:

    def __init__(self):
        self.board = Board()
        self.view = GameView()

    def start_game(self):
        put_positions = self.board.select_list(self.board.who_turn)
        while True:
            if self.check_game_over():
                break
            self.view.display(self.board, put_positions)
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
                    put_positions = self.board.select_list(self.board.who_turn)

    def check_game_over(self):
        put_positions_S = self.board.select_list(self.board.player1)
        put_positions_G = self.board.select_list(self.board.player2)
        if put_positions_G or put_positions_S:
            return False

        self.view.strscr.addstr(0, 0, str(self.board))
        result = self.board.count_piece()
        self.view.write_message(
            f"{result[0].name} won! ({result[1]} vs {result[2]})")
        return True


    def will_quit(self):
        self.view.write_message("")
        while True:
            key = self.view.get_key()
            if key == ' ':
                self.board = Board()
                return False
            if key == 'q':
                self.view.finish_curses()
                return True
