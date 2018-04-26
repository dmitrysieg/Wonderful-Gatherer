import wx


_version = "1.0"


class WGFieldButton(wx.Panel):
    def __init__(self, parent, pos):
        wx.Panel.__init__(self, parent=parent, pos=pos)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('#C0C0C0'))
        dc.SetBrush(wx.Brush('#C0C0C0'))
        dc.DrawRectangle(0, 0, 18, 18)

        dc.SetPen(wx.WHITE_PEN)
        dc.DrawLine(0, 0, 20, 0)
        dc.DrawLine(0, 0, 0, 20)
        dc.SetPen(wx.Pen('#808080'))
        dc.DrawLine(19, 0, 19, 19)
        dc.DrawLine(0, 19, 20, 19)

    def OnLeftDown(self, event):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('#C0C0C0'))
        dc.SetBrush(wx.Brush('#C0C0C0'))
        dc.DrawRectangle(0, 0, 19, 19)

    def OnSize(self, event):
        self.Refresh()


def main():
    app = wx.App()
    window = wx.Frame(None, title="Wonderful Gatherer v" + str(_version), size=(400, 300))
    window.SetBackgroundColour(wx.LIGHT_GREY)

    menu_bar = wx.MenuBar()

    menu_file = wx.Menu()
    menu_file.Append(101, "Выход")

    menu_help = wx.Menu()
    menu_help.Append(201, "О программе")

    menu_bar.Append(menu_file, "Файл")
    menu_bar.Append(menu_help, "Помощь")

    window.SetMenuBar(menu_bar)

    outer_box = wx.GridSizer(1)
    panel = wx.Panel(window, style=wx.RAISED_BORDER)
    panel.SetBackgroundColour(wx.LIGHT_GREY)
    outer_box.Add(panel, 0, wx.EXPAND | wx.ALL, 4)

    v_score_panel = wx.Panel(panel, style=wx.SUNKEN_BORDER)

    v_game_panel = wx.Panel(panel, style=wx.SUNKEN_BORDER)

    # g_main_grid = wx.GridSizer(rows=16, cols=16)
    b_one = WGFieldButton(v_game_panel, pos=(32, 32))
    b_one.SetBackgroundColour(wx.LIGHT_GREY)

    v_inner_box = wx.BoxSizer(wx.VERTICAL)
    v_inner_box.Add(v_score_panel, 2, wx.EXPAND | wx.ALL, border=4)
    v_inner_box.Add(v_game_panel, 8, wx.EXPAND | wx.ALL, border=4)

    panel.SetAutoLayout(True)
    panel.SetSizer(v_inner_box)
    panel.Layout()

    window.SetAutoLayout(True)
    window.SetSizer(outer_box)
    window.Layout()

    window.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
