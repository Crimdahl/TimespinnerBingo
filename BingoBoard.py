import tkinter
import os
import random

class BingoBoard(tkinter.Frame):
    iconDirectory = os.path.join(os.path.dirname(__file__), "Icons")

    def __init__(self, master, settings):
        self.master = master
        self.icons = {}
        self.buttonevents = []

        self.settings = settings

        #Iterate over dictionaries in settings, making images out of the enabled lists of items
        for k, v in self.settings.__dict__.items():
            if type(v) is dict:
                if v["settingtype"] == "item" and v["value"]:
                    for item in v["items"]:
                        image = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png"))
                        assert image.height() == image.width(), "Supplied icons should be square in shape, 16x16, 32x32, 64x64, or 128x128."
                        if image.height() == 16:
                            self.icons[item] = image.zoom(2)
                        elif image.height() == 32:
                            self.icons[item] = image
                        elif image.height() == 64:
                            self.icons[item] = image.subsample(2)
                        elif image.height() == 128:
                            self.icons[item] = image.subsample(4)

        for c in range(int(self.settings.columns["value"])):
            for r in range(int(self.settings.rows["value"])):
                frame = tkinter.Frame(
                    self.master
                )
                frame.grid(row=r, column=c, padx=2, pady=2)
                randomkey = random.choice(list(self.icons.keys()))
                if self.settings.allowDuplicates["value"]:
                    icon = self.icons.get(randomkey)
                else:
                    icon = self.icons.pop(randomkey)
                if self.settings.useCompactMode["value"]:
                    button = tkinter.Button(
                        master = frame,
                        image = icon,
                        width = icon.width(),
                        height = icon.height(),
                        compound = tkinter.BOTTOM,
                        bg = "white"
                    )
                else:
                    button = tkinter.Button(
                        master = frame,
                        text = randomkey.replace(" ", "\n", 1),
                        image = icon,
                        width = icon.width() * 2.5,
                        height = icon.height() * 2,
                        compound = tkinter.BOTTOM,
                        bg = "white"
                    )
                self.buttonevents.append(ButtonEvents(button, randomkey))
                button.image = icon
                button.pack()
    
class ButtonEvents(object):
    def __init__(self, widget, text="widget info"):
        self.waittime = 0
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.click)
        self.id = None
        self.tw = None
        self.clicked = False
        
    def click(self, event):
        self.clicked = True

    def enter(self, event=None):
        self.schedule()
        if self.widget["bg"] == "white":
            self.widget["bg"] = "green"
        elif self.widget["bg"] == "green":
            self.widget["bg"] = "white"

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        if not self.clicked:
            if self.widget["bg"] == "white":
                self.widget["bg"] = "green"
            elif self.widget["bg"] == "green":
                self.widget["bg"] = "white"
        else:
            self.clicked = False

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx()
        y += self.widget.winfo_rooty() - (self.widget.winfo_height() / 2)
        # creates a toplevel window
        self.tw = tkinter.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(self.tw, text=self.text, justify='left',
                        background="#ffffff", relief='solid', borderwidth=1,
                        wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
    



