class WGController(object):

    def __init__(self, score_panel, game_panel, score):
        self.score_panel = score_panel
        self.score_panel.controller = self
        self.game_panel = game_panel
        self.game_panel.controller = self
        self.score = score
        self.print_remaining()

    def check_mines(self, x, y, checked):
        if self.game_panel.field.isMine(x, y):
            if checked:
                self.game_panel.field.mines_left -= 1
            else:
                self.game_panel.field.mines_left += 1

        return self.game_panel.field.mines_left == 0

    def print_remaining(self):
        remaining = self.game_panel.field.mines_left
        self.score.SetLabel(str(remaining))

    def refresh_after_mark(self, x, y, checked):
        result = self.check_mines(x, y, checked)
        if result:
            self.win()
        else:
            self.print_remaining()

    def win(self):
        self.score.SetLabel("WIN")
