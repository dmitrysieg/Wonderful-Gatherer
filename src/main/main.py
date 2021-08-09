# coding=utf-8
import wx
from controller import MSController
from view import MSView


def main():
    app = wx.App()
    view = MSView()
    controller = MSController(view)
    controller.bind_menu(view.menu)

    app.MainLoop()


if __name__ == "__main__":
    main()
