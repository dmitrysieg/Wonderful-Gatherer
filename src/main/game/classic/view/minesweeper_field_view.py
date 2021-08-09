import wx
from .minesweeper_field_button import MSFieldButton


class MSFieldView(wx.Panel):
    def __init__(self, game_model, parent, width, height):
        wx.Panel.__init__(self, parent, style=wx.SUNKEN_BORDER)
        self.game_model = game_model
        self.width = width
        self.height = height
        self.buttons = []
        self.bmap = wx.Bitmap(1, 1)
        self.bmap.LoadFile("../../img/apple.png", wx.BITMAP_TYPE_ANY)
        self.score = None
        self.initialize()

    def initialize(self):
        for j in range(0, self.height):
            self.buttons.append([])
            for i in range(0, self.width):
                button = MSFieldButton(self, (i * 20, j * 20), i, j)
                button.parent = self
                button.SetOnClick(self.ClickHandler)
                button.SetOnAfterMark(self.AfterMarkHandler)
                self.buttons[j].append(button)

    def show_amount(self, x, y, amount):
        wx.StaticText(self,
                      pos=(x * 20, y * 20),
                      size=(20, 20),
                      style=wx.ALIGN_CENTRE_HORIZONTAL,
                      label=str(amount))

    def show_mine(self, x, y):
        wx.StaticBitmap(self, pos=(x * 20, y * 20), bitmap=self.bmap)

    def after_reveal_cell(self, x, y):
        self.buttons[y][x].Destroy()

    def show_win(self):
        self.score.SetLabel("WIN!")

    def show_lose(self):
        self.score.SetLabel("LOSE!")

    def show_remaining(self, amount):
        self.score.SetLabel(str(amount))

    def disable_controls(self):
        for y in range(0, len(self.buttons)):
            for x in range(0, len(self.buttons[y])):
                if self.buttons[y][x]:
                    self.buttons[y][x].disabled = True

    def ClickHandler(self, button):
        self.game_model.on_field_open(button, self.game_model)

    def AfterMarkHandler(self, button):
        self.game_model.refresh_after_mark(button.x_index, button.y_index, button.marked)
