import os
import wx
from PIL import ImageFilter
from PIL import Image

class PhotoCtrl(wx.App):
    filepath = ""
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Photoshop')

        self.panel = wx.Panel(self.frame)

        self.choice = ["grayscale", "dramatic", "cool", "posterize", "invert", "no red", "no green", "no blue", "sharpen", "contour", "smooth", "blur", "detail", "edge enhance", "emboss"]
        self.combo = wx.ComboBox(self.panel, choices = self.choice)

        #self.save = wx.Button(self.panel, label='Save')


        self.PhotoMaxSize = 240

        self.createWidgets()
        self.frame.Show()

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
    def invert(self, pixel):
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
    def same(self, pixel):
        r, g, b = pixel
        return(r, g, b)
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

    def createWidgets(self):
        img = wx.Image(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                         wx.Bitmap(img))

        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))
        browseBtn = wx.Button(self.panel, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(browseBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)
        '''
        choice = ["darken", "brighten", "gaussian blur", "grayscale", "dramatic", "cool", "posterize", "invert", "no red", "no green", "no blue", "sharpen", "contour", "smooth", "blur", "detail", "edge enhance", "emboss", "crop"]
        combo = wx.ComboBox(self.panel, choices = choice)
        '''
        self.sizer.Add(self.combo)
        #self.sizer.Add(self.save)


        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)
        self.panel.Layout()

        self.combo.Bind(wx.EVT_COMBOBOX, self.onCombo)
        #self.save.Bind(wx.EVT_BUTTON, self.onSave)

    def onCombo(self, event):
        label =  self.combo.GetValue()
        if(label == "grayscale"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.grayscale(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "dramatic"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.dramatic(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "cool"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.cool(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "posterize"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.posterize(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "invert"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.invert(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "no red"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.no_red(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "no green"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.no_green(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "no blue"):
            image = Image.open(self.photoTxt.GetValue())
            pixel_list = [self.no_blue(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("temp.png")
            self.onView2("temp.png")
        if(label == "sharpen"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.SHARPEN)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "contour"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.CONTOUR)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "smooth"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.CONTOUR)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "smooth"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.SMOOTH)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "blur"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.BLUR)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "detail"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.DETAIL)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "edge enhance"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.EDGE_ENHANCE)
            im1.save("temp.png")
            self.onView2("temp.png")
        if(label == "emboss"):
            im = Image.open(self.photoTxt.GetValue())
            im1 = im.filter(ImageFilter.EMBOSS)
            im1.save("temp.png")
            self.onView2("temp.png")

    '''

    def onSave(self, event):
        label =  self.combo.GetValue()
        image = Image.open("temp.png")
        if(label == "grayscale"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("grayscaleImage.png")
            os.remove("temp.png")
        if(label == "dramatic"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("dramaticImage.png")
            os.remove("temp.png")
        if(label == "cool"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("coolImage.png")
            os.remove("temp.png")
        if(label == "posterize"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("posterizedImage.png")
            os.remove("temp.png")
        if(label == "invert"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("invertedImage.png")
            os.remove("temp.png")
        if(label == "no red"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("no_redImage.png")
            os.remove("temp.png")
        if(label == "no green"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("no_greenImage.png")
            os.remove("temp.png")
        if(label == "no blue"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("no_blueImage.png")
            os.remove("temp.png")
        if(label == "sharpen"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("sharpenedImage.png")
            os.remove("temp.png")
        if(label == "contour"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("contouredImage.png")
            os.remove("temp.png")
        if(label == "smooth"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("smoothImage.png")
            os.remove("temp.png")
        if(label == "blur"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("blurredImage.png")
            os.remove("temp.png")
        if(label == "detail"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("detailImage.png")
            os.remove("temp.png")
        if(label == "edge enhance"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("edge_enhancedImage.png")
            os.remove("temp.png")
        if(label == "emboss"):
            pixel_list = [self.same(pixel) for pixel in list(image.getdata())]
            new = Image.new("RGB", image.size)
            new.putdata(pixel_list)
            new.save("embossedImage.png")
            os.remove("temp.png")
    '''
    def onBrowse(self, event):
        """
        Browse for file
        """
        wildcard = "PNG files (*.png)|*.png"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

    def onView2(self, filepath):
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.filepath = filepath
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    def onView(self):
        filepath = self.photoTxt.GetValue()
        self.filepath = filepath
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

if __name__ == '__main__':
    app = PhotoCtrl()
    app.MainLoop()
