from tkinter import *
from tkinter import ttk
from enum import IntEnum


class Buttons(IntEnum):
    PRINT = 0
    CLEAR = 1

class Prompts(IntEnum):
    NO_MONTH = 0
    MONTH_NOT_VALID = 1
    YEAR_NOT_VALID = 2

class Years(IntEnum):
    MIN_YEAR = 0
    MAX_YEAR = 1
    FALLBACK_YEAR = 2

button_texts = [
    'Print',
    'Clear'
]

prompts = [
    'Please select a month.',
    'Not a valid month.',
    'Please select a valid year.'
]

years = [
    1900,
    9999,
    0
]

combobox_values = (
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
)

class App:

    def __init__(self, parent):
        # Variables
        self.month = StringVar()
        self.year = StringVar()

        # Combobox for month selection
        self.combobox = ttk.Combobox(parent, textvariable=self.month)
        self.combobox.pack()
        self.combobox.config(values=combobox_values)

        # Spinbox for year selection
        self.spinbox = Spinbox(parent, from_ = years[Years.MIN_YEAR], to = years[Years.MAX_YEAR], textvariable=self.year)
        self.spinbox.pack()

        # Print button
        self.print_button = ttk.Button(parent, text=button_texts[Buttons.PRINT], command=self.print_entry)
        self.print_button.pack()
        
        # Clear button
        self.clear_button = ttk.Button(parent, text=button_texts[Buttons.CLEAR], command=self.clear_entry)
        self.clear_button.pack()
        

    def print_entry(self):
        selected_month, selected_year = self.get_entries()
        if selected_month in combobox_values:
            if years[Years.MIN_YEAR] <= selected_year <= years[Years.MAX_YEAR]:
                print(selected_month, selected_year)
            else:
                print(prompts[Prompts.YEAR_NOT_VALID])
        elif selected_month == '':
            print(prompts[Prompts.NO_MONTH])
        else:
            print(prompts[Prompts.MONTH_NOT_VALID])
    
    def get_entries(self):
        selected_month = self.month.get()
        selected_year = self.year.get()
        try:
            selected_year = int(selected_year)
        except ValueError:
            selected_year = years[Years.FALLBACK_YEAR]
        return selected_month, selected_year

    def clear_entry(self):
        self.month.set('')


def main():

    root = Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
