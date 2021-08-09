# coding=utf-8
import wx
from model import GameManager
from view import MSView


def main():
    app = wx.App()
    base_view = MSView(GameManager.GAME_WIDTH, GameManager.GAME_HEIGHT)
    base_model = GameManager(base_view)
    base_model.start_game_classic()

    app.MainLoop()


if __name__ == "__main__":
    main()
