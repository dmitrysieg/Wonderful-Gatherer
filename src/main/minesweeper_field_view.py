import wx
from minesweeper_widgets import WGFieldButton


def WGClickHandler(button):
    field_view = button.parent
    if field_view.field.isMine(button.x_index, button.y_index):
        wx.StaticBitmap(field_view, pos=(button.x_index * 20, button.y_index * 20), bitmap=field_view.bmap)
    else:
        around = field_view.field.getAround(button.x_index, button.y_index)
        if around > 0:
            wx.StaticText(field_view, pos=(button.x_index * 20, button.y_index * 20), label=str(around))
        else:
            field_view.field.RevealAround(field_view, button.x_index, button.y_index)

    field_view.field.field[button.y_index][button.x_index].revealed = True
    button.Destroy()


class WGFieldView(wx.Panel):
    def __init__(self, parent, width, height, field):
        wx.Panel.__init__(self, parent, style=wx.SUNKEN_BORDER)
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
                button = WGFieldButton(self, (i * 20, j * 20), i, j)
                button.parent = self
                button.SetOnClick(WGClickHandler)
                self.buttons[j].append(button)
        return self