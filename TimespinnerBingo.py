import string
import tkinter
import BingoBoard
import Config
from time import time
from tkinter import ttk
from copy import deepcopy


class TimespinnerBingo(tkinter.Frame):
    def __init__(self, master):
        self.config = Config.Config()
        self.master = master
        self.cbRows = None
        self.cbColumns = None
        self.lblAvailableIcons = None
        self.lblRequiredIcons = None
        self.availableIcons = 0
        self.requiredIcons = 0
        self.tfSeed = None
        self.btnGenerate = None
        self.variables = {}
        self.candidates = {}

        #
        # COLUMN 0-1 - icon settings
        #
        # Label at the top of Column 1
        icon_label = tkinter.Label(master=self.master, text="Icons")
        icon_label.grid(row=5, column=0, sticky="s")

        icon_separator = ttk.Separator(master=self.master, orient="horizontal")
        icon_separator.grid(row=6, column=0, columnspan=100, sticky="ew")

        # To make a scrollable area containing the checkboxes is pretty complicated.
        #   We need a Canvas, a Scrollbar, a Frame, checkboxes, and Master.
        #   The checkboxes are inserted into the frame. The frame is inserted into the Canvas.
        #   The Canvas and Scrollbar are inserted into Master.
        icon_canvas = tkinter.Canvas(master=self.master)
        icon_canvas_scrollbar = tkinter.Scrollbar(
            master=self.master,
            orient='vertical',
            command=icon_canvas.yview
        )
        icon_container = tkinter.Frame(master=icon_canvas)

        # Method that scrolls the list of icons with the mousewheel
        def icon_canvas_scroll(event):
            icon_canvas.yview_scroll(-1 * int(event.delta / 120), 'units')

        # Bind the canvas and frame to scroll the canvas whenever the mouse is over them and
        #   the user scrolls the mouse wheel
        icon_canvas.bind('<MouseWheel>', icon_canvas_scroll)
        icon_container.bind('<MouseWheel>', icon_canvas_scroll)

        # Iterates through item-related settings, providing checkboxes
        objective_index = 2
        for key in self.config.get_tile_data().keys():
            var = tkinter.IntVar()
            widget = tkinter.Checkbutton(
                master=icon_container,
                text=string.capwords(key),
                variable=var
            )
            # Have the checkbox start checked if the item is enabled in config
            if self.config.get_tile_data()[key]['enabled']:
               widget.select()
            # Add the checkbox to the variable list so the checkbox state can be identified later
            self.variables[widget["text"]] = var
            # icon_changed is the changelistener that runs when the checkbox is checked
            widget.config(command=lambda arg=widget: self.icon_changed(arg))
            # We want to bind the mousewheel to scroll the canvas holding the checkbox
            #   If this is not done, the canvas will not scroll if the mouse is over a checkbox
            widget.bind('<MouseWheel>', icon_canvas_scroll)
            # Anchoring justifies the checkboxes against the left side
            widget.pack(anchor="w")
            objective_index += 1

        # The Canvas create_window command is required for the scrollbar to work properly
        icon_canvas.create_window(0, 0, anchor='nw', window=icon_container, width=175)
        # The Canvas update_idletasks waits until the checkboxes are added before configuring the scrollbar
        #   If this is not done, the scrollbar does not work properly because the Canvas is not full yet?
        icon_canvas.update_idletasks()
        icon_canvas.configure(
            scrollregion=icon_canvas.bbox('all'),
            yscrollcommand=icon_canvas_scrollbar.set,
            width=175
        )

        # Configures the row containing the scrollable canvases to fill the rest of the window vertically
        master.grid_rowconfigure(7, weight=1)
        icon_canvas_scrollbar.grid(row=7, column=1, sticky='nse')
        icon_canvas.grid(row=7, column=0, padx=(5, 0), sticky='ns')

        #
        # COLUMN 2 - Separator
        #
        col_separator1 = ttk.Separator(master=self.master, orient="vertical")
        col_separator1.grid(row=5, column=2, padx=(5, 5), rowspan=3, sticky="ns")

        #
        # COLUMN 3-4 - tag settings
        #
        tag_label = tkinter.Label(master=self.master, text="Tags")
        tag_label.grid(row=5, column=3, sticky="s")

        tag_separator = ttk.Separator(
            master=self.master,
            orient="horizontal"
        )
        tag_separator.grid(row=6, column=3, columnspan=100, sticky="ew")

        # To make a scrollable area containing the checkboxes is pretty complicated.
        #   We need a Canvas, a Scrollbar, a Frame, checkboxes, and Master.
        #   The checkboxes are inserted into the frame. The frame is inserted into the Canvas.
        #   The Canvas and Scrollbar are inserted into Master.
        tag_canvas = tkinter.Canvas(master=self.master)
        tag_canvas_scrollbar = tkinter.Scrollbar(
            master=self.master,
            orient='vertical',
            command=tag_canvas.yview
        )
        tag_container = tkinter.Frame(master=tag_canvas)

        # Method that scrolls the list of icons with the mousewheel
        def tag_canvas_scroll(event):
            tag_canvas.yview_scroll(-1 * int(event.delta / 120), 'units')

        # Bind the canvas and frame to scroll the canvas whenever the mouse is over them and
        #   the user scrolls the mouse wheel
        tag_canvas.bind('<MouseWheel>', tag_canvas_scroll)
        tag_container.bind('<MouseWheel>', tag_canvas_scroll)

        # Iterates through item-related settings, providing checkboxes
        objective_index = 2
        for key in sorted(self.config.get_tag_data().keys()):
            var = tkinter.IntVar()
            widget = tkinter.Checkbutton(
                master=tag_container,
                text=string.capwords(key),
                variable=var
            )
            # Have the checkbox start checked if the item is enabled in config
            if self.config.get_tag_data()[key] == 'enabled':
                widget.select()
            # Add the checkbox to the variable list so the checkbox state can be identified later
            self.variables[widget["text"]] = var
            # icon_changed is the changelistener that runs when the checkbox is checked
            widget.config(command=lambda arg=widget: self.tag_changed(arg))
            # We want to bind the mousewheel to scroll the canvas holding the checkbox
            #   If this is not done, the canvas will not scroll if the mouse is over a checkbox
            widget.bind('<MouseWheel>', tag_canvas_scroll)
            # Anchoring justifies the checkboxes against the left side
            widget.pack(anchor="w")
            objective_index += 1

        # The Canvas create_window command is required for the scrollbar to work properly
        tag_canvas.create_window(0, 0, anchor='nw', window=tag_container, width=175)
        # The Canvas update_idletasks waits until the checkboxes are added before configuring the scrollbar
        #   If this is not done, the scrollbar does not work properly because the Canvas is not full yet?
        tag_canvas.update_idletasks()
        tag_canvas.configure(
            scrollregion=tag_canvas.bbox('all'),
            yscrollcommand=tag_canvas_scrollbar.set,
            width=175
        )

        tag_canvas_scrollbar.grid(row=7, column=4, sticky='nse')
        tag_canvas.grid(row=7, column=3, padx=(5, 0), sticky='ns')

        #
        # Column 5
        #
        config_separator = ttk.Separator(
            master=self.master,
            orient="vertical"
        )
        config_separator.grid(row=5, column=5, rowspan=3, padx=(5, 5), sticky="ns")

        #
        # Column 6 & 7 - generation settings
        #
        layout_label = tkinter.Label(
            master=self.master,
            text="Generation Settings"
        )
        layout_label.grid(row=5, column=6, sticky="s")

        # Since the entirety of the area below the header is a single row in master, we need to
        #   wrap everything in a frame to effectively split it into sub-rows
        layout_frame = tkinter.Frame(
            master=self.master
        )
        layout_frame.grid(row=7, column=6, pady=(5, 0), sticky='news')

        layout_rows_label = tkinter.Label(
            master=layout_frame,
            text="Bingo Rows: "
        )
        layout_rows_label.grid(row=0, column=1, padx=(5, 5), pady=(5, 0), sticky="w")

        self.cbRows = ttk.Combobox(
            master=layout_frame,
            text="Rows: " + str(self.availableIcons),
            width=5,
            values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"),
            state='readonly'
        )
        self.cbRows.current(int(self.config.rows["value"]) - 1)
        self.cbRows.bind("<<ComboboxSelected>>", lambda x: self.rows_changed())
        self.cbRows.grid(row=0, column=2, padx=(0, 10), pady=(5, 0), sticky="ew")

        layout_columns_label = tkinter.Label(
            master=layout_frame,
            text="Bingo Columns: "
        )
        layout_columns_label.grid(row=1, column=1, padx=(5, 0), pady=(5, 0), sticky="w")

        self.cbColumns = ttk.Combobox(
            master=layout_frame,
            text="Columns: " + str(self.availableIcons),
            width=5,
            values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"),
            state='readonly'
        )
        self.cbColumns.current(int(self.config.columns["value"]) - 1)
        self.cbColumns.bind("<<ComboboxSelected>>", lambda x: self.columns_changed())
        self.cbColumns.grid(row=1, column=2, padx=(0, 10), pady=(5, 0), sticky="ew")

        var = tkinter.BooleanVar()
        compact_mode_checkbox = tkinter.Checkbutton(
            master=layout_frame,
            text=self.config.use_compact_mode["friendlyName"],
            variable=var
        )
        if self.config.use_compact_mode["value"]: compact_mode_checkbox.select()
        compact_mode_checkbox.config(command=lambda arg=compact_mode_checkbox: self.checkbox_changed(arg))
        self.variables[compact_mode_checkbox["text"]] = var
        compact_mode_checkbox.grid(row=2, column=1, padx=(5, 0), pady=(5, 0), columnspan=2, sticky="w")

        var = tkinter.BooleanVar()
        allow_duplicates_checkbox = tkinter.Checkbutton(
            master=layout_frame,
            text=self.config.allow_duplicates["friendlyName"],
            variable=var
        )
        if self.config.allow_duplicates["value"]: allow_duplicates_checkbox.select()
        allow_duplicates_checkbox.config(command=lambda arg=allow_duplicates_checkbox: self.checkbox_changed(arg))
        self.variables[allow_duplicates_checkbox["text"]] = var
        allow_duplicates_checkbox.grid(row=3, column=1, padx=(5, 0), pady=(0, 0), columnspan=2, sticky="w")

        available_icons_label = tkinter.Label(
            master=layout_frame,
            text="Available Items :"
        )
        available_icons_label.grid(row=4, column=1, padx=(5, 0), pady=(5, 0), sticky="w")

        self.lblAvailableIcons = tkinter.Label(
            master=layout_frame,
            text=str(self.availableIcons)
        )
        self.lblAvailableIcons.grid(row=4, column=2, pady=(5, 0),  sticky="w")

        required_items_label = tkinter.Label(
            master=layout_frame,
            text="Required Items :"
        )
        required_items_label.grid(row=5, column=1, padx=(5, 0), pady=(5, 0), sticky="w")

        self.lblRequiredIcons = tkinter.Label(
            master=layout_frame,
            text=str(self.requiredIcons)
        )
        self.lblRequiredIcons.grid(row=5, column=2, padx=(0, 5), pady=(5, 0), sticky="w")

        seed_label = tkinter.Label(
            master=layout_frame,
            text="Seed:"
        )
        seed_label.grid(row=7, column=1, padx=(5, 0), pady=(50, 0), sticky="w")

        self.tfSeed = tkinter.Text(
            master=layout_frame,
            height=1,
            width=15
        )
        self.tfSeed.grid(row=7, column=1, columnspan=2, padx=(40, 10), pady=(50, 0), sticky='ew')

        self.btnGenerate = tkinter.Button(
            master=layout_frame,
            compound=tkinter.BOTTOM,
            text="Generate!",
            command=self.generate_bingo_board
        )
        self.btnGenerate.grid(row=8, column=1, columnspan=2, padx=(10, 10), pady=(5, 20), sticky="ew")

        self.calculateAvailableIcons()
        if self.availableIcons > 0 and self.config.allow_duplicates["value"]:
            self.lblAvailableIcons["text"] = "Infinite"
        self.calculate_required_icons()
        self.validate_required_icons()

    def calculateAvailableIcons(self):
        self.availableIcons = 0
        self.candidates = {}
        tile_data = self.config.get_tile_data()
        tag_data = self.config.get_tag_data()
        for key in tile_data.keys():
            tile_enabled_by_tags = True
            if not tile_data[key]['enabled']:
                # Not enabled - do not check tags, do not pass go
                continue

            for tag_key in tile_data[key]['tags']:
                if tag_data[tag_key] == 'disabled':
                    tile_enabled_by_tags = False

            if tile_enabled_by_tags:
                self.availableIcons += 1
                self.candidates[key] = tile_data[key]
        self.lblAvailableIcons["text"] = text = str(self.availableIcons)

    def calculate_required_icons(self):
        self.requiredIcons = int(self.cbRows.get()) * int(self.cbColumns.get())
        self.lblRequiredIcons["text"] = text = str(self.requiredIcons)

    def icon_changed(self, arg):
        icon_name = str.lower(arg["text"])
        state = self.variables[arg["text"]].get()
        for key in self.config.get_tile_data().keys():
            if key == icon_name:
                if state == 0:
                    self.config.get_tile_data()[key]['enabled'] = False
                else:
                    self.config.get_tile_data()[key]['enabled'] = True
        self.calculateAvailableIcons()
        self.validate_required_icons()
        self.config.save_settings()

    def tag_changed(self, arg):
        tag_name = str.lower(arg['text'])
        state = self.variables[arg['text']].get()
        for key in self.config.get_tag_data().keys():
            if key == tag_name:
                if state == 0:
                    self.config.get_tag_data()[key] = 'disabled'
                else:
                    self.config.get_tag_data()[key] = 'enabled'
        self.calculateAvailableIcons()
        self.validate_required_icons()
        self.config.save_settings()

    def checkbox_changed(self, arg):
        variable = str.lower(arg['text'])
        state = self.variables[arg["text"]].get()
        print(variable)
        if variable == "use compact mode":
            if state == 0:
                self.config.set_use_compact_mode(False)
            else:
                self.config.set_use_compact_mode(True)
        elif variable == "allow duplicates":
            if state == 0:
                self.config.set_allow_duplicates(False)
            else:
                self.config.set_allow_duplicates(True)
        self.config.save_settings()
        self.calculateAvailableIcons()
        if self.availableIcons > 0 and self.config.allow_duplicates["value"]:
            self.lblAvailableIcons["text"] = "Infinite"
        self.validate_required_icons()
        return

    def rows_changed(self):
        self.config.set_rows(int(self.cbRows.get()))
        self.config.save_settings()
        self.calculate_required_icons()
        self.validate_required_icons()

    def columns_changed(self):
        self.config.set_columns(int(self.cbColumns.get()))
        self.config.save_settings()
        self.calculate_required_icons()
        self.validate_required_icons()

    def validate_required_icons(self):
        if not self.config.allow_duplicates["value"]:
            if self.availableIcons - self.requiredIcons < 0:
                self.btnGenerate["state"] = tkinter.DISABLED
                self.lblAvailableIcons["fg"] = "Red"
            else:
                self.btnGenerate["state"] = tkinter.NORMAL
                self.lblAvailableIcons["fg"] = "Black"
        elif self.availableIcons == 0:
            self.btnGenerate["state"] = tkinter.DISABLED
            self.lblAvailableIcons["fg"] = "Red"
        else:
            self.btnGenerate["state"] = tkinter.NORMAL
            self.lblAvailableIcons["fg"] = "Black"
        return

    def generate_bingo_board(self):
        if self.tfSeed.get("1.0", "end-1c") != "":
            try:
                seed = int(self.tfSeed.get("1.0", "end"))
                self.config.set_seed(seed)
            except ValueError:
                tkinter.messagebox.showerror(title="Seed Error", message="Error: The seed must be an integer.")
                return
        else:
            self.config.set_seed(int(time() * 1000))
        new_window = tkinter.Toplevel(root)
        new_window.title("Timespinner Bingo")
        BingoBoard.BingoBoard(new_window, self.config, deepcopy(self.candidates))
        return


if __name__ == "__main__":
    root = tkinter.Tk()
    #root.geometry("800x400")
    settingsUI = TimespinnerBingo(root)
    root.title("Bingo Settings")
    root.mainloop()
