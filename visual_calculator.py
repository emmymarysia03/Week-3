import wx
import time

class Example(wx.Frame):
    num1 = ""
    num2 = ""
    op = ""

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
    def bintooct(self, bin):
        l = len(bin)
        convert = ""
        result = ""
        if "." not in bin:
            if l % 3 == 2:
                convert = "0" + bin
            elif l % 3 == 1:
                convert = "00" + bin
            else:
                convert = bin
            x = 0
            while(x < l):
                c = convert[x:x+3]
                add = self.bintodec(c)
                result += add
                x += 3
        else:
            first = bin[0:bin.index(".")]
            last = bin[bin.index(".") + 1:l]
            fconv = ""
            lconv = ""
            a = len(first)
            b = len(last)
            if a % 3 == 2:
                fconv = "0" + first
            elif a % 3 == 1:
                fconv = "00" + first
            else:
                fconv = first
            count = 0
            while(count < a):
                f = fconv[count:count+3]
                add = self.bintodec(f)
                result += add
                count += 3
            result += "."
            o = 0
            if b % 3 == 2:
                lconv = last + "0"
            elif b % 3 == 1:
                lconv = last + "00"
            else:
                lconv = last
            while(o < b):
                h = lconv[o:o+3]
                add = self.bintodec(h)
                result += add
                o += 3

        self.display.SetValue(result)

    def bintohex(self, bin):
        l = len(bin)
        convert = ""
        result = ""
        if "." not in bin:
            if l % 4 == 3:
                convert = "0" + bin
            elif l % 4 == 2:
                convert = "00" + bin
            elif l % 4 == 1:
                convert = "000" + bin
            else:
                convert = bin
            x = 0
            while(x < l):
                c = convert[x:x+4]
                add = self.bintodec(c)
                if(add != "10" and add != "11" and add != "12" and add != "13" and add != "14" and add != "15"):
                    result += add
                else:
                    if add == "10":
                        result += "A"
                    elif add == "11":
                        result += "B"
                    elif add == "12":
                        result += "C"
                    elif add == "13":
                        result += "D"
                    elif add == "14":
                        result += "E"
                    elif add == "15":
                        result += "F"
                x += 4
        else:
            first = bin[0:bin.index(".")]
            last = bin[bin.index(".") + 1:l]
            fconv = ""
            lconv = ""
            a = len(first)
            b = len(last)
            if a % 4 == 3:
                fconv = "0" + first
            elif a % 4 == 2:
                fconv = "00" + first
            elif a % 4 == 1:
                fconv = "000" + first
            else:
                fconv = first
            x = 0
            while(x < a):
                c = fconv[x:x+4]
                add = self.bintodec(c)
                if(add != "10" and add != "11" and add != "12" and add != "13" and add != "14" and add != "15"):
                    result += add
                else:
                    if add == "10":
                        result += "A"
                    elif add == "11":
                        result += "B"
                    elif add == "12":
                        result += "C"
                    elif add == "13":
                        result += "D"
                    elif add == "14":
                        result += "E"
                    elif add == "15":
                        result += "F"
                x += 4
            result += "."
            o = 0
            if b % 4 == 3:
                lconv = last + "0"
            elif b % 3 == 2:
                lconv = last + "00"
            elif b % 3 == 1:
                lconv = last + "000"
            else:
                lconv = last
            while(o < b):
                h = lconv[o:o+4]
                add = self.bintodec(h)
                if(add != "10" and add != "11" and add != "12" and add != "13" and add != "14" and add != "15"):
                    result += add
                else:
                    if add == "10":
                        result += "A"
                    elif add == "11":
                        result += "B"
                    elif add == "12":
                        result += "C"
                    elif add == "13":
                        result += "D"
                    elif add == "14":
                        result += "E"
                    elif add == "15":
                        result += "F"
                o += 4
        self.display.SetValue(result)

    def bintodec(self, bin):
        l = len(bin)
        dec = 0
        if "." not in bin:
            for x in range(l):
                n = bin[x]
                num = int(n)
                num *= 2** (l - 1 - x)
                dec += num
        else:
            first = bin[0:bin.index(".")]
            last = bin[bin.index(".") - 1:l-1]
            a = len(first)
            b = len(last)
            for x in range(a):
                n = first[x]
                num = float(n)
                num *= 2** (a - 1 - x)
                dec += num
            for x in range(b):
                n = last[x]
                if(n == "."):
                    continue
                num = float(n)
                num *= 2 ** (0 - (x + 1))
                dec += num
        self.display.SetValue(str(dec))
        return(str(dec))
    def mod(self, a, b):
        orig = a
        while a > 0:
            a = a - b
        if(a < 0):
            a += b
        self.display.SetValue(str(a))
        return (a)
    def add(self, a, b):
        result = a + b
        self.display.SetValue(str(a) + " + " + str(b) + " = " + str(result))
    def sub(self, a, b):
        result = a - b
        self.display.SetValue(str(a) + " - " + str(b) + " = " + str(result))
    def mult(self, a, b):
        result = 0
        for x in range(b):
            result += a
        self.display.SetValue(str(a) + " * " + str(b) + " = " + str(result))
    def pow(self, a, b):
        result = a
        for x in range(b - 1):
            result *= a
        self.display.SetValue(str(a) + "^" + str(b) + " = " + str(result))
    def div(self, a, b):
        rem = self.mod(a, b)
        result = 0
        oa = a #stores the original value of a, since a is modified when dividing
        if(rem == 0):
            while a > 0:
                a = a - b
                result += 1
        if(rem > 0):
            a = a - rem
            while a > 0:
                a = a - b
                result += 1
        rem = float(rem)
        result = result + rem/2
        self.display.SetValue(str(oa) + " / " + str(b) + " = " + str(result))

    def click(self, event):
        btn = event.GetEventObject()
        l = btn.GetLabelText()
        if(l == "+" or l == "-" or l == "*" or l == "/" or l == "%" or l == "^"):
            self.display.write(btn.GetLabelText())
            self.op = l
        elif(l == "="):
            self.display.write(btn.GetLabelText())
            if(self.op == "+"):
                self.add(float(self.num1), float(self.num2))
            elif(self.op == "-"):
                self.sub(float(self.num1), float(self.num2))
            elif(self.op == "*"):
                self.mult(int(self.num1), int(self.num2))
            elif(self.op == "/"):
                self.div(int(self.num1), int(self.num2))
            elif(self.op == "%"):
                self.mod(float(self.num1), float(self.num2))
            elif(self.op == "^"):
                self.pow(int(self.num1), int(self.num2))
        elif(l == "Bin to Oct"):
            self.bintooct(self.num1)
        elif(l == "Bin to Hex"):
            self.bintohex(self.num1)
        elif(l == "Bin to Dec"):
            self.bintodec(self.num1)
        else:
            self.display.write(btn.GetLabelText())
            if(self.op != ""):
                self.num2 += l
            else:
                self.num1 += l


    def clear1(self):
        self.num1 = ""
        self.num2 = ""
        self.op = ""
        self.display.SetValue("")

    def clear(self, event):
        btn = event.GetEventObject()
        self.num1 = ""
        self.num2 = ""
        self.op = ""
        self.display.SetValue("")
    def back(self, event):
        btn = event.GetEventObject()
        str = self.display.GetValue()
        s = str[0:len(str) - 1]
        self.display.SetValue(s)



    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag = wx.EXPAND|wx.TOP|wx.BOTTOM, border = 4)
        gs = wx.GridSizer(7, 4, 5, 5)
        clsa = wx.Button(self, id=wx.ID_ANY, label="Cls") #, 0, wx.EXPAND
        #clsa = wx.Button(self, label='Cls'), 0, wx.EXPAND
        seven = wx.Button(self, label='7') #, 0, wx.EXPAND
        eight = wx.Button(self, label='8') #, 0, wx.EXPAND
        nine = wx.Button(self, label='9') #, 0, wx.EXPAND
        div = wx.Button(self, label='/') #, 0, wx.EXPAND
        four = wx.Button(self, label='4') #, 0, wx.EXPAND
        five = wx.Button(self, label='5') #, 0, wx.EXPAND
        six = wx.Button(self, label='6') #, 0, wx.EXPAND
        mult = wx.Button(self, label='*') #, 0, wx.EXPAND
        one = wx.Button(self, label='1') #, 0, wx.EXPAND
        two = wx.Button(self, label='2') #, 0, wx.EXPAND
        three = wx.Button(self, label='3') #, 0, wx.EXPAND
        minus = wx.Button(self, label='-') #, 0, wx.EXPAND
        zero = wx.Button(self, label='0') #, 0, wx.EXPAND
        dot = wx.Button(self, label='.') #, 0, wx.EXPAND
        eq = wx.Button(self, label='=') #, 0, wx.EXPAND
        plus = wx.Button(self, label='+') #, 0, wx.EXPAND
        btd = wx.Button(self, label='Bin to Dec') #, 0, wx.EXPAND
        bth = wx.Button(self, label='Bin to Hex') #, 0, wx.EXPAND
        bto = wx.Button(self, label='Bin to Oct') #, 0, wx.EXPAND
        exp = wx.Button(self, label='^') #, 0, wx.EXPAND
        mod = wx.Button(self, label = '%') #, 0, wx.EXPAND

        gs.AddMany( [(clsa), (wx.StaticText(self), wx.EXPAND),(wx.StaticText(self), wx.EXPAND),(wx.StaticText(self), wx.EXPAND),(seven),(eight),(nine),(div),(four),(five),(six),(mult),(one),(two),(three),(minus),(zero),(dot),(eq),(plus),(btd),(bth),(bto),(exp),(mod),(wx.StaticText(self), wx.EXPAND),(wx.StaticText(self), wx.EXPAND),(wx.StaticText(self), wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag = wx.EXPAND)
        self.SetSizer(vbox)

        clsa.Bind(wx.EVT_BUTTON, self.clear)
        seven.Bind(wx.EVT_BUTTON, self.click)
        eight.Bind(wx.EVT_BUTTON, self.click)
        nine.Bind(wx.EVT_BUTTON, self.click)
        div.Bind(wx.EVT_BUTTON, self.click)
        four.Bind(wx.EVT_BUTTON, self.click)
        five.Bind(wx.EVT_BUTTON, self.click)
        six.Bind(wx.EVT_BUTTON, self.click)
        mult.Bind(wx.EVT_BUTTON, self.click)
        one.Bind(wx.EVT_BUTTON, self.click)
        two.Bind(wx.EVT_BUTTON, self.click)
        three.Bind(wx.EVT_BUTTON, self.click)
        minus.Bind(wx.EVT_BUTTON, self.click)
        zero.Bind(wx.EVT_BUTTON, self.click)
        dot.Bind(wx.EVT_BUTTON, self.click)
        eq.Bind(wx.EVT_BUTTON, self.click)
        plus.Bind(wx.EVT_BUTTON, self.click)
        btd.Bind(wx.EVT_BUTTON, self.click)
        bth.Bind(wx.EVT_BUTTON, self.click)
        bto.Bind(wx.EVT_BUTTON, self.click)
        exp.Bind(wx.EVT_BUTTON, self.click)
        mod.Bind(wx.EVT_BUTTON, self.click)


def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
