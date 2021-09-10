import string
import tkinter
import os
import random
import re
from collections import defaultdict

HEX_GREEN = "#008000"
HEX_LIGHTGRAY = "#D3D3D3"
HEX_BLACK = "#000000"
HEX_GOLD = "#daa520"
HEX_ALT_GREEN = "#008100"


class BingoBoard(tkinter.Frame):
    icon_directory = os.path.join(os.path.dirname(__file__), "Icons")

    def __init__(self, master, config, candidates, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.buttons = defaultdict(list)
        self.button_events = []
        self.btn_toggle = None
        self.settings = config
        random.seed(config.get_seed())

        # Iterate over dictionaries in settings, making images out of the enabled lists of items.
        #   Images are inserted directly into the candidate dictionary for use later.
        for icon in candidates:
            image = None
            # Enforce file name case insensitivity by iterating through the icon directory
            #   comparing each filename to the icon's name in a case-insensitive manner
            for icon_file in os.listdir(self.icon_directory):
                if icon_file[:icon_file.rindex(".")].lower() == icon.lower():
                    image = tkinter.PhotoImage(file=os.path.join(self.icon_directory, icon_file))
            if not image:
                image = tkinter.PhotoImage(file=os.path.join(self.icon_directory, "none.png"))
            assert image.height() == image.width(), \
                "Supplied icons should be square in shape, 16x16, 32x32, 64x64, or 128x128."
            if image.height() == 16:
                candidates[icon]['image'] = image.zoom(2)
            elif image.height() == 32:
                candidates[icon]['image'] = image
            elif image.height() == 64:
                candidates[icon]['image'] = image.subsample(2)
            elif image.height() == 128:
                candidates[icon]['image'] = image.subsample(4)

        # Create and insert a search field, but only if there are at least 3 columns of space on the board.
        if self.settings.get_columns()["value"] > 3:
            search_label = tkinter.Label(
                master=self.master,
                text="Search"
            )
            if self.settings.get_use_compact_mode()["value"]:
                search_label.grid(row=0, column=0, columnspan=2, padx=(2, 2), sticky="w")
            else:
                search_label.grid(row=0, column=0, padx=(2, 2), sticky="e")

            search_box = CustomText(
                master=self.master,
                height=1,
                width=0
            )
            search_box.bind("<<TextModified>>", self.search_box_modified)
            search_box.grid(row=0, column=1, columnspan=self.settings.get_columns()["value"] - 2, sticky="ew")

            search_button = tkinter.Button(
                master=self.master,
                compound=tkinter.BOTTOM,
                text="Mark",
                command=self.toggle_buttons
            )
            search_button.grid(row=0,
                               column=self.settings.get_columns()["value"] - 1,
                               columnspan=2,
                               padx=(2, 2),
                               sticky="ew")

        # For each column and each row...
        for c in range(int(self.settings.get_columns()["value"])):
            for r in range(1, int(self.settings.get_rows()["value"]) + 1):
                # ...create a frame, select a random tile from the set of candidates
                #   and create a button out of it.
                frame = tkinter.Frame(
                    master=self.master
                )
                frame.grid(row=r, column=c, padx=2, pady=2)
                random_key = random.choice(list(candidates.keys()))
                image = candidates[random_key]['image']

                if not self.settings.get_allow_duplicates()["value"]:
                    # If duplicates are not allowed, remove the candidate so it isn't reused
                    candidates.pop(random_key)

                if self.settings.get_use_compact_mode()["value"]:
                    button = tkinter.Button(
                        master=frame,
                        image=image,
                        width=image.width(),
                        height=image.height(),
                        bg=HEX_LIGHTGRAY
                    )
                else:
                    button = tkinter.Button(
                        master=frame,
                        text=string.capwords(random_key).replace(" ", "\n", 1),
                        image=image,
                        width=image.width() * 2.5,
                        height=image.height() * 2,
                        compound=tkinter.BOTTOM,
                        bg=HEX_LIGHTGRAY
                    )

                self.buttons[random_key].append(button)
                self.button_events.append(ButtonEvents(button, random_key))
                button.image = image
                button.pack()

        seed_label = tkinter.Label(
            master=self.master,
            text="Seed:"
        )
        seed_label.grid(row=self.settings.get_rows()["value"] + 1, column=0, padx=(2, 2), sticky="w")

        seed_input = tkinter.Text(
            master=self.master,
            height=1,
            width=len(str(self.settings.get_seed()))
        )
        seed_input.insert(1.0, str(self.settings.get_seed()))
        seed_input.configure(state="disabled")
        seed_input.grid(row=self.settings.get_rows()["value"] + 1, column=0, columnspan=9999, padx=(40, 2), sticky="w")

    def search_box_modified(self, event=None):
        # This method searches through all buttons to find ones with items that contain
        #   the search value text.
        # If the button is unmarked, it colors the background gold
        search_value = event.widget.get(1.0, "end-1c")
        if search_value != "":
            for k, v in self.buttons.items():
                for button in v:
                    if button["bg"] == HEX_GREEN:
                        button["bg"] = HEX_ALT_GREEN
                    if button["bg"] != HEX_GREEN and button["bg"] != HEX_ALT_GREEN:
                        if button["bg"] != HEX_GREEN and re.search(search_value.lower(), k.lower()):
                            button["bg"] = HEX_GOLD
                        elif button["bg"] != HEX_GREEN:
                            button["bg"] = HEX_LIGHTGRAY
        else:
            for k, v in self.buttons.items():
                for button in v:
                    if button["bg"] == HEX_GOLD:
                        button["bg"] = HEX_LIGHTGRAY
                    elif button["bg"] == HEX_ALT_GREEN:
                        button["bg"] = HEX_GREEN

    def toggle_buttons(self):
        # For any buttons colored with a gold background after searching,
        for k, v in self.buttons.items():
            for button in v:
                if button["bg"] == HEX_GOLD:
                    button["bg"] = HEX_ALT_GREEN


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
        self.wait_time = 0
        self.wrap_length = 180
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

    # Changes button background color when the mouse hovers over the button
    def enter(self, event=None):
        self.schedule()
        if self.widget["bg"] == HEX_LIGHTGRAY:
            self.widget["bg"] = HEX_GREEN
        elif self.widget["bg"] == HEX_GREEN:
            self.widget["bg"] = HEX_LIGHTGRAY
        elif self.widget["bg"] == HEX_GOLD:
            self.widget["bg"] = HEX_ALT_GREEN
        elif self.widget["bg"] == HEX_ALT_GREEN:
            self.widget["bg"] = HEX_GOLD

    # Reverts button background color change when the mouse leaves the button
    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        if not self.clicked:
            if self.widget["bg"] == HEX_LIGHTGRAY:
                self.widget["bg"] = HEX_GREEN
            elif self.widget["bg"] == HEX_GREEN:
                self.widget["bg"] = HEX_LIGHTGRAY
            elif self.widget["bg"] == HEX_GOLD:
                self.widget["bg"] = HEX_ALT_GREEN
            elif self.widget["bg"] == HEX_ALT_GREEN:
                self.widget["bg"] = HEX_GOLD
        else:
            self.clicked = False

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx()
        if self.widget["text"] == "":
            y += self.widget.winfo_rooty() - (self.widget.winfo_height() / 2)
        else:
            y += self.widget.winfo_rooty() - (self.widget.winfo_height() / 4)
        # creates a top level window
        self.tw = tkinter.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(self.tw, text=string.capwords(self.text), justify='left',
                              background="#ffffff", relief='solid', borderwidth=1,
                              wraplength=self.wrap_length)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
