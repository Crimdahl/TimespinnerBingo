import os
import json
import codecs
import sys
from time import time
from tkinter import messagebox

if getattr(sys, "frozen", False):
    SETTINGS_PATH = os.path.join(os.path.dirname(sys.executable), "settings.txt")
elif __file__:
    SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.txt")


class Settings(object):
    def __init__(self):
        # Apply default settings
        self.SETTINGS_VERSION = "1.3.0"
        self.consumables = {"friendlyName": "Use Consumables", "settingtype": "item", "value": True,
                            "items": ["Antidote", "Berry Pick-Mi-Up", "Berry Pick-Mi-Up+", "Biscuit", "Chaos Rose",
                                      "Cheveur Breast", "Cheveur Drumstick",
                                      "Dream Wisp", "Eel Meat", "Empress Cake", "Ether", "Filigree Tea", "Hi-Ether",
                                      "Hi-Potion", "Jerky", "Mind Refresh Ultra",
                                      "Mind Refresh", "Mushroom", "Orange Juice", "Plump Maggot", "Potion",
                                      "Rotten Tail", "Sand Bottle", "Sand Vial",
                                      "Spaghetti", "Warp Shard", "Wyvern Tail"]}
        self.quest_items = {"friendlyName": "Use Quest Items", "settingtype": "item", "value": True,
                           "items": ["Alchemy Backpack", "Cheveur Breast", "Cheveur Drumstick", "Cheveur Feather",
                                     "Eel Meat", "Food Synthesizer", "Galaxy Stone",
                                     "Herb", "Mushroom", "Plasma Core", "Plasma Crystal", "Plasma IV Bag", "Silver Ore",
                                     "Siren Ink", "Wyvern Tail"]}
        self.relics = {"friendlyName": "Use Relics", "settingtype": "item", "value": True,
                       "items": ["Celestial Sash", "Eternal Brooch", "Gas Mask", "Goddess Brooch", "Greed Brooch",
                                 "Jewelry Box", "Soul Scanner", "Succubus Hairpin",
                                 "Tablet", "Talaria Attachment", "Timespinner Gear 1", "Timespinner Gear 2",
                                 "Timespinner Gear 3", "Timespinner Spindle",
                                 "Timespinner Wheel", "Twin Pyramids", "Water Mask", "Wyrm Brooch"]}
        self.orbs = {"friendlyName": "Use Orbs", "settingtype": "item", "value": True,
                     "items": ["Blade Orb", "Blood Orb", "Blue Orb", "Empire Orb", "Eye Orb", "Fire Orb",
                               "Forbidden Tome", "Gun Orb", "Ice Orb", "Iron Orb",
                               "Nether Orb", "Plasma Orb", "Radiant Orb", "Shattered Orb", "Umbra Orb", "Wind Orb"]}
        self.passives = {"friendlyName": "Use Passives", "settingtype": "item", "value": True,
                         "items": ["Bleak Ring", "Dusk Ring", "Economizer", "Hope Ring", "Icicle Ring", "Oculus Ring",
                                   "Pyro Ring", "Royal Ring", "Sanguine Ring",
                                   "Scythe Ring", "Shadow Seal", "Shield Ring", "Silence Ring", "Star of Lachiem",
                                   "Sun Ring", "Tailwind Ring"]}
        self.spells = {"friendlyName": "Use Spells", "settingtype": "item", "value": True,
                       "items": ["Arm Cannon", "Aura Blast", "Aura Serpent", "Bombardment", "Chaos Blades",
                                 "Colossal Blade", "Colossal Hammer", "Corruption",
                                 "Crimson Vortex", "Dark Flames", "Djinn Inferno", "Icicle Crash", "Infernal Flames",
                                 "Lightwall", "Plasma Geyser", "Storm Eye"]}
        self.armor = {"friendlyName": "Use Armor", "settingtype": "item", "value": True,
                      "items": ["Advisor Robe", "Copper Breastplate", "Dragoon Armor", "Empress Robe", "Eternal Coat",
                                "Lab Coat", "Leather Jerkin", "Librarian Robe",
                                "Midnight Cloak", "Military Armor", "Old Coat", "Princess Dress", "Security Vest",
                                "Travellers Cloak", "Trendy Jacket"]}
        self.headgear = {"friendlyName": "Use Headgear", "settingtype": "item", "value": True,
                         "items": ["Advisor Hat", "Buckle Hat", "Captains Helmet", "Combat Helmet", "Copper Helmet",
                                   "Dragoon Helmet", "Empire Crown", "Engineer Goggles",
                                   "Eternal Crown", "Lab Glasses", "Leather Helmet", "Librarian Hat", "Pointy Hat",
                                   "Security Visor", "Sunglasses", "Viletian Crown"]}
        self.trinkets = {"friendlyName": "Use Trinkets", "settingtype": "item", "value": True,
                         "items": ["Ancient Coin", "Azure Stole", "Bird Statue", "Chaos Horn", "Chaos Stole",
                                   "Cheveur Plume", "Filigree Clasp", "Galaxy Earrings",
                                   "Gilded Egg", "Glass Pumpkin", "Metal Wristband", "Mother of Pearl",
                                   "Nymph Hairband", "Pendulum", "Selens Bangle", "Synthetic Plume"]}
        self.keycards = {"friendlyName": "Use Keycards", "settingtype": "item", "value": True,
                         "items": ["Elevator Keycard", "Keycard A", "Keycard B", "Keycard C", "Keycard D", "Keycard V"]}
        self.familiars = {"friendlyName": "Use Familiars", "settingtype": "item", "value": True,
                          "items": ["Demon", "Griffin", "Kobo", "Merchant Crow", "Meyef", "Sprite"]}
        self.bosses = {"friendlyName": "Use Bosses", "settingtype": "item", "value": True,
                       "items": ["Boots", "Idol", "Aelana", "Maw", "Genza", "Daddy", "Vol", "Xarion", "Nightmare"]}
        self.miscellaneous = {"friendlyName": "Use Miscellaneous", "settingtype": "item", "value": True,
                              "items": ["Aura Up", "Elemental Beads", "Essence Crystal", "Gold Necklace", "Gold Ring",
                                        "Health Up", "Herb", "Sand Up", "Shiny Rock"]}
        self.exclude_meyef = {"friendlyName": "Exclude Meyef", "settingtype": "exclusion", "value": False}
        self.exclude_jewelry_box = {"friendlyName": "Exclude Jewelry Box", "settingtype": "exclusion", "value": False}
        self.exclude_talaria_attachment = {"friendlyName": "Exclude Talaria Attachment", "settingtype": "exclusion",
                                         "value": False}
        self.exclude_kickstarter_items = {"friendlyName": "Exclude Kickstarter-exclusive Items",
                                        "settingtype": "exclusion", "value": False}
        self.exclude_rare_items = {"friendlyName": "Exclude Rare Items", "settingtype": "exclusion", "value": False}
        self.use_compact_mode = {"friendlyName": "Use Compact Mode", "settingtype": "generation", "value": False}
        self.allow_duplicates = {"friendlyName": "Allow Duplicates", "settingtype": "generation", "value": False}
        self.rows = {"friendlyName": "Number of Rows", "settingtype": "generation", "value": 5}
        self.columns = {"friendlyName": "Number of Columns", "settingtype": "generation", "value": 5}
        self.seed = int(time() * 1000)
        print(str(self.seed))

        # If a settings file exists, apply the settings from that file
        if SETTINGS_PATH and os.path.isfile(SETTINGS_PATH):
            # Load settings from file
            try:
                with codecs.open(SETTINGS_PATH, encoding="utf-8-sig", mode="r") as f:
                    new_settings = json.load(f)
                    if "SETTINGS_VERSION" in new_settings.keys() and new_settings["SETTINGS_VERSION"] == \
                            self.SETTINGS_VERSION:
                        new_settings["seed"] = int(time() * 1000)
                        self.__dict__ = new_settings
                    else:
                        messagebox.showerror("Notice", "A settings file from a different version of TimespinnerBingo "
                                                       "has been detected - your settings may be reset.")
            except:
                print("Handled error loading settings from file.")

        # Save the settings to file
        self.save_settings()

    # Reload settings from file
    def reload_settings(self):
        with codecs.open(SETTINGS_PATH, encoding="utf-8-sig", mode="r") as f:
            self.__dict__ = json.load(f, encoding="utf-8")
        return

    # Save settings to file
    def save_settings(self):
        try:
            with codecs.open(SETTINGS_PATH, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f)
        except Exception as e:
            print("Error saving file: " + str(e))
        return

    # Getter
    def get_use_consumables(self):
        return self.consumables["value"]

    # Setter
    def set_use_consumables(self, arg):
        if type(arg) is bool:
            self.consumables["value"] = arg
        else:
            raise TypeError("Bad argument passed to the consumables setter.")
        return

    # Getter
    def get_use_quest_items(self):
        return self.quest_items["value"]

    # Setter
    def set_use_quest_items(self, arg):
        if type(arg) is bool:
            self.quest_items["value"] = arg
        else:
            raise TypeError("Bad argument passed to the questItems setter.")
        return

    # Getter
    def get_use_relics(self):
        return self.relics["value"]

    # Setter
    def set_use_relics(self, arg):
        if type(arg) is bool:
            self.relics["value"] = arg
        else:
            raise TypeError("Bad argument passed to the relics setter.")
        return

    # Getter
    def get_use_orbs(self):
        return self.orbs["value"]

    # Setter
    def set_use_orbs(self, arg):
        if type(arg) is bool:
            self.orbs["value"] = arg
        else:
            raise TypeError("Bad argument passed to the orbs setter.")
        return

    # Getter
    def get_use_passives(self):
        return self.passives["value"]

    # Setter
    def set_use_passives(self, arg):
        if type(arg) is bool:
            self.passives["value"] = arg
        else:
            raise TypeError("Bad argument passed to the passives setter.")
        return

    # Getter
    def get_use_spells(self):
        return self.spells["value"]

    # Setter
    def set_use_spells(self, arg):
        if type(arg) is bool:
            self.spells["value"] = arg
        else:
            raise TypeError("Bad argument passed to the spells setter.")
        return

    # Getter
    def get_use_armor(self):
        return self.armor["value"]

    # Setter
    def set_use_armor(self, arg):
        if type(arg) is bool:
            self.armor["value"] = arg
        else:
            raise TypeError("Bad argument passed to the armor setter.")
        return

    # Getter
    def get_use_headgear(self):
        return self.headgear["value"]

    # Setter
    def set_use_headgear(self, arg):
        if type(arg) is bool:
            self.headgear["value"] = arg
        else:
            raise TypeError("Bad argument passed to the headgear setter.")
        return

    # Getter
    def get_use_trinkets(self):
        return self.get_use_trinkets["value"]

    # Setter
    def set_use_trinkets(self, arg):
        if type(arg) is bool:
            self.get_use_trinkets["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useTrinkets setter.")
        return

    # Getter
    def get_use_keycards(self):
        return self.get_use_keycards["value"]

    # Setter
    def set_use_keycards(self, arg):
        if type(arg) is bool:
            self.get_use_keycards["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useKeycards setter.")
        return

    # Getter
    def get_use_familiars(self):
        return self.get_use_familiars["value"]

    # Setter
    def set_use_familiars(self, arg):
        if type(arg) is bool:
            self.get_use_familiars["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useFamiliars setter.")
        return

    # Getter
    def get_use_miscellaneous(self):
        return self.get_use_miscellaneous["value"]

    # Setter
    def set_use_miscellaneous(self, arg):
        if type(arg) is bool:
            self.get_use_miscellaneous["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useMiscellaneous setter.")
        return

    # Getter
    def get_rows(self):
        return self.rows

    # Setter
    def set_rows(self, arg):
        if type(arg) is int:
            self.rows["value"] = arg
        else:
            raise TypeError("Bad argument passed to the rows setter.")
        return

    # Getter
    def get_columns(self):
        return self.columns

    # Setter
    def set_columns(self, arg):
        if type(arg) is int:
            self.columns["value"] = arg
        else:
            raise TypeError("Bad argument passed to the columns setter.")
        return

    # Getter
    def get_use_compact_mode(self):
        return self.use_compact_mode

    # Setter
    def set_use_compact_mode(self, arg):
        if type(arg) is bool:
            self.use_compact_mode["value"] = arg
        else:
            raise TypeError("Bad argument passed to the useCompactMode setter.")
        return

    # Getter
    def get_allow_duplicates(self):
        return self.allow_duplicates

    # Setter
    def set_allow_duplicates(self, arg):
        if type(arg) is bool:
            self.allow_duplicates["value"] = arg
        else:
            raise TypeError("Bad argument passed to the allowDuplicates setter.")
        return

    # Getter
    def get_seed(self):
        return self.seed

    # Setter
    def set_seed(self, arg):
        if type(arg) is int:
            self.seed = arg
        else:
            raise TypeError("Bad argument passed to the setSeed setter.")
        return

    def items(self):
        return self.__dict__.items()
