# coding=utf-8
import wx
from game.classic.controller.controller import MSController
from view import MSView


def main():
    app = wx.App()
    view = MSView()
    controller = MSController(view)
    controller.start_game_classic()

    app.MainLoop()


if __name__ == "__main__":
    main()
