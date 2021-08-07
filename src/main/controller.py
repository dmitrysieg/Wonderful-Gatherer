import wx


class WGController(object):

    def __init__(self, window, score_panel, game_panel, score):
        self.window = window
        self.score_panel = score_panel
        self.score_panel.controller = self
        self.game_panel = game_panel
        self.game_panel.controller = self
        self.score = score
        self.print_remaining()

    def onExit(self, event):
        self.window.Close()

    def BindMenu(self, menu):
        menu.getMenuBar().Bind(wx.EVT_MENU, self.onExit, menu.getMenuExit())

    def reveal(self, x, y):
        self.game_panel.buttons[y][x].Destroy()
        self.game_panel.field.field[y][x].revealed = True
        if self.game_panel.field.isMine(x, y):
            self.game_panel.show_mine(x, y)

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
        self.score.SetLabel("WIN!")
        self.disableControls()

    def lose(self):
        self.score.SetLabel("LOSE!")
        for mine in self.game_panel.field.mines:
            self.reveal(mine[0], mine[1])
        self.disableControls()

    def disableControls(self):
        for y in range(0, self.game_panel.field.height):
            for x in range(0, self.game_panel.field.width):
                if self.game_panel.buttons[y][x]:
                    self.game_panel.buttons[y][x].disabled = True
