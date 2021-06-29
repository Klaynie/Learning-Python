from tkinter import *
from tkinter import ttk
from enum import IntEnum


class Button(IntEnum):
    PRINT = 0
    CLEAR = 1


button_texts = [
    'Print',
    'Clear'
]


class App:

    def __init__(self, parent):
        self.entry = ttk.Entry(parent, width=30)
        self.entry.pack()
        
        self.print_button = ttk.Button(parent, text=button_texts[Button.PRINT], command=self.print_entry)
        self.print_button.pack()
        
        self.clear_button = ttk.Button(parent, text=button_texts[Button.CLEAR], command=self.clear_entry)
        self.clear_button.pack()

    def print_entry(self):
        print(self.entry.get())
    
    def clear_entry(self):
        self.entry.delete(0, END)


def main():

    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
