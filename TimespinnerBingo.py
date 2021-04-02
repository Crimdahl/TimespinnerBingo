import tkinter
import BingoBoard
import Settings
from tkinter import ttk

class TimespinnerBingo(tkinter.Frame):
    def __init__(self, master):
        self.settings = Settings.Settings()
        self.master = master
        self.cbRows = None
        self.cbColumns = None
        self.lblAvailableIcons = None
        self.lblRequiredIcons = None
        self.availableIcons = 0
        self.requiredIcons = 0
        self.tfSeed = None
        self.seed = 0
        self.btnGenerate = None
        self.variables={}

        #
        # COLUMN 0
        #
        #Label at the top of Column 1
        widget = tkinter.Label(master=self.master,
            text="Generation Settings")
        widget.grid(row=0, column=0, pady=(10,0), sticky="s")
        
        widget = ttk.Separator(
            master=self.master,
            orient="horizontal"
            )
        widget.grid(row=1, column=0, columnspan=100, sticky="ew")

        var = tkinter.BooleanVar()
        widget = tkinter.Checkbutton(
            master=self.master,
            text=self.settings.allowDuplicates["friendlyName"],
            variable = var
            )
        if self.settings.allowDuplicates["value"]: widget.select()
        widget.config(command = lambda arg=widget:self.checkboxChanged(arg))
        self.variables[widget["text"]] = var
        widget.grid(row=2, column=0, padx=(10, 0), columnspan=2, sticky="w")
        
        #Iterates through item-related settings, providing checkboxes
        objective_index = 3
        for k, v in self.settings.__dict__.items():
            if type(v) is dict:
                if v["settingtype"] == "item":
                    var = tkinter.IntVar()
                    widget = tkinter.Checkbutton(
                        master=self.master,
                        text=v["friendlyName"],
                        variable=var
                        )
                    if v["value"]: widget.select()
                    self.variables[widget["text"]] = var
                    widget.config(command = lambda arg=widget:self.checkboxChanged(arg))
                    widget.grid(row=objective_index, column=0, padx=(10, 10), sticky="w")
                    objective_index += 1
        
        #
        # Column 1 - Separator
        #
        widget = ttk.Separator(
            master=self.master,
            orient="vertical"
            )
        widget.grid(row=0, column=1, rowspan=100, sticky="ns")
        
        #
        # Column 2
        #
        widget = tkinter.Label(
            master=self.master,
            text="Flag-related Settings"
            )
        widget.grid(row=0, column=2, columnspan=2, pady=(10,0), sticky="s")

        #Iterates through item-related settings, providing checkboxes
        flag_index = 2
        for k, v in self.settings.__dict__.items():
            if type(v) is dict:
                if v["settingtype"] == "flag":
                    var = tkinter.IntVar()
                    widget = tkinter.Checkbutton(
                        master=self.master,
                        text=v["friendlyName"],
                        variable=var
                        )
                    if v["value"]: widget.select()
                    self.variables[widget["text"]] = var
                    widget.config(command = lambda arg=widget:self.checkboxChanged(arg))
                    widget.grid(row=flag_index, column=2, columnspan=2, padx=(10, 10), sticky="w")
                    flag_index += 1

        #
        # Column 3 - Separator
        #
        #widget = ttk.Separator(
        #    master=self.master,
        #    orient="vertical"
        #    )
        #widget.grid(row=0, column=3, rowspan=100, sticky="ns")

        #
        # Column 3 & 4
        #
        widget = tkinter.Label(
            master=self.master,
            text="Layout Settings"
            )
        widget.grid(row=flag_index + 2, column=2, columnspan=2)

        widget = ttk.Separator(
            master=self.master,
            orient="horizontal"
            )
        widget.grid(row=flag_index + 2, column=2, columnspan=2, rowspan=2, sticky="ew")

        widget = tkinter.Label(
            master=self.master,
            text="Bingo Rows: "
            )
        widget.grid(row=flag_index + 3, column=2, padx=(10, 0), sticky="w")

        self.cbRows = ttk.Combobox(
            master=self.master,
            text="Rows: " + str(self.availableIcons),
            width=5,
            values = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15")
            )
        self.cbRows.current(int(self.settings.rows["value"]) - 1)
        self.cbRows.bind("<<ComboboxSelected>>", lambda x:self.rowsChanged())
        self.cbRows.grid(row=flag_index + 3, column=3, padx=(0, 10), sticky="ew")

        widget = tkinter.Label(
            master=self.master,
            text="Bingo Columns: "
            )
        widget.grid(row=flag_index + 4, column=2, padx=(10, 0), sticky="w")

        self.cbColumns = ttk.Combobox(
            master=self.master,
            text="Columns: " + str(self.availableIcons),
            width=5,
            values = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15")
            )
        self.cbColumns.current(int(self.settings.columns["value"]) - 1)
        self.cbColumns.bind("<<ComboboxSelected>>", lambda x:self.columnsChanged())
        self.cbColumns.grid(row=flag_index + 4, column=3, padx=(0, 10), sticky="ew")

        var = tkinter.BooleanVar()
        widget = tkinter.Checkbutton(
            master=self.master,
            text=self.settings.useCompactMode["friendlyName"],
            variable = var
            )
        if self.settings.useCompactMode["value"]: widget.select()
        widget.config(command = lambda arg=widget:self.checkboxChanged(arg))
        self.variables[widget["text"]] = var
        widget.grid(row=flag_index + 5, column=2, padx=(10, 0), columnspan=2, sticky="w")
        
        widget = tkinter.Label(
            master=self.master,
            text="Available Items :"
            )
        widget.grid(row=objective_index - 2, column=2, padx=(10, 0), sticky="e")

        self.lblAvailableIcons = tkinter.Label(
            master=self.master,
            text=str(self.availableIcons)
            )
        self.lblAvailableIcons.grid(row=objective_index - 2, column=3, padx=(0, 10), sticky="w")

        widget = tkinter.Label(
            master=self.master,
            text="Required Items :"
            )
        widget.grid(row=objective_index - 1, column=2, padx=(10, 0), sticky="e")

        self.lblRequiredIcons = tkinter.Label(
            master=self.master,
            text=str(self.requiredIcons)
            )
        self.lblRequiredIcons.grid(row=objective_index - 1, column=3, padx=(0, 10), sticky="w")

        self.btnGenerate = tkinter.Button(
                        master = self.master,
                        compound = tkinter.BOTTOM,
                        width=18,
                        text="Generate!",
                        command=self.generateBingoBoard
                    )
        self.btnGenerate.grid(row=objective_index, column=2, columnspan=2, pady=(0, 10), padx=(10, 10), sticky="ew")

        self.calculateAvailableIcons()
        if self.availableIcons > 0 and self.settings.allowDuplicates["value"]:
            self.lblAvailableIcons["text"] = "Infinite"
        self.calculateRequiredIcons() 
        self.validateRequiredIcons()
        
    def calculateAvailableIcons(self):
        self.availableIcons = 0
        items = set()
        for k, v in self.settings.__dict__.items():
            if type(v) is dict:
                if v["settingtype"] == "item" and v["value"]:
                    for item in v["items"]:
                        if self.settings.excludeMeyef["value"] and item == "Meyef": continue
                        if self.settings.excludeJewelryBox["value"] and item == "Jewelry Box": continue
                        if self.settings.excludeTalariaAttachment["value"] and item == "Talaria Attachment": continue
                        items.add(item)

        self.availableIcons += len(items)
        self.lblAvailableIcons["text"] = text=str(self.availableIcons)

    def calculateRequiredIcons(self):
        self.requiredIcons = int(self.cbRows.get()) * int(self.cbColumns.get())
        self.lblRequiredIcons["text"] = text=str(self.requiredIcons)

    def checkboxChanged(self, arg):
        variable = self.variables[arg["text"]].get()
        for v in self.settings.__dict__.values():
            if type(v) is dict:
                if v["friendlyName"] == arg["text"]:
                    if variable:
                        v["value"] = True
                    else:
                        v["value"] = False
        self.settings.Save()
        self.calculateAvailableIcons()
        if self.availableIcons > 0 and self.settings.allowDuplicates["value"]:
            self.lblAvailableIcons["text"] = "Infinite"
        self.validateRequiredIcons()
        return

    def rowsChanged(self):
        self.settings.setRows(int(self.cbRows.get()))
        self.settings.Save()
        self.calculateRequiredIcons()
        self.validateRequiredIcons()

    def columnsChanged(self):
        self.settings.setColumns(int(self.cbColumns.get()))
        self.settings.Save()
        self.calculateRequiredIcons()
        self.validateRequiredIcons()

    def validateRequiredIcons(self):
        if not self.settings.allowDuplicates["value"]:
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

    def generateBingoBoard(self):
        newWindow = tkinter.Toplevel(root)
        newWindow.title("Timespinner Bingo")
        BingoBoard.BingoBoard(newWindow, self.settings)
        return


if __name__ == "__main__":
    root = tkinter.Tk()
    settingsUI = TimespinnerBingo(root)
    root.title("Bingo Settings")
    root.mainloop()