from .minesweeper_field import MSField


class MSGameClassic:

    def __init__(self, game_view, width, height):
        self.field_model = MSField(game_view, width, height)
        self.game_view = game_view
        game_view.game_model = self

    def game_start(self):
        self.print_remaining()

    def on_field_open(self, button, game_model):
        game_view = button.parent
        if self.field_model.is_mine(button.x_index, button.y_index):
            self.lose()
        else:
            self.field_model.reveal(button.x_index, button.y_index)

    def refresh_after_mark(self, x, y, checked):
        result = self.check_mines(x, y, checked)
        if result:
            self.win()
        else:
            self.print_remaining()

    def check_mines(self, x, y, checked):
        if self.field_model.is_mine(x, y):
            if checked:
                self.field_model.mines_left -= 1
            else:
                self.field_model.mines_left += 1

        return self.field_model.mines_left == 0

    def win(self):
        self.game_view.show_win()
        self.reveal_all()

    def lose(self):
        self.game_view.show_lose()
        for mine in self.field_model.mines:
            self.reveal_one(mine[0], mine[1])
        self.game_view.disable_controls()

    def reveal_one(self, x, y):
        cell = self.field_model.field[y][x]
        if not cell.revealed:
            cell.revealed = True
            self.game_view.after_reveal_cell(x, y)
        if self.field_model.is_mine(x, y):
            self.game_view.show_mine(x, y)

    def reveal_all(self):
        for y in range(0, self.field_model.height):
            for x in range(0, self.field_model.width):
                self.reveal_one(x, y)

    def print_remaining(self):
        self.game_view.show_remaining(self.field_model.mines_left)