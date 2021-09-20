import os
import json
import codecs
import sys
from time import time
from tkinter import messagebox

if getattr(sys, "frozen", False):
    CONFIG_PATH = os.path.join(os.path.dirname(sys.executable), "config.txt")
elif __file__:
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.txt")


class Config(object):
    def __init__(self):
        # Apply default settings
        self.CONFIG_VERSION = "1.1.4"
        # If a settings file exists, apply the settings from that file
        try:
            with codecs.open(CONFIG_PATH, encoding="utf-8-sig", mode="r") as f:
                new_settings = json.load(f)
                if "CONFIG_VERSION" in new_settings.keys() and new_settings["CONFIG_VERSION"] == \
                        self.CONFIG_VERSION:
                    new_settings["seed"] = int(time() * 1000)
                    self.__dict__ = new_settings
                else:
                    messagebox.showerror("Notice", "A settings file from a different version of TimespinnerBingo "
                                                   "has been detected - your settings may be reset.")
                    raise IOError
        except IOError:
            self.tile_data = {
                "advisor hat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "advisor robe": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "aelana": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "alchemy backpack": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items"
                    ]
                },
                "ancient coin": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "shop items"
                    ]
                },
                "ancient frail": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "antheia": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "antidote": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "arm cannon": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: piercing", "element: light", "set: gun"
                    ]
                },
                "aura blast": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: aura", "set: blue"
                    ]
                },
                "aura serpent": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: aura", "set: empire"
                    ]
                },
                "aura up": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "stat upgrades"
                    ]
                },
                "azure stole": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops", "enemy drops: rare"
                    ]
                },
                "azure queen": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "baby cheveur": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "barbed anemone": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "berry pick-mi-up": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "shop items"
                    ]
                },
                "berry pick-mi-up+": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables"
                    ]
                },
                "bird statue": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets"
                    ]
                },
                "biscuit": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "shop items"
                    ]
                },
                "blade orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: sharp", "set: blade"
                    ]
                },
                "bleak ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: blue"
                    ]
                },
                "blood orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: dark", "set: blood"
                    ]
                },
                "blossom automaton": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "blue orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: blunt", "set: blue"
                    ]
                },
                "bombardment": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: blunt", "set: shattered"
                    ]
                },
                "buckle hat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "cantoran": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses", "quest locked"
                    ]
                },
                "captain's helmet": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "captain's uniform": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "celestial sash": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "progression: vertical"
                    ]
                },
                "chaos blades": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: sharp", "set: eye"
                    ]
                },
                "chaos horn": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops", "enemy drops: rare"
                    ]
                },
                "chaos rose": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "shop items"
                    ]
                },
                "chaos stole": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops", "enemy drops: rare"
                    ]
                },
                "cheveur au vin": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest locked", "shop items"
                    ]
                },
                "cheveur breast": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items", "enemy drops"
                    ]
                },
                "cheveur dragoon": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "cheveur drumstick": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items", "enemy drops"
                    ]
                },
                "cheveur feather": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items", "enemy drops"
                    ]
                },
                "cheveur fly": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "cheveur hatchling": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "cheveur helicopter": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "cheveur plume": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops"
                    ]
                },
                "cheveur spring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "cheveur tank": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "colossal blade": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: sharp", "set: blade"
                    ]
                },
                "colossal hammer": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: blunt", "set: iron"
                    ]
                },
                "combat helmet": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats", "enemy drops"
                    ]
                },
                "conviction": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "copper breastplate": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors", "enemy drops"
                    ]
                },
                "copper helmet": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors", "enemy drops"
                    ]
                },
                "copper wyvern": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "corruption": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: dark", "set: nether"
                    ]
                },
                "creeping fungus": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "crimson vortex": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: dark", "set: blood"
                    ]
                },
                "dark flames": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: dark", "set: umbra"
                    ]
                },
                "demon": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "familiars"
                    ]
                },
                "demon guard": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "devil's vine": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "djinn": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses", "vanilla only"
                    ]
                },
                "djinn inferno": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: fire", "set: forbidden"
                    ]
                },
                "dragoon armor": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors", "quest items", "quest locked"
                    ]
                },
                "dragoon helmet": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats", "enemy drops"
                    ]
                },
                "dream wisp": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "enemy drops: rare"
                    ]
                },
                "dusk ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: umbra"
                    ]
                },
                "economizer ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: gun"
                    ]
                },
                "ectoplasm": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "eel meat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "quest items"
                    ]
                },
                "elemental beads": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "crafting", "enemy drops", "enemy drops: rare"
                    ]
                },
                "elevator keycard": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "progression", "relics"
                    ]
                },
                "empire crown": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "empire giantess": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "empire knight": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "empire orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: aura", "set: empire"
                    ]
                },
                "empire sniper": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "empress cake": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "empress robe": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "engineer goggles": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats", "enemy drops"
                    ]
                },
                "essence crystal": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "crafting", "shop items", "quest items"
                    ]
                },
                "eternal brooch": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "relics: cosmetics"
                    ]
                },
                "eternal coat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "eternal crown": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "ether": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "shop items"
                    ]
                },
                "experiment 11": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "experiment 13": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "eye orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: sharp", "set: eye"
                    ]
                },
                "fanged anemone": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "feline sentry": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "fetid wyvern": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "fiend": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "filigree clasp": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets"
                    ]
                },
                "filigree tea": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "fire orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: fire", "set: fire"
                    ]
                },
                "flesh arachnid": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "fledgling warbird": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "food synthesizer": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items"
                    ]
                },
                "forbidden tome": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: sharp", "set: forbidden"
                    ]
                },
                "freshwater eel": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "fried cheveur": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest locked", "shop items"
                    ]
                },
                "frozen spires": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: ice", "set: ice"
                    ]
                },
                "galactic sage": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "galaxy earrings": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets"
                    ]
                },
                "galaxy stone": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items"
                    ]
                },
                "gas mask": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression"
                    ]
                },
                "genza": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "gilded egg": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "shop items"
                    ]
                },
                "glass pumpkin": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "danger: vanilla"
                    ]
                },
                "goddess brooch": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "relics: cosmetics"
                    ]
                },
                "gold necklace": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "crafting", "shop items"
                    ]
                },
                "gold ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "crafting", "shop items"
                    ]
                },
                "golden idol": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "greed brooch": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "relics: cosmetics", "kickstarter exclusive"
                    ]
                },
                "griffin": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "familiars"
                    ]
                },
                "gun orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: sharp", "set: gun"
                    ]
                },
                "harvest rat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "health up": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "stat upgrades"
                    ]
                },
                "helix toad": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "hell gazer": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "herb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "crafting", "enemy drops", "quest items"
                    ]
                },
                "hi-ether": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "hi-potion": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables"
                    ]
                },
                "historical documents": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest locked", "quest items"
                    ]
                },
                "hope ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: radiant"
                    ]
                },
                "ice adept": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "ice orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: ice", "set: ice"
                    ]
                },
                "ichor": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "icicle ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "element: ice", "set: ice"
                    ]
                },
                "infernal flames": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: fire", "set: fire"
                    ]
                },
                "iron orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: blunt", "set: iron"
                    ]
                },
                "jerky": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables"
                    ]
                },
                "jewelry box": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "flags: jewelry box start"
                    ]
                },
                "justice": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "kain": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: rare"
                    ]
                },
                "keycard a": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "keycards"
                    ]
                },
                "keycard b": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "keycards"
                    ]
                },
                "keycard c": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "keycards"
                    ]
                },
                "keycard d": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "keycards"
                    ]
                },
                "keycard v": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "keycards"
                    ]
                },
                "kobo": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "familiars"
                    ]
                },
                "lab coat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "lab glasses": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "lachiem archer": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "lachiem engineer": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "lachiem giantess": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "lachiem knight": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "lachiemi sun": {
                    "enabled": False,
                    "path": "icons\\",
                    "tags": [
                        "consumables"
                    ]
                },
                "leather helmet": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats", "quest items", "quest locked"
                    ]
                },
                "leather jerkin": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors", "enemy drops"
                    ]
                },
                "librarian hat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "librarian robe": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "lightwall": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: light", "set: radiant", "progression", "progression: vertical"
                    ]
                },
                "maw": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "merchant crow": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "familiars", "danger: vanilla"
                    ]
                },
                "metal wristband": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets"
                    ]
                },
                "meteor sparrow": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "meyef": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "familiars", "flags: meyef start"
                    ]
                },
                "midnight cloak": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "military armor": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors", "enemy drops"
                    ]
                },
                "mind refresh ultra": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables"
                    ]
                },
                "mind refresh": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "shop items"
                    ]
                },
                "mobile blossom": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "mother of pearl": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops", "enemy drops: rare"
                    ]
                },
                "mushroom tower": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "mushroom": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "quest items"
                    ]
                },
                "nether orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: blunt", "element: dark", "set: nether"
                    ]
                },
                "nethershade": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: rare"
                    ]
                },
                "nightmare": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "nuvius": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "nymph hairband": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops"
                    ]
                },
                "oculus ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: eye"
                    ]
                },
                "old coat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "orange juice": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "ornagy rut": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: rare", "vanilla only"
                    ]
                },
                "pendulum": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets"
                    ]
                },
                "plantbat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "plasma core": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items", "enemy drops"
                    ]
                },
                "plasma crystal": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items"
                    ]
                },
                "plasma geyser": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: plasma", "set: plasma"
                    ]
                },
                "plasma iv bag": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items"
                    ]
                },
                "plasma orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: plasma", "set: plasma"
                    ]
                },
                "plasma pod": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "plump maggot": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest items", "enemy drops"
                    ]
                },
                "pointy hat": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "poison moth": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "potion": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "shop items"
                    ]
                },
                "princess dress": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "pyro ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "element: fire", "set: fire"
                    ]
                },
                "radiant orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: light", "set: radiant"
                    ]
                },
                "rotten tail": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "royal advisor": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "royal casserole": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest locked", "shop items"
                    ]
                },
                "royal demon": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "royal guard": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "royal ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: plasma"
                    ]
                },
                "ryshia": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: rare"
                    ]
                },
                "sand bottle": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "sand up": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "stat upgrades"
                    ]
                },
                "sand vial": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops"
                    ]
                },
                "sanguine ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: blood"
                    ]
                },
                "sauteed wyvern tail": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest locked", "shop items"
                    ]
                },
                "savage cheveur": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "scythe ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "element: sharp"
                    ]
                },
                "security guard": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "security vest": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors", "enemy drops"
                    ]
                },
                "security visor": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats", "enemy drops"
                    ]
                },
                "selen's bangle": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets"
                    ]
                },
                "security turret": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "shadow seal": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: nether"
                    ]
                },
                "shattered orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: blunt", "set: shattered"
                    ]
                },
                "shield ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: iron"
                    ]
                },
                "shiny rock": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "shop items", "equipment", "equipment: trinkets"
                    ]
                },
                "silence ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: shattered"
                    ]
                },
                "silver ore": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items"
                    ]
                },
                "siren ink": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "quest items", "enemy drops"
                    ]
                },
                "siren": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "soul scanner": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics"
                    ]
                },
                "spaghetti": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest locked"
                    ]
                },
                "sporevine": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "sprite": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "familiars"
                    ]
                },
                "star of lachiem": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: empire"
                    ]
                },
                "starship engineer": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "storm eye": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "spells", "element: sharp", "set: wind"
                    ]
                },
                "succubus hairpin": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "progression: vertical"
                    ]
                },
                "sun ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: forbidden"
                    ]
                },
                "sunglasses": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "shop items", "equipment", "equipment: hats"
                    ]
                },
                "synthetic plume": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: trinkets", "enemy drops"
                    ]
                },
                "tablet": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics"
                    ]
                },
                "tailwind ring": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "passives", "set: wind"
                    ]
                },
                "talaria attachment": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression", "flags: fast start"
                    ]
                },
                "tenebrous moth": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "timespinner gear 1": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "timespinner pieces", "progression"
                    ]
                },
                "timespinner gear 2": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "timespinner pieces", "progression"
                    ]
                },
                "timespinner gear 3": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "timespinner pieces", "progression"
                    ]
                },
                "timespinner spindle": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "timespinner pieces", "progression"
                    ]
                },
                "timespinner wheel": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "timespinner pieces", "progression", "progression: vertical"
                    ]
                },
                "traveller's cloak": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: body armors"
                    ]
                },
                "trendy jacket": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "shop items", "equipment", "equipment: body armors"
                    ]
                },
                "twin pyramids": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression"
                    ]
                },
                "umbra orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: dark", "set: umbra", "kickstarter exclusive"
                    ]
                },
                "unagi roll": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "quest locked", "shop items"
                    ]
                },
                "viletian crown": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "equipment", "equipment: hats"
                    ]
                },
                "vol terrillis": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "warp shard": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "shop items"
                    ]
                },
                "water mask": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "progression"
                    ]
                },
                "wind orb": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "orbs", "element: sharp", "set: wind"
                    ]
                },
                "worm blossom": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "wyrm brooch": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "relics", "relics: cosmetics", "kickstarter exclusive"
                    ]
                },
                "wyvern tail": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "consumables", "enemy drops", "quest items"
                    ]
                },
                "xarion": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: bosses"
                    ]
                },
                "zeal": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: normal"
                    ]
                },
                "zel": {
                    "enabled": True,
                    "path": "icons\\",
                    "tags": [
                        "enemies", "enemies: rare", "vanilla only"
                    ]
                }
            }
            self.tags = {}

            # Auto-populate tags based on the above json data
            for key in self.tile_data.keys():
                for tag in self.tile_data[key]['tags']:
                    if tag not in self.tags.keys():
                        self.tags[tag] = {}
                    try:
                        self.tags[tag]['icons'].append(key)
                    except KeyError:
                        self.tags[tag]['icons'] = []
                        self.tags[tag]['icons'].append(key)
                    if tag not in ['vanilla only']:
                        self.tags[tag]['enabled'] = True
                    else:
                        self.tags[tag]['enabled'] = False

            self.use_compact_mode = {"friendlyName": "Use Compact Mode", "settingtype": "generation", "value": False}
            self.allow_duplicates = {"friendlyName": "Allow Duplicates", "settingtype": "generation", "value": False}
            self.rows = {"friendlyName": "Number of Rows", "settingtype": "generation", "value": 5}
            self.columns = {"friendlyName": "Number of Columns", "settingtype": "generation", "value": 5}
            self.seed = int(time() * 1000)

            # Save the settings to file
            self.save_settings()

    # Reload settings from file
    def reload_settings(self):
        with codecs.open(CONFIG_PATH, encoding="utf-8-sig", mode="r") as f:
            self.__dict__ = json.load(f, encoding="utf-8", indent=4)
        return

    # Save settings to file
    def save_settings(self):
        try:
            with codecs.open(CONFIG_PATH, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, indent=4)
        except Exception as e:
            print("Error saving file: " + str(e))
        return

    # Getter
    def get_tile_data(self):
        return self.tile_data

    def get_tag_data(self):
        return self.tags

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
