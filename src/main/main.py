# coding=utf-8
import wx
from minesweeper_field import WGField
from minesweeper_field_view import WGFieldView
from menu import MSMenu
from controller import WGController

_version = "1.0"
_h_number = 16
_v_number = 16


def main():
    app = wx.App()
    window = wx.Frame(None,
                      title="Wonderful Gatherer v" + str(_version),
                      size=(32 + _h_number * 20, 158 + _v_number * 20),
                      style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
    window.SetBackgroundColour(wx.LIGHT_GREY)
    menu = MSMenu(window)
    window.SetMenuBar(menu.getMenuBar())

    outer_box = wx.GridSizer(1)
    panel = wx.Panel(window, style=wx.RAISED_BORDER)
    panel.SetBackgroundColour(wx.LIGHT_GREY)
    outer_box.Add(panel, 0, wx.EXPAND | wx.ALL, 4)

    v_score_panel = wx.Panel(panel, style=wx.SUNKEN_BORDER)
    v_score = wx.StaticText(v_score_panel, pos=(20, 10), label="")

    wg_field = WGField(_h_number, _v_number).initialize()
    v_game_panel = WGFieldView(panel, _h_number, _v_number, wg_field).initialize()

    v_inner_box = wx.BoxSizer(wx.VERTICAL)
    v_inner_box.Add(v_score_panel, 2, wx.EXPAND | wx.ALL, border=4) # todo fixed size
    v_inner_box.Add(v_game_panel, 8, wx.EXPAND | wx.ALL, border=4)

    controller = WGController(window, v_score_panel, v_game_panel, v_score)
    controller.BindMenu(menu)

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
