import curses

class GameView:
    def __init__(self):
        self.init_curses()

    def init_curses(self):
        self.strscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.strscr.keypad(True)

    def finish_curses(self):
        curses.nocbreak()
        self.strscr.keypad(False)
        curses.echo()
        curses.endwin()

    def get_key(self):
        return self.strscr.getkey()

    def display(self, board, put_positions):
        scr = self.strscr
        scr.clear()
        scr.addstr(0, 0, str(board))
        for i, player in enumerate(board.players):
            teban_str = ' (teban)' if player == board.who_turn else ''
            scr.addstr(10 + i, 0, f'{player.name} {teban_str}')
        x, y = put_positions[0]
        scr.addstr(12, 0, '[Space] Next piece. [Return] Put piece. [q] Quit.')
        # scr.addstr(13, 0, str(put_positions))
        scr.move(y, x*2)
        scr.refresh()

    def write_message(self, message):
        scr = self.strscr
        scr.addstr(12, 0, "                                                    ")
        scr.addstr(12, 0, message)
        scr.addstr(13, 0, '[Space] Play again. [q] Quit.')
        scr.refresh()
