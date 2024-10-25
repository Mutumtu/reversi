class Player:

    SENTE = 0
    GOTE = 1

    def __init__(self, name, direction):
        self.name = name
        self.direction = direction

    def is_sente(self):
        return True if self.direction == 0 else False

    def color(self):
        return "ｏ" if self.is_sente() else "＊"


