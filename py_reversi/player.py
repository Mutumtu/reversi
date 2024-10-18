class Player:
    def __init__(self):
        self.sente = 0
        self.gote = 1
        self.color = "⚪︎" if self.is_sente() else "×"

    def is_sente(self):
        return True if

