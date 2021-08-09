# coding=utf-8
import wx
from game.classic.model.minesweeper_field import MSField
from game.classic.view.minesweeper_field_view import MSFieldView
from menu import MSMenu


_version = "1.0"
_h_number = 16
_v_number = 16


class MSView:
    def __init__(self):
        self.window = wx.Frame(None,
                          title="Wonderful Gatherer v" + str(_version),
                          size=(32 + _h_number * 20, 158 + _v_number * 20),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        window = self.window
        window.SetBackgroundColour(wx.LIGHT_GREY)
        self.menu = MSMenu(window)
        window.SetMenuBar(self.menu.menu_bar)

        outerBox = wx.GridSizer(1)
        panel = wx.Panel(window, style=wx.RAISED_BORDER)
        panel.SetBackgroundColour(wx.LIGHT_GREY)
        outerBox.Add(panel, 0, wx.EXPAND | wx.ALL, 4)

        self.score_panel = wx.Panel(panel, style=wx.SUNKEN_BORDER)
        self.score = wx.StaticText(self.score_panel, pos=(20, 10), label="")

        self.field = MSField(_h_number, _v_number).initialize()
        self.field_view = MSFieldView(self, panel, _h_number, _v_number, self.field).initialize()

        innerBox = wx.BoxSizer(wx.VERTICAL)
        innerBox.Add(self.score_panel, 2, wx.EXPAND | wx.ALL, border=4) # todo fixed size
        innerBox.Add(self.field_view, 8, wx.EXPAND | wx.ALL, border=4)

        panel.SetAutoLayout(True)
        panel.SetSizer(innerBox)
        panel.Layout()

        window.SetAutoLayout(True)
        window.SetSizer(outerBox)
        window.Layout()

        window.Show(True)

    def start_game_classic(self):
        None