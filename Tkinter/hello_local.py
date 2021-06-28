
from tkinter import *
from tkinter import ttk
from enum import IntEnum


class ButtonName(IntEnum):
    RESET = 0
    TEXAS = 1
    HAWAII = 2


class Greeting(IntEnum):
    DEFAULT = 0
    TEXAS = 1
    HAWAII = 2


button_names = [
    'Reset',
    'Texas',
    'Hawaii'
]

greetings = [
    "Hello, Tkinter!",
    'Howdy, Tkinter!',
    'Aloha, Tkinter'
]


class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text=greetings[Greeting.DEFAULT])
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text=button_names[ButtonName.TEXAS], command=self.texas_hello).grid(
            row=1, column=0)
        ttk.Button(master, text=button_names[ButtonName.HAWAII], command=self.hawaii_hello).grid(
            row=1, column=1)
        ttk.Button(master, text=button_names[ButtonName.RESET], command=self.reset).grid(
            row=2, column=0, columnspan=2)

    def texas_hello(self):
        self.label.config(text=greetings[Greeting.TEXAS])

    def hawaii_hello(self):
        self.label.config(text=greetings[Greeting.HAWAII])

    def reset(self):
        self.label.config(text=greetings[Greeting.DEFAULT])


def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
