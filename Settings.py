import os
import json
import codecs
import sys
from tkinter import messagebox

if getattr(sys, "frozen", False):
    SETTINGS_PATH = os.path.join(os.path.dirname(sys.executable), "settings.txt")
elif __file__:
    SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.txt")

class Settings(object):
    def __init__(self):
        #Apply default settings
        self.SETTINGS_VERSION = "1.2.2"
        self.consumables = {"friendlyName":"Use Consumables", "settingtype": "item", "value":True, "items":["Antidote", "Berry Pick-Mi-Up", "Berry Pick-Mi-Up+", "Biscuit", "Chaos Rose", "Cheveur Breast", "Cheveur Drumstick",
                        "Dream Wisp", "Eel Meat", "Empress Cake", "Ether", "Filigree Tea", "Hi-Ether", "Hi-Potion", "Jerky", "Mind Refresh Ultra",
                        "Mind Refresh", "Mushroom", "Orange Juice", "Plump Maggot", "Potion", "Rotten Tail", "Sand Bottle", "Sand Vial",
                        "Spaghetti", "Warp Shard", "Wyvern Tail"]}
        self.questItems = {"friendlyName":"Use Quest Items", "settingtype": "item", "value":True, "items":["Alchemy Backpack", "Cheveur Breast", "Cheveur Drumstick", "Cheveur Feather", "Eel Meat", "Food Synthesizer", "Galaxy Stone", 
                        "Herb", "Mushroom", "Plasma Core", "Plasma Crystal", "Plasma IV Bag", "Silver Ore", "Siren Ink", "Wyvern Tail" ]}
        self.relics = {"friendlyName":"Use Relics", "settingtype": "item", "value":True, "items":["Celestial Sash", "Eternal Brooch", "Gas Mask", "Goddess Brooch", "Greed Brooch", "Jewelry Box", "Soul Scanner", "Succubus Hairpin",
                   "Tablet", "Talaria Attachment", "Timespinner Gear 1", "Timespinner Gear 2", "Timespinner Gear 3", "Timespinner Spindle",
                   "Timespinner Wheel", "Twin Pyramids", "Water Mask", "Wyrm Brooch"]}
        self.orbs = {"friendlyName":"Use Orbs", "settingtype": "item", "value":True, "items":["Blade Orb", "Blood Orb", "Blue Orb", "Empire Orb", "Eye Orb", "Fire Orb", "Forbidden Tome", "Gun Orb", "Ice Orb", "Iron Orb",
                 "Nether Orb", "Plasma Orb", "Radiant Orb", "Shattered Orb", "Umbra Orb", "Wind Orb"]}
        self.passives = {"friendlyName":"Use Passives", "settingtype": "item", "value":True, "items":["Bleak Ring", "Dusk Ring", "Economizer", "Hope Ring", "Icicle Ring", "Oculus Ring", "Pyro Ring", "Royal Ring", "Sanguine Ring",
                     "Scythe Ring", "Shadow Seal", "Shield Ring", "Silence Ring", "Star of Lachiem", "Sun Ring", "Tailwind Ring"]} 
        self.spells = {"friendlyName":"Use Spells", "settingtype": "item", "value":True, "items":["Arm Cannon", "Aura Blast", "Aura Serpent", "Bombardment", "Chaos Blades", "Colossal Blade", "Colossal Hammer", "Corruption",
                   "Crimson Vortex", "Dark Flames", "Djinn Inferno", "Icicle Crash", "Infernal Flames", "Lightwall", "Plasma Geyser", "Storm Eye"]}
        self.armor = {"friendlyName":"Use Armor", "settingtype": "item", "value":True, "items":["Advisor Robe", "Copper Breastplate", "Dragoon Armor", "Empress Robe", "Eternal Coat", "Lab Coat", "Leather Jerkin", "Librarian Robe",
                   "Midnight Cloak", "Military Armor", "Old Coat", "Princess Dress", "Security Vest", "Travellers Cloak", "Trendy Jacket"]}
        self.headgear = {"friendlyName":"Use Headgear", "settingtype": "item", "value":True, "items":["Advisor Hat", "Buckle Hat", "Captains Helmet", "Combat Helmet", "Copper Helmet", "Dragoon Helmet", "Empire Crown", "Engineer Goggles",
                     "Eternal Crown", "Lab Glasses", "Leather Helmet", "Librarian Hat", "Pointy Hat", "Security Visor", "Sunglasses", "Viletian Crown"]} 
        self.trinkets = {"friendlyName":"Use Trinkets", "settingtype": "item", "value":True, "items":["Ancient Coin", "Azure Stole", "Bird Statue", "Chaos Horn", "Chaos Stole", "Cheveur Plume", "Filigree Clasp", "Galaxy Earrings",
                     "Gilded Egg", "Glass Pumpkin", "Metal Wristband", "Mother of Pearl", "Nymph Hairband", "Pendulum", "Selens Bangle", "Synthetic Plume"]}
        self.keycards = {"friendlyName":"Use Keycards", "settingtype": "item", "value":True, "items":["Elevator Keycard", "Keycard A", "Keycard B", "Keycard C", "Keycard D", "Keycard V"]}
        self.familiars = {"friendlyName":"Use Familiars", "settingtype": "item", "value":True, "items":["Demon", "Griffin", "Kobo", "Merchant Crow", "Meyef", "Sprite"]}
        self.bosses = {"friendlyName":"Use Bosses", "settingtype": "item", "value":True, "items":["Boots", "Idol", "Aelana", "Maw", "Genza", "Daddy", "Vol", "Xarion", "Nightmare"]}
        self.miscellaneous = {"friendlyName":"Use Miscellaneous", "settingtype": "item", "value":True, "items":["Aura Up", "Elemental Beads", "Essence Crystal", "Gold Necklace", "Gold Ring", "Health Up", "Herb", "Sand Up", "Shiny Rock"]}
        self.excludeMeyef = {"friendlyName":"Exclude Meyef", "settingtype": "exclusion", "value":False}
        self.excludeJewelryBox = {"friendlyName":"Exclude Jewelry Box", "settingtype": "exclusion", "value":False}
        self.excludeTalariaAttachment = {"friendlyName":"Exclude Talaria Attachment", "settingtype": "exclusion", "value":False}
        self.excludeKickstarterItems = {"friendlyName":"Exclude Kickstarter-exclusive Items", "settingtype": "exclusion", "value":False}
        self.excludeRareItems = {"friendlyName":"Exclude Rare Items", "settingtype": "exclusion", "value":False}
        self.useCompactMode = {"friendlyName":"Use Compact Mode", "settingtype": "generation", "value":False}
        self.allowDuplicates = {"friendlyName":"Allow Duplicates", "settingtype": "generation", "value":False}
        self.rows = {"friendlyName":"Number of Rows", "settingtype": "generation", "value":5}
        self.columns = {"friendlyName":"Number of Columns", "settingtype": "generation", "value":5}

        #If a settings file exists, apply the settings from that file
        if SETTINGS_PATH and os.path.isfile(SETTINGS_PATH):
            #Load settings from file
            try:
                with codecs.open(SETTINGS_PATH, encoding="utf-8-sig", mode="r") as f:
                    newSettings = json.load(f)
                    if "SETTINGS_VERSION" in newSettings.keys() and newSettings["SETTINGS_VERSION"] == self.SETTINGS_VERSION:
                        self.__dict__ = newSettings
                    else:
                        messagebox.showerror("Notice", "A settings file from a different version of TimespinnerBingo has been detected - your settings may be reset.")
                #for k, v in newSettings.items():
                #    if "version" in k and newSettings["version"] == self.version:
                #        self.__dict__[k] = v
                #    else:
                #        messagebox.showerror("Notice", "An incompatible settings file has been detected - your settings may be reset.")
                #        break
            except:
                print("Handled error loading settings from file.")
        
        ##Save the settings to file
        self.Save()

    #Reload settings from file
    def Reload(self):
        with codecs.open(SETTINGS_PATH, encoding="utf-8-sig", mode="r") as f:
            self.__dict__ = json.load(f, encoding="utf-8")
        return

    #Save settings to file
    def Save(self):
        try:
            with codecs.open(SETTINGS_PATH, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f)
        except Exception as e:
            print("Error saving file: " + str(e))
        return

    #Getter
    def useConsumables(self):
        return self.consumables["value"]

    #Setter
    def setConsumables(self, arg):
        if type(arg) is bool:
            self.consumables["value"] = arg
        else:
            raise TypeError("Bad argument passed to the consumables setter.")
        return

    #Getter
    def useQuestItems(self):
        return self.questItems["value"]

    #Setter
    def setQuestItems(self, arg):
        if type(arg) is bool:
            self.questItems["value"] = arg
        else:
            raise TypeError("Bad argument passed to the questItems setter.")
        return

    #Getter
    def useRelics(self):
        return self.relics["value"]

    #Setter
    def setrelics(self, arg):
        if type(arg) is bool:
            self.relics["value"] = arg
        else:
            raise TypeError("Bad argument passed to the relics setter.")
        return

    #Getter
    def useOrbs(self):
        return self.orbs["value"]

    #Setter
    def setOrbs(self, arg):
        if type(arg) is bool:
            self.orbs["value"] = arg
        else:
            raise TypeError("Bad argument passed to the orbs setter.")
        return

    #Getter
    def usePassives(self):
        return self.passives["value"]

    #Setter
    def setPassives(self, arg):
        if type(arg) is bool:
            self.passives["value"] = arg
        else:
            raise TypeError("Bad argument passed to the passives setter.")
        returnspells

    #Getter
    def useSpells(self):
        return self.spells["value"]

    #Setter
    def setSpells(self, arg):
        if type(arg) is bool:
            self.spells["value"] = arg
        else:
            raise TypeError("Bad argument passed to the spells setter.")
        return

    #Getter
    def useArmor(self):
        return self.armor["value"]

    #Setter
    def setArmor(self, arg):
        if type(arg) is bool:
            self.armor["value"] = arg
        else:
            raise TypeError("Bad argument passed to the armor setter.")
        return

    #Getter
    def useHeadgear(self):
        return self.headgear["value"]

    #Setter
    def setHeadgear(self, arg):
        if type(arg) is bool:
            self.headgear["value"] = arg
        else:
            raise TypeError("Bad argument passed to the headgear setter.")
        return

    #Getter
    def useTrinkets(self):
        return self.useTrinkets["value"]

    #Setter
    def setUseTrinkets(self, arg):
        if type(arg) is bool:
            self.useTrinkets["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useTrinkets setter.")
        return

    #Getter
    def useKeycards(self):
        return self.useKeycards["value"]

    #Setter
    def setUseKeycards(self, arg):
        if type(arg) is bool:
            self.useKeycards["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useKeycards setter.")
        return

    #Getter
    def useFamiliars(self):
        return self.useFamiliars["value"]

    #Setter
    def setUseFamiliars(self, arg):
        if type(arg) is bool:
            self.useFamiliars["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useFamiliars setter.")
        return

    #Getter
    def useMiscellaneous(self):
        return self.useMiscellaneous["value"]

    #Setter
    def setUseMiscellaneous(self, arg):
        if type(arg) is bool:
            self.useMiscellaneous["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useMiscellaneous setter.")
        return

    #Getter
    def rows(self):
        return self.rows

    #Setter
    def setRows(self, arg):
        if type(arg) is int:
            self.rows["value"] = arg
        else:
            raise TypeError("Bad argument passed to the rows setter.")
        return

    #Getter
    def columns(self):
        return self.columns

    #Setter
    def setColumns(self, arg):
        if type(arg) is int:
            self.columns["value"] = arg
        else:
            raise TypeError("Bad argument passed to the columns setter.")
        return

    #Getter
    def useCompactMode(self):
        return self.useCompactMode

    #Setter
    def setUseCompactMode(self, arg):
        if type(arg) is bool:
            self.useCompactMode["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useCompactMode setter.")
        return

    #Getter
    def allowDuplicates(self):
        return self.allowDuplicates

    #Setter
    def setAllowDuplicates(self, arg):
        if type(arg) is bool:
            self.allowDuplicates["value"] = arg
        else:
            raise TypeError("Bad argument passed to the allowDuplicates setter.")
        return

    def items(self):
        return self.__dict__.items()


