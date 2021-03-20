import tkinter
import os
import random

class BingoBoard(tkinter.Frame):
    iconDirectory = os.path.join(os.path.dirname(__file__), "Icons")
    consumables = ["Antidote", "Berry Pick-Mi-Up", "Berry Pick-Mi-Up Plus", "Biscuit", "Chaos Rose", "Cheveur Breast", "Cheveur Drumstick",
                        "Dream Wisp", "Eel Meat", "Empress Cake", "Ether", "Filigree Tea", "Hi-Ether", "Hi-Potion", "Jerky", "Mind Refresh Ultra",
                        "Mind Refresh", "Mushroom", "Orange Juice", "Plump Maggot", "Potion", "Rotten Tail", "Sand Bottle", "Sand Vial",
                        "Spaghetti", "Warp Shard", "Wyvern Tail"]
    quest_items = ["Alchemy Backpack", "Cheveur Breast", "Cheveur Drumstick", "Cheveur Feather", "Eel Meat", "Food Synthesizer", "Galaxy Stone", 
                        "Herb", "Mushroom", "Plasma Core", "Plasma Crystal", "Plasma IV Bag", "Silver Ore", "Siren Ink", "Wyvern Tail" ]
    relics = ["Celestial Sash", "Eternal Brooch", "Gas Mask", "Goddess Brooch", "Greed Brooch", "Jewelry Box", "Soul Scanner", "Succubus Hairpin",
                   "Tablet", "Talaria Attachment", "Timespinner Gear 1", "Timespinner Gear 2", "Timespinner Gear 3", "Timespinner Spindle",
                   "Timespinner Wheel", "Twin Pyramids", "Water Mask", "Wyrm Brooch"]
    orbs = ["Blade Orb", "Blood Orb", "Blue Orb", "Empire Orb", "Eye Orb", "Fire Orb", "Forbidden Tome", "Gun Orb", "Ice Orb", "Iron Orb",
                 "Nether Orb", "Plasma Orb", "Radiant Orb", "Shattered Orb", "Umbra Orb", "Wind Orb"]
    passives = ["Bleak Ring", "Dusk Ring", "Economizer", "Hope Ring", "Icicle Ring", "Oculus Ring", "Pyro Ring", "Royal Ring", "Sanguine Ring",
                     "Scythe Ring", "Shadow Seal", "Shield Ring", "Silence Ring", "Star of Lachiem", "Sun Ring", "Tailwind Ring"]
    spells = ["Arm Cannon", "Aura Blast", "Aura Serpent", "Bombardment", "Chaos Blades", "Colossal Blade", "Colossal Hammer", "Corruption",
                   "Crimson Vortex", "Dark Flames", "Djinn Inferno", "Icicle Crash", "Infernal Flames", "Lightwall", "Plasma Geyser", "Storm Eye"]
    armor = ["Advisor Robe", "Copper Breastplate", "Dragoon Armor", "Empress Robe", "Eternal Coat", "Lab Coat", "Leather Jerkin", "Librarian Robe",
                   "Midnight Cloak", "Military Armor", "Old Coat", "Princess Dress", "Security Vest", "Travellers Cloak", "Trendy Jacket"]
    headgear = ["Advisor Hat", "Buckle Hat", "Captains Helmet", "Combat Helmet", "Copper Helmet", "Dragoon Helmet", "Empire Crown", "Engineer Goggles",
                     "Eternal Crown", "Lab Glasses", "Leather Helmet", "Librarian Hat", "Pointy Hat", "Security Visor", "Sunglasses", "Viletian Crown"]
    trinkets = ["Ancient Coin", "Azure Stole", "Bird Statue", "Chaos Horn", "Chaos Stole", "Cheveur Plume", "Filigree Clasp", "Galaxy Earrings",
                     "Gilded Egg", "Glass Pumpkin", "Metal Wristband", "Mother of Pearl", "Nymph Hairband", "Pendulum", "Selens Bangle", "Synthetic Plume"]
    keycards = ["Elevator Keycard", "Keycard A", "Keycard B", "Keycard C", "Keycard D", "Keycard V"]
    familiars = ["Demon", "Griffin", "Kobo", "Merchant Crow", "Meyef", "Sprite"]
    miscellaneous = ["Aura Up", "Elemental Beads", "Essence Crystal", "Gold Necklace", "Gold Ring", "Health Up", "Herb", "Sand Up", "Shiny Rock"]

    def __init__(self, master, settings):
                 #,useConsumables = True, useQuestItems = True, 
                 #useRelics = True, useOrbs = True, usePassives = True, 
                 #useSpells = True, useArmors = True, useHeadgear = True, 
                 #useTrinkets = True, useKeycards = True, useMiscellaneous = True,
                 #useFamiliars = True, compactMode = False, allowDuplicates = True,
                 #rows = 5, columns = 5
        #self.rows = rows
        #self.columns = columns
        self.master = master
        self.icons = {}
        self.tooltips = []

        self.settings = settings

        if self.settings.questItems["value"]:
            for item in self.settings.questItems["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                   
        if self.settings.relics["value"]:
            for item in self.settings.relics["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.orbs["value"]:
            for item in self.settings.orbs["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.passives["value"]:
            for item in self.settings.passives["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                   
        if self.settings.spells["value"]:
            for item in self.settings.spells["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.armor["value"]:
            for item in self.settings.armor["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.headgear["value"]:
            for item in self.settings.headgear["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                   
        if self.settings.trinkets["value"]:
            for item in self.settings.trinkets["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.keycards["value"]:
            for item in self.settings.keycards["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.familiars["value"]:
            for item in self.settings.familiars["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if self.settings.miscellaneous["value"]:
            for item in self.settings.miscellaneous["items"]:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
        
        for c in range(int(self.settings.columns["value"])):
            for r in range(int(self.settings.rows["value"])):
                frame = tkinter.Frame(
                    self.master
                )
                frame.grid(row=r, column=c, padx=2, pady=2)
                randomkey = random.choice(list(self.icons.keys()))
                if self.settings.allowDuplicates:
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
                        text = randomkey[:6] + randomkey[6:12].replace(" ", "\n", 1) + randomkey[12:],
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
        x += self.widget.winfo_rootx() #- (self.widget.winfo_width() / 2)
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
    



