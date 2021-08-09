# coding=utf-8
import wx


class MSMenu:
    def __init__(self, window):
        self.window = window
        self.menu_bar = wx.MenuBar()

        self.menu_file = wx.Menu()
        self.menu_exit = self.menu_file.Append(wx.ID_EXIT, "Выход")

        self.menu_help = wx.Menu()
        self.menu_help.Append(201, "О программе")

        self.menu_bar.Append(self.menu_file, "Файл")
        self.menu_bar.Append(self.menu_help, "Помощь")