from PIL import ImageFilter
from PIL import Image
import wx
import time

class Photoshop(wx.Frame):

    imageName = ""
    saveName = ""

    def __init__(self, parent, title):
        super(Photoshop, self).__init__(parent, title = title)

        self.InitUI()
        self.Centre()
    def scale_bitmap(self, bitmap, width, height):
        image = bitmap
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result
    def getFileName(self, event):
        fileName = self.display.GetValue()
        self.imageName = fileName
        png = wx.Image(self.imageName, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        pic = wx.StaticBitmap(self, -1, png, (10, 5), (100, 100))
        pic = self.scale_bitmap(pic, 300, 200)
    def grayscale(self, pixel):
        r, g, b, a = pixel
        gray = int((r + g + b)/3)
        return(gray, gray, gray)
    def darken(self, pixel, amt):
        r, g, b, a = pixel
        return(int(r * (1- amt)), int(g * (1 - amt)), int(b * (1 - amt)))
    def brighten(self, pixel, amt):
        r, g, b, a = pixel
        nr = int(r * amt)
        if nr > 255:
            nr = 255
        ng = int(g * amt)
        if ng > 255:
            ng = 255
        nb = int(b * amt)
        if nb > 255:
            nb = 255
        return(nr, ng, nb)
    def inv(self, pixel):
        r, g, b, a = pixel
        return(255 - r, 255 - g, 255 - b)
    def no_red(self, pixel):
        r, g, b, a = pixel
        return(0, g, b)
    def no_green(self, pixel):
        r, g, b, a = pixel
        return(r, 0, b)
    def no_blue(self, pixel):
        r, g, b, a = pixel
        return(r, g, 0)
    def cool(self, pixel):
        r, g, b, a = pixel
        return(r - 10, g - 10, b + 20)
    def dramatic(self, pixel):
        r, g, b, a = pixel
        if(g > r and g > b):
            if(g < 127):
                g = g - 25
                r = r - 5
                b = b - 5
            else:
                g += 25
                r += 5
                b += 5
        if(b > r and b > g):
            if(b < 127):
                b = b - 25
                r = r - 5
                g = g - 5
            else:
                b += 25
                r += 5
                g += 5
        if(r > b and r > g):
            if(r < 127):
                r = r - 25
                b = b - 5
                g = g - 5
            else:
                r += 25
                b += 5
                g += 5
        return(r, g, b)
    def posterize(self, pixel):
        r, g, b, a = pixel
        if(0 <= r <= 63):
            r = 50
        elif(64 <= r <= 127):
            r = 100
        elif(128 <= r <= 191):
            r = 150
        else:
            r = 200
        if(0 <= g <= 63):
            g = 50
        elif(64 <= g <= 127):
            r = 100
        elif(128 <= g <= 191):
            g = 150
        else:
            g = 200
        if(0 <= b <= 63):
            bug = 50
        elif(64 <= b <= 127):
            b = 100
        elif(128 <= b <= 191):
            b = 150
        else:
            b = 200
        return(r, g, b)
    def invert(self, event):
        btn = event.GetEventObject()
        inp = self.imageName
        image = Image.open(inp)
        pixel_list = [self.inv(pixel) for pixel in list(image.getdata())]
        new = Image.new("RGB", image.size)
        new.putdata(pixel_list)
        self.saveName = "invertedImage.png"
        new.save(self.saveName)
        png = wx.Image(self.saveName, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        pic2 = wx.StaticBitmap(self, -1, png, (500, 500), (100, 100))
    def gray(self, event):
        btn = event.GetEventObject()
        inp = self.imageName
        image = Image.open(inp)
        pixel_list = [self.grayscale(pixel) for pixel in list(image.getdata())]
        new = Image.new("RGB", image.size)
        new.putdata(pixel_list)
        self.saveName = "grayscaleImage.png"
        new.save(self.saveName)
        png = wx.Image(self.saveName, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        pic2 = wx.StaticBitmap(self, -1, png, (500, 500), (240, 250))

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        open = wx.Button(self, label = 'open')

        box = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_LEFT)
        box.Add(self.display, flag = wx.EXPAND|wx.TOP|wx.BOTTOM, border = 4)
        box.Add(open, flag = wx.EXPAND)


        png = wx.Image("blacksquare.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        pic = wx.StaticBitmap(self, -1, png, (500, 500), (240, 240))

        png = wx.Image("blacksquare.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        pic2 = wx.StaticBitmap(self, -1, png, (500, 500), (240, 240))

        g = wx.GridSizer(1, 2, 5, 5)
        g.AddMany([pic, pic2])
        '''
        gs = wx.GridSizer(5, 4, 5, 5)
        #self.display.Bind(wx.EVT_TEXT_ENTER, self.getFileName)
        dark = wx.Button(self, label='darken')
        bright = wx.Button(self, label='brighten')
        gaussian = wx.Button(self, label='gaussian blur')
        grayscale = wx.Button(self, label='grayscale')
        dramatic = wx.Button(self, label='dramatic')
        cool = wx.Button(self, label='cool')
        posterize = wx.Button(self, label='posterize')
        invert = wx.Button(self, label='invert')
        nored = wx.Button(self, label='no red')
        nogreen = wx.Button(self, label='no green')
        noblue = wx.Button(self, label='no blue')
        sharpen = wx.Button(self, label='sharpen')
        contour = wx.Button(self, label='contour')
        smooth = wx.Button(self, label='smooth')
        blur = wx.Button(self, label='blur')
        detail = wx.Button(self, label='detail')
        edge = wx.Button(self, label='edge enhance')
        emboss = wx.Button(self, label='emboss')
        crop = wx.Button(self, label='crop')

        gs.AddMany( [(dark, 0, wx.EXPAND) ,(bright, 0, wx.EXPAND) , (gaussian, 0, wx.EXPAND), (grayscale, 0, wx.EXPAND), (dramatic, 0, wx.EXPAND), (cool, 0, wx.EXPAND), (posterize, 0, wx.EXPAND), (invert, 0, wx.EXPAND), (nored, 0, wx.EXPAND), (nogreen, 0, wx.EXPAND), (noblue, 0, wx.EXPAND), (sharpen, 0, wx.EXPAND), (contour, 0, wx.EXPAND), (smooth, 0, wx.EXPAND), (blur, 0, wx.EXPAND), (detail, 0, wx.EXPAND), (edge, 0, wx.EXPAND), (emboss, 0, wx.EXPAND), (crop, 0, wx.EXPAND)])
'''
        box.Add(g, proportion = 1, flag = wx.EXPAND)
        #box.Add(gs, proportion=1, flag = wx.EXPAND)
        self.SetSizer(box)
        panel = wx.Panel(self)
        choice = ["darken", "brighten", "gaussian blur", "grayscale", "dramatic", "cool", "posterize", "invert", "no red", "no green", "no blue", "sharpen", "contour", "smooth", "blur", "detail", "edge enhance", "emboss", "crop"]
        combo = wx.ComboBox(panel, choices = choice)
        box.Add(panel, wx.ALIGN_CENTRE)
        open.Bind(wx.EVT_BUTTON, self.getFileName)
        '''
        invert.Bind(wx.EVT_BUTTON, self.invert)
        grayscale.Bind(wx.EVT_BUTTON, self.gray)
        '''



def main():

    app = wx.App()
    ex = Photoshop(None, title='Photoshop')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
