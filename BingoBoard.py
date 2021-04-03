import tkinter
import os
import random
import re
from collections import defaultdict

hexGreen = "#008000"
hexWhite = "#FFFFFF"
hexBlack = "#000000"
hexGold = "#daa520"
hexAltGreen = "#008100"

class BingoBoard(tkinter.Frame):
    iconDirectory = os.path.join(os.path.dirname(__file__), "Icons")

    def __init__(self, master, settings):
        self.master = master
        self.icons = {}
        self.buttons = defaultdict(list)
        self.buttonevents = []
        self.btnToggle = None
        self.settings = settings

        #Iterate over dictionaries in settings, making images out of the enabled lists of items
        for k, v in self.settings.__dict__.items():
            if type(v) is dict:
                if v["settingtype"] == "item" and v["value"]:
                    for item in v["items"]:
                        if settings.excludeMeyef["value"] and item == "Meyef": continue
                        if settings.excludeJewelryBox["value"] and item == "Jewelry Box": continue
                        if settings.excludeTalariaAttachment["value"] and item == "Talaria Attachment": continue
                        if settings.excludeKickstarterItems["value"] and (item == "Wyrm Brooch" or item == "Greed Brooch" or item == "Umbra Orb"): continue
                        if settings.excludeRareItems["value"] and (item == "Elemental Beads"): continue
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

        if self.settings.columns["value"] > 3:
            widget = tkinter.Label(
                master = self.master,
                text = "Search"
                )
            if self.settings.useCompactMode["value"]:
                widget.grid(row=0, column=0, columnspan=2, padx=(2,2), sticky="w")
            else:
                widget.grid(row=0, column=0, padx=(2,2), sticky="e")

            widget = CustomText(
                master = self.master,
                height = 1,
                width = 0
                )
            widget.bind("<<TextModified>>", self.searchBoxModified)
            widget.grid(row=0, column=1, columnspan=self.settings.columns["value"] - 2, sticky="ew")

            widget = tkinter.Button(
                            master = self.master,
                            compound = tkinter.BOTTOM,
                            text="Mark",
                            command=self.toggleButtons
                        )
            widget.grid(row=0, column=self.settings.columns["value"] - 1, columnspan=2, padx=(2, 2), sticky="ew")

        for c in range(int(self.settings.columns["value"])):
            for r in range(1, int(self.settings.rows["value"]) + 1):
                frame = tkinter.Frame(
                    master = self.master
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
                        bg = hexWhite
                    )
                else:
                    button = tkinter.Button(
                        master = frame,
                        text = randomkey.replace(" ", "\n", 1),
                        image = icon,
                        width = icon.width() * 2.5,
                        height = icon.height() * 2,
                        compound = tkinter.BOTTOM,
                        bg = hexWhite
                    )
                self.buttons[randomkey].append(button)
                self.buttonevents.append(ButtonEvents(button, randomkey))
                button.image = icon
                button.pack()

    def searchBoxModified(self, event = None):
        search_value = event.widget.get(1.0, "end-1c")
        if search_value != "":
            for k, v in self.buttons.items():
                for button in v:
                    if button["bg"] == hexGreen:
                        button["bg"] = hexAltGreen
                    if button["bg"] != hexGreen and button["bg"] != hexAltGreen:
                        if button["bg"] != hexGreen and re.search(search_value.lower(), k.lower()):
                            button["bg"] = hexGold
                        elif button["bg"] != hexGreen: 
                            button["bg"] = hexWhite
        else:
            for k, v in self.buttons.items():
                for button in v:
                    if button["bg"] == hexGold:
                        button["bg"] = hexWhite
                    elif button["bg"] == hexAltGreen:
                        button["bg"] = hexGreen
        
    def toggleButtons(self):
        for k, v in self.buttons.items():
            for button in v:
                if button["bg"] == hexGold:
                    button["bg"] = hexAltGreen

class CustomText(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")

        return result

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
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True

    def enter(self, event=None):
        self.schedule()
        if self.widget["bg"] == hexWhite:
            self.widget["bg"] = hexGreen
        elif self.widget["bg"] == hexGreen:
            self.widget["bg"] = hexWhite
        elif self.widget["bg"] == hexGold:
            self.widget["bg"] = hexAltGreen
        elif self.widget["bg"] == hexAltGreen:
            self.widget["bg"] = hexGold

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        if not self.clicked:
            if self.widget["bg"] == hexWhite:
                self.widget["bg"] = hexGreen
            elif self.widget["bg"] == hexGreen:
                self.widget["bg"] = hexWhite
            elif self.widget["bg"] == hexGold:
                self.widget["bg"] = hexAltGreen
            elif self.widget["bg"] == hexAltGreen:
                self.widget["bg"] = hexGold
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
        if self.widget["text"] == "":
            y += self.widget.winfo_rooty() - (self.widget.winfo_height() / 2)
        else:
            y += self.widget.winfo_rooty() - (self.widget.winfo_height() / 4)
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
    



