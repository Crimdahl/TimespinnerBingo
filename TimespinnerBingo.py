import tkinter
import os

WINDOW = None
ROWS = 5
COLUMNS = 5
ICONDIR = os.path.join(os.path.dirname(__file__), "Icons")
CONSUMABLE_SET = set()
QUEST_SET = set()
RELIC_SET = set()
ORB_SET = set()
PASSIVE_SET = set()
SPELL_SET = set()
ARMOR_SET = set()
HEADGEAR_SET = set()
TRINKET_SET = set()
KEYCARD_SET = set()

if __name__ == "__main__":
    WINDOW = tkinter.Tk()



    for col in range(COLUMNS):
        for row in range(ROWS):
            
            CONSUMABLE_SET.add(os.path.join(ICONDIR, "Antidote.png"))
            frame = tkinter.Frame(
                master = WINDOW

            )
            frame.grid(row=row, column=col, padx=2, pady=2)
            icon = tkinter.PhotoImage(file = CONSUMABLE_SET.pop()).zoom(2)
            button = tkinter.Button(
                master = frame,
                image = icon,
                width = icon.width() * 2,
                height = icon.height() * 2
            )
            
            button.pack()

    WINDOW.mainloop()