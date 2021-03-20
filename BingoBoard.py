import tkinter
import os
import random

class BingoBoard():
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
    armors = ["Advisor Robe", "Copper Breastplate", "Dragoon Armor", "Empress Robe", "Eternal Coat", "Lab Coat", "Leather Jerkin", "Librarian Robe",
                   "Midnight Cloak", "Military Armor", "Old Coat", "Princess Dress", "Security Vest", "Travellers Cloak", "Trendy Jacket"]
    headgear = ["Advisor Hat", "Buckle Hat", "Captains Helmet", "Combat Helmet", "Copper Helmet", "Dragoon Helmet", "Empire Crown", "Engineer Goggles",
                     "Eternal Crown", "Lab Glasses", "Leather Helmet", "Librarian Hat", "Pointy Hat", "Security Visor", "Sunglasses", "Viletian Crown"]
    trinkets = ["Ancient Coin", "Azure Stole", "Bird Statue", "Chaos Horn", "Chaos Stole", "Cheveur Plume", "Filigree Clasp", "Galaxy Earrings",
                     "Gilded Egg", "Glass Pumpkin", "Metal Wristband", "Mother of Pearl", "Nymph Hairband", "Pendulum", "Selens Bangle", "Synthetic Plume"]
    keycards = ["Elevator Keycard", "Keycard A", "Keycard B", "Keycard C", "Keycard D", "Keycard V"]
    familiars = ["Demon", "Griffin", "Kobo", "Merchant Crow", "Meyef", "Sprite"]
    miscellaneous = ["Aura Up", "Elemental Beads", "Essence Crystal", "Gold Necklace", "Gold Ring", "Health Up", "Herb", "Sand Up", "Shiny Rock"]

    def __init__(self, useConsumables = True, useQuestItems = True, 
                 useRelics = True, useOrbs = True, usePassives = True, 
                 useSpells = True, useArmors = True, useHeadgear = True, 
                 useTrinkets = True, useKeycards = True, useMiscellaneous = True,
                 useFamiliars = True, rows = 5, columns = 5):
        self.root = tkinter.Tk()
        self.rows = rows
        self.columns = columns
        self.icons = {}

        if useQuestItems:
            for item in self.quest_items:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                   
        if useRelics:
            for item in self.relics:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if useOrbs:
            for item in self.orbs:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if usePassives:
            for item in self.passives:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                   
        if useSpells:
            for item in self.spells:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if useArmors:
            for item in self.armors:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if useHeadgear:
            for item in self.headgear:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)
                   
        if useTrinkets:
            for item in self.trinkets:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if useKeycards:
            for item in self.keycards:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if useFamiliars:
            for item in self.familiars:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        if useMiscellaneous:
            for item in self.miscellaneous:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item + ".png")).zoom(2)

        for c in range(self.columns):
            for r in range(self.rows):
                frame = tkinter.Frame(
                    master = self.root
                )
                frame.grid(row=r, column=c, padx=2, pady=2)
                randomkey = random.choice(list(self.icons.keys()))
                icon = self.icons.pop(randomkey)
                button = tkinter.Button(
                    master = frame,
                    text = randomkey,
                    image = icon,
                    width = icon.width() * 4,
                    height = icon.height() * 2,
                    compound = tkinter.BOTTOM,
                    bg = "white"
                )
                button.config(command = lambda arg=button:buttonClick(arg))
                button.image = icon
                button.pack()

        #Button click event handler
        def buttonClick(arg):
            if arg["bg"] == "white":
                arg["bg"] = "green"
            elif arg["bg"] == "green":
                arg["bg"] = "white"


    def loadQuestItems(self):
        for item in self.quest_items:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)
                
    def loadRelics(self):
        for item in self.relics:
                if item not in self.icons.keys():
                    self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadOrbs(self):
        for item in self.orbs:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadPassives(self):
        for item in self.passives:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadSpells(self):
        for item in self.spells:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadArmors(self):
        for item in self.armors:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadHeadgear(self):
        for item in self.headgear:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadTrinkets(self):
        for item in self.trinkets:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadKeycards(self):
        for item in self.keycards:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadFamiliars(self):
        for item in self.familiars:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def loadMiscellaneous(self):
        for item in self.miscellaneous:
            if item not in self.icons.keys():
                self.icons[item] = tkinter.PhotoImage(file = os.path.join(self.iconDirectory, item)).zoom(2)

    def displayGrid(self):
        for c in range(COLUMNS):
            for r in range(ROWS):
                frame = tkinter.Frame(
                    master = self

                )
                frame.grid(row=r, column=c, padx=2, pady=2)
                randomkey = random.choice(list(self.icons.keys()))
                icon = self.icons.pop(randomkey)
                button = tkinter.Button(
                    master = frame,
                    text = randomkey,
                    image = icon,
                    width = icon.width() * 4,
                    height = icon.height() * 2,
                    compound = tkinter.BOTTOM,
                    bg = "white"
                )
                button.config(command = lambda arg=button:buttonClick(arg))
                button.image = icon
                button.pack()

    



