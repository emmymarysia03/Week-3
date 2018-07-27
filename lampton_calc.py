import wx


class Example(wx.Frame):
    num1 = ""
    num2 = ""
    op = ""
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
    def Addition(self, a, b):
        result = a + b
        self.display.write(str(result))
    def Subtraction(self, a, b):
        result = a - b
        self.display.write(str(result))


    def Multiplication(self, a, b):
        result = 0
        for x in range (b):
            result= result + a
        self.display.write(str(result))



    def Division(self, a, b):
        remainder = 0
        result = 0
        remainder = float(remainder)
        while (a >= b and a - b >= 0):
            a -= b
            result = result + 1
        if not (a == 0):
            remainder = a
        self.display.write(str(result))
        print (remainder)

    def BinaryToOctal(self, number):
        unit = input("does you number have a decimal? ")
        if unit == "yes":
            [num_bef_dec, num_aft_dec] = number.split(".")
        if unit == "no":
            num_bef_dec = number
            num_aft_dec = ""
        output = ""

        if len(num_bef_dec) % 3 == 1:
            num_bef_dec = "00" + num_bef_dec
        if len(num_bef_dec) % 3 == 2:
            num_bef_dec = "0" + num_bef_dec

        for index in range(0, len(num_bef_dec), 3):
            cur_group = num_bef_dec[index: index+3]

            if cur_group == "000":
                output = output + "0"
            elif cur_group == "001":
                output = output + "1"
            elif cur_group == "010":
                output = output + "2"
            elif cur_group == "011":
                output = output + "3"
            elif cur_group == "100":
                output = output + "4"
            elif cur_group == "101":
                output = output + "5"
            elif cur_group == "110":
                output = output + "6"
            elif cur_group == "111":
                output = output + "7"

        if len(num_aft_dec) % 3 == 1:
            num_aft_dec = "00" + num_aft_dec
        if len(num_aft_dec) % 3 == 2:
            num_aft_dec = "0" + num_aft_dec
        output+= "."
        for index in range(0, len(num_aft_dec), 3):
            cur_group = num_aft_dec[index: index+3]

            if cur_group == "000":
                output = output + "0"
            elif cur_group == "001":
                output = output + "1"
            elif cur_group == "010":
                output = output + "2"
            elif cur_group == "011":
                output = output + "3"
            elif cur_group == "100":
                output = output + "4"
            elif cur_group == "101":
                output = output + "5"
            elif cur_group == "110":
                output = output + "6"
            elif cur_group == "111":
                output = output + "7"
        self.display.SetValue(output)

    def Backfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        print (l)
    def Clearfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.num1 = ""
        self.num2 = ""
        self.op = ""
        self.display.SetValue("")
    def Closefunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()

    def Sevenfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Eightfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Ninefunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Dividebuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        self.op = l
    def Fourfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Fivefunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Sixfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Multiplybuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        self.op = l
    def Onefunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Twofunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Threefunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Minusbuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        self.op = l
    def Zerofunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Decimalbuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == ""):
            self.num1 += l
        else:
            self.num2 += l
    def Equalbuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        if (self.op == "+"):
            self.Addition(float(self.num1),float(self.num2))
        elif(self.op == "-"):
            self.Subtraction(float(self.num1),float(self.num2))
        elif(self.op == "*"):
            self.Multiplication(int(self.num1),int(self.num2))
        elif(self.op == "/"):
            self.Division(float(self.num1),float(self.num2))

    def Addbuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.display.write(l)
        self.op = l
    def Binarytooctalbuttonfunction(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        self.BinaryToOctal(self.num1)




    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(6, 4, 6, 6)

        clear = wx.Button(self, label='Clear')
        back = wx.Button(self, label='Bck')
        wx.StaticText(self)
        close = wx.Button(self, label='Close')
        seven = wx.Button(self, label='7')
        eight = wx.Button(self, label='8')
        nine = wx.Button(self, label='9')
        dividebutton = wx.Button(self, label='/')
        four = wx.Button(self, label='4')
        five = wx.Button(self, label='5')
        six = wx.Button(self, label='6')
        multiplybutton = wx.Button(self, label='*')
        one = wx.Button(self, label='1')
        two = wx.Button(self, label='2')
        three = wx.Button(self, label='3')
        minusbutton = wx.Button(self, label='-')
        zero = wx.Button(self, label='0')
        decimalbutton = wx.Button(self, label='.')
        equalbutton = wx.Button(self, label='=')
        addbutton = wx.Button(self, label='+')
        binarytooctalbutton = wx.Button(self, label='Bi to Octal')
        gs.AddMany([(clear, 0, wx.EXPAND),
        (back, 0, wx.EXPAND),
        wx.StaticText(self),
        (close, 0, wx.EXPAND),
        (seven, 0, wx.EXPAND),
        (eight, 0, wx.EXPAND),
        (nine, 0, wx.EXPAND),
        (dividebutton, 0, wx.EXPAND),
        (four, 0, wx.EXPAND),
        (five, 0, wx.EXPAND),
        (six, 0, wx.EXPAND),
        (multiplybutton, 0, wx.EXPAND),
        (one, 0, wx.EXPAND),
        (two, 0, wx.EXPAND),
        (three, 0, wx.EXPAND),
        (minusbutton, 0, wx.EXPAND),
        (zero, 0, wx.EXPAND),
        (decimalbutton, 0, wx.EXPAND),
        (equalbutton, 0, wx.EXPAND),
        (addbutton, 0, wx.EXPAND),
        (binarytooctalbutton, 0, wx.EXPAND)])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.Backfunction, back)
        self.Bind(wx.EVT_BUTTON, self.Clearfunction, clear)
        self.Bind(wx.EVT_BUTTON, self.Closefunction, close)
        self.Bind(wx.EVT_BUTTON, self.Sevenfunction, seven)
        self.Bind(wx.EVT_BUTTON, self.Eightfunction, eight)
        self.Bind(wx.EVT_BUTTON, self.Ninefunction, nine)
        self.Bind(wx.EVT_BUTTON, self.Dividebuttonfunction, dividebutton)
        self.Bind(wx.EVT_BUTTON, self.Fourfunction, four)
        self.Bind(wx.EVT_BUTTON, self.Fivefunction, five)
        self.Bind(wx.EVT_BUTTON, self.Sixfunction, six)
        self.Bind(wx.EVT_BUTTON, self.Multiplybuttonfunction, multiplybutton)
        self.Bind(wx.EVT_BUTTON, self.Onefunction, one)
        self.Bind(wx.EVT_BUTTON, self.Twofunction, two)
        self.Bind(wx.EVT_BUTTON, self.Threefunction, three)
        self.Bind(wx.EVT_BUTTON, self.Minusbuttonfunction, minusbutton)
        self.Bind(wx.EVT_BUTTON, self.Zerofunction, zero)
        self.Bind(wx.EVT_BUTTON, self.Decimalbuttonfunction, decimalbutton)
        self.Bind(wx.EVT_BUTTON, self.Equalbuttonfunction, equalbutton)
        self.Bind(wx.EVT_BUTTON, self.Addbuttonfunction, addbutton)
        self.Bind(wx.EVT_BUTTON, self.Binarytooctalbuttonfunction, binarytooctalbutton)


def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
