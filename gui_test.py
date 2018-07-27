import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')

def main():
    app = wx.App()
    ex = Example(None, title = 'Sizing')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()

'''
frame = wx.Frame(None, style = wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX)
frame.Show(True)

app.MainLoop()
'''
