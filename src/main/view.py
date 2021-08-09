# coding=utf-8
import wx
from game.classic.model.minesweeper_field import MSField
from game.classic.view.minesweeper_field_view import MSFieldView
from menu import MSMenu


_version = "1.0"


class MSView:
    def __init__(self, base_width, base_height):
        self.create_base_view(base_width, base_height)

    def create_base_view(self, base_width, base_height):
        self.window = wx.Frame(None,
                               title="Wonderful Gatherer v" + str(_version),
                               size=(32 + base_width * 20, 158 + base_height * 20),
                               style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        window = self.window
        window.SetBackgroundColour(wx.LIGHT_GREY)
        self.menu = MSMenu(window)
        window.SetMenuBar(self.menu.menu_bar)
        self.bind_menu()

        outerBox = wx.GridSizer(1)
        self.panel = wx.Panel(window, style=wx.RAISED_BORDER)
        self.panel.SetBackgroundColour(wx.LIGHT_GREY)
        outerBox.Add(self.panel, 0, wx.EXPAND | wx.ALL, 4)
        self.panel.SetAutoLayout(True)

        self.innerBox = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.innerBox)
        self.panel.Layout()

        window.SetAutoLayout(True)
        window.SetSizer(outerBox)
        window.Layout()

        window.Show(True)

    def layout(self):
        self.panel.Layout()
        self.window.Layout()

    def on_exit(self, event):
        self.window.Close()

    def bind_menu(self):
        self.menu.menu_bar.Bind(wx.EVT_MENU, self.on_exit, self.menu.menu_exit)

    def start_game_classic(self, game_width, game_height):
        self.field_view = MSFieldView(self, self.panel, game_width, game_height)
        self.score_panel = wx.Panel(self.panel, style=wx.SUNKEN_BORDER)
        self.score = wx.StaticText(self.score_panel, pos=(20, 10), label="")
        self.field_view.score = self.score

        self.innerBox.Add(self.score_panel, 2, wx.EXPAND | wx.ALL, border=4) # todo fixed size
        self.innerBox.Add(self.field_view, 8, wx.EXPAND | wx.ALL, border=4)
        self.layout()
        return self.field_view
