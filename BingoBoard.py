import tkinter
import os
import random

class BingoBoard(tkinter.Frame):
    iconDirectory = os.path.join(os.path.dirname(__file__), "Icons")

    def __init__(self, master, settings):
        self.master = master
        self.icons = {}
        self.tooltips = []

        self.settings = settings
        index = 1
        if self.settings.consumables["value"]:
            for item in self.settings.consumables["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.questItems["value"]:
            for item in self.settings.questItems["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1
                   
        if self.settings.relics["value"]:
            for item in self.settings.relics["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.orbs["value"]:
            for item in self.settings.orbs["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.passives["value"]:
            for item in self.settings.passives["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1
                   
        if self.settings.spells["value"]:
            for item in self.settings.spells["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.armor["value"]:
            for item in self.settings.armor["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.headgear["value"]:
            for item in self.settings.headgear["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1
                   
        if self.settings.trinkets["value"]:
            for item in self.settings.trinkets["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.keycards["value"]:
            for item in self.settings.keycards["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.familiars["value"]:
            for item in self.settings.familiars["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1

        if self.settings.miscellaneous["value"]:
            for item in self.settings.miscellaneous["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                    index += 1
        
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
                button.config(command = lambda arg=button:buttonClick(arg))
                self.tooltips.append(ToolTip(button, randomkey))
                button.image = icon
                button.pack()

        #Button click event handler
        def buttonClick(arg):
            if arg["bg"] == "white":
                arg["bg"] = "green"
            elif arg["bg"] == "green":
                arg["bg"] = "white"
    
class ToolTip(object):
    def __init__(self, widget, text="widget info"):
        self.waittime = 0
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

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
    



