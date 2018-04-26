import wx


_version = "1.0"


def main():
    app = wx.App()
    window = wx.Frame(None, title="Wonderful Gatherer v" + str(_version), size=(400, 300))
    panel = wx.Panel(window)

    window.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
