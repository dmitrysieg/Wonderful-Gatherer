import wx


class MSController(object):

    def WGClickHandler(self, button, controller):
        field_view = button.parent
        if field_view.field.is_mine(button.x_index, button.y_index):
            controller.lose()
        else:
            around = field_view.field.get_around(button.x_index, button.y_index)
            if around > 0:
                wx.StaticText(field_view, pos=(button.x_index * 20, button.y_index * 20), label=str(around))
            else:
                field_view.field.reveal_around(field_view, button.x_index, button.y_index)
            field_view.field.field[button.y_index][button.x_index].revealed = True
            button.Destroy()

    def __init__(self, view):
        self.view = view
        view.controller = self

        self.print_remaining()
        self.bind_menu(view.menu)

    def on_exit(self, event):
        self.view.window.Close()

    def bind_menu(self, menu):
        menu.menu_bar.Bind(wx.EVT_MENU, self.on_exit, menu.menu_exit)

    def reveal(self, x, y):
        cell = self.view.game_panel.field.field[y][x]
        if not cell.revealed:
            self.view.game_panel.buttons[y][x].Destroy()
            cell.revealed = True
        if self.view.game_panel.field.is_mine(x, y):
            self.view.game_panel.show_mine(x, y)

    def reveal_all(self):
        for y in range(0, self.view.game_panel.field.height):
            for x in range(0, self.view.game_panel.field.width):
                self.reveal(x, y)

    def check_mines(self, x, y, checked):
        if self.view.game_panel.field.is_mine(x, y):
            if checked:
                self.view.game_panel.field.mines_left -= 1
            else:
                self.view.game_panel.field.mines_left += 1

        return self.view.game_panel.field.mines_left == 0

    def print_remaining(self):
        remaining = self.view.game_panel.field.mines_left
        self.view.score.SetLabel(str(remaining))

    def refresh_after_mark(self, x, y, checked):
        result = self.check_mines(x, y, checked)
        if result:
            self.win()
        else:
            self.print_remaining()

    def win(self):
        self.view.score.SetLabel("WIN!")
        self.reveal_all()

    def lose(self):
        self.view.score.SetLabel("LOSE!")
        for mine in self.view.game_panel.field.mines:
            self.reveal(mine[0], mine[1])
        self.disable_controls()

    def disable_controls(self):
        for y in range(0, self.view.game_panel.field.height):
            for x in range(0, self.view.game_panel.field.width):
                if self.view.game_panel.buttons[y][x]:
                    self.view.game_panel.buttons[y][x].disabled = True
