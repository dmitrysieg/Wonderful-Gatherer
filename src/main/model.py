from game.classic.model.minesweeper_game_classic import MSGameClassic


class GameManager:

    GAME_WIDTH = 16
    GAME_HEIGHT = 16

    def __init__(self, base_view):
        self.base_view = base_view

    def start_game_classic(self):
        game_view = self.base_view.start_game_classic(self.GAME_WIDTH, self.GAME_HEIGHT)
        self.game = MSGameClassic(game_view, self.GAME_WIDTH, self.GAME_HEIGHT)