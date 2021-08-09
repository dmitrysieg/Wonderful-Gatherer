import wx


class WGFieldButton(wx.Panel):

    def __init__(self, parent, pos, x_index, y_index):
        wx.Panel.__init__(self, parent=parent, pos=pos)

        self.mark_bmap = wx.Bitmap(1, 1)
        self.mark_bmap.LoadFile("../../img/warning_a.gif", wx.BITMAP_TYPE_ANY)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        # Handlers
        self.OnClick = lambda: None
        self.Bind(wx.EVT_LEFT_DOWN   , self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP     , self.OnLeftUp)
        self.Bind(wx.EVT_RIGHT_DOWN  , self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP    , self.OnRightUp)
        self.Bind(wx.EVT_LEFT_DCLICK , self.OnDClick)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)

        # Properties
        self.disabled = False
        self.pressed = False
        self.marked = False
        self.mark_in_progress = False
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
            if self.marked:
                dc.DrawBitmap(self.mark_bmap, 2, 2, True)
        else:
            dc = wx.PaintDC(self)
            dc.SetPen(wx.Pen('#C0C0C0'))
            dc.SetBrush(wx.Brush('#C0C0C0'))
            dc.DrawRectangle(0, 0, 19, 19)

    def OnLeftDown(self, event):
        if not self.disabled:
            self.pressed = True
            self.Refresh()

    def OnLeftUp(self, event):
        if self.pressed:
            self.pressed = False
            self.Refresh()
            self.OnClick(self)

    def OnDClick(self, event):
        if not self.disabled:
            self.pressed = True
            self.Refresh()

    def OnRightDown(self, event):
        if not self.disabled:
            self.mark_in_progress = True

    def OnRightUp(self, event):
        if self.mark_in_progress:
            self.marked = not self.marked
            self.Refresh()
            self.GetParent().view.controller.refresh_after_mark(self.x_index, self.y_index, self.marked)

    def OnLeave(self, event):
        self.pressed = False
        self.mark_in_progress = False
        self.Refresh()

    def SetOnClick(self, handler):
        self.OnClick = handler

    def OnSize(self, event):
        self.Refresh()
