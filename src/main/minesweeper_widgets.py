import wx


class WGFieldButton(wx.Panel):
    def __init__(self, parent, pos, x_index, y_index):
        wx.Panel.__init__(self, parent=parent, pos=pos)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        # Handlers
        self.OnClick = lambda: None
        self.Bind(wx.EVT_LEFT_DOWN  , self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP    , self.OnLeftUp)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDClick)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)

        # Properties
        self.pressed = False
        self.x_index = x_index
        self.y_index = y_index

    def OnPaint(self, event):
        if not self.pressed:
            # dc = wx.BufferedPaintDC(self)
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
        else:
            dc = wx.PaintDC(self)
            dc.SetPen(wx.Pen('#C0C0C0'))
            dc.SetBrush(wx.Brush('#C0C0C0'))
            dc.DrawRectangle(0, 0, 19, 19)

    def OnLeftDown(self, event):
        self.pressed = True
        self.Refresh()

    def OnLeftUp(self, event):
        if self.pressed:
            self.pressed = False
            self.Refresh()
            self.OnClick(self)

    def OnDClick(self, event):
        self.pressed = True
        self.Refresh()

    def OnLeave(self, event):
        self.pressed = False
        self.Refresh()

    def SetOnClick(self, handler):
        self.OnClick = handler

    def OnSize(self, event):
        self.Refresh()
