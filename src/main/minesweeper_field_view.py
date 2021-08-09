import wx
from minesweeper_widgets import MSFieldButton


class MSFieldView(wx.Panel):
    def __init__(self, view, parent, width, height, field):
        wx.Panel.__init__(self, parent, style=wx.SUNKEN_BORDER)
        self.view = view
        self.width = width
        self.height = height
        self.field = field
        self.buttons = []
        self.bmap = wx.Bitmap(1, 1)
        self.bmap.LoadFile("../../img/apple.png", wx.BITMAP_TYPE_ANY)

    def initialize(self):
        for j in range(0, self.height):
            self.buttons.append([])
            for i in range(0, self.width):
                button = MSFieldButton(self, (i * 20, j * 20), i, j)
                button.parent = self
                button.SetOnClick(self.ClickHandler)
                self.buttons[j].append(button)
        return self

    def show_amount(self, x, y, amount):
        wx.StaticText(self,
                      pos=(x * 20, y * 20),
                      size=(20, 20),
                      style=wx.ALIGN_CENTRE_HORIZONTAL,
                      label=str(amount))

    def show_mine(self, x, y):
        wx.StaticBitmap(self, pos=(x * 20, y * 20), bitmap=self.bmap)

    def ClickHandler(self, button):
        self.view.controller.WGClickHandler(button, self.view.controller)
