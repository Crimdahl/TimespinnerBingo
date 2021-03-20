import tkinter
import os
import random
import sys
import BingoBoard

#WINDOW = None

#ROWS = 5
#COLUMNS = 5
#ICONDIR = os.path.join(os.path.dirname(__file__), "Icons")
#ICONSET = {}
#CONSUMABLE_SET = set()
#QUEST_SET = set()
#RELIC_SET = set()
#ORB_SET = set()
#PASSIVE_SET = set()
#SPELL_SET = set()
#ARMOR_SET = set()
#HEADGEAR_SET = set()
#TRINKET_SET = set()
#KEYCARD_SET = set()

def buttonClick(self):
    if self["bg"] == "white":
        self["bg"] = "green"
    elif self["bg"] == "green":
        self["bg"] = "white"

if __name__ == "__main__":
    #WINDOW = tkinter.Tk()
    #WINDOW.title("Timespinner Bingo")

    #for filename in os.listdir(ICONDIR):
    #    if filename.endswith(".png"):
    #        ICONSET[filename[:filename.index(".")]] = tkinter.PhotoImage(file = os.path.join(ICONDIR, filename), name = "Hello").zoom(2)

    #for c in range(COLUMNS):
    #    for r in range(ROWS):
    #        frame = tkinter.Frame(
    #            master = WINDOW

    #        )
    #        frame.grid(row=r, column=c, padx=2, pady=2)
    #        randomkey = random.choice(list(ICONSET.keys()))
    #        icon = ICONSET.pop(randomkey)
    #        button = tkinter.Button(
    #            master = frame,
    #            text = randomkey,
    #            image = icon,
    #            width = icon.width() * 4,
    #            height = icon.height() * 2,
    #            compound = tkinter.BOTTOM,
    #            bg = "white"
    #        )
    #        button.config(command = lambda arg=button:buttonClick(arg))
    #        button.image = icon
    #        button.pack()

    #WINDOW.mainloop()
    window = BingoBoard.BingoBoard()
    window.root.mainloop()