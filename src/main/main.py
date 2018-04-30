# coding=utf-8
import wx
from minesweeper_widgets import WGFieldButton
from minesweeper_field import WGField
from minesweeper_field_view import WGFieldView

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

    wg_field = WGField(_h_number, _v_number).initialize()
    v_game_panel = WGFieldView(panel, _h_number, _v_number, wg_field).initialize()

    v_inner_box = wx.BoxSizer(wx.VERTICAL)
    v_inner_box.Add(v_score_panel, 2, wx.EXPAND | wx.ALL, border=4) # todo fixed size
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
