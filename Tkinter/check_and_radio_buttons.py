from tkinter import *
from tkinter import ttk
import os
from enum import IntEnum


class Button(IntEnum):
    CHECKBUTTON = 0
    LOG_SETTINGS = 1
    RADIO_SPAM = 2
    RADIO_EGGS = 3
    RADIO_SAUSAGE = 4


class Settings(IntEnum):
    SPAM_ON = 0
    SPAM_OFF = 1


class RadioValue(IntEnum):
    SPAM = 0
    EGGS = 1
    SAUSAGE = 2


button_texts = [
    'SPAM?',
    'Log Settings',
    'SPAM',
    'Eggs',
    'Sausage'
]

settings = [
    'SPAM Please!',
    'Boo SPAM'
]

radio_values = [
    'SPAM',
    'Eggs',
    'Sausage'
]


class App:

    def __init__(self, master):
        self.spam_setting = StringVar()
        self.spam_setting.set(settings[Settings.SPAM_OFF])
        self.breakfast = StringVar()
        self.breakfast.set(radio_values[RadioValue.SAUSAGE])

        self.checkbutton = ttk.Checkbutton(
            master, text=button_texts[Button.CHECKBUTTON])
        self.checkbutton.config(
            variable=self.spam_setting, onvalue=settings[Settings.SPAM_ON], offvalue=settings[Settings.SPAM_OFF])
        self.checkbutton.pack()

        self.radiobutton_1 = ttk.Radiobutton(
            master, text=button_texts[Button.RADIO_SPAM], variable=self.breakfast, value=radio_values[RadioValue.SPAM])
        self.radiobutton_1.pack()

        self.radiobutton_2 = ttk.Radiobutton(
            master, text=button_texts[Button.RADIO_EGGS], variable=self.breakfast, value=radio_values[RadioValue.EGGS])
        self.radiobutton_2.pack()

        self.radiobutton_3 = ttk.Radiobutton(
            master, text=button_texts[Button.RADIO_SAUSAGE], variable=self.breakfast, value=radio_values[RadioValue.SAUSAGE])
        self.radiobutton_3.pack()

        self.radiobutton_4 = ttk.Radiobutton(
            master, text=button_texts[Button.RADIO_SPAM], variable=self.breakfast, value=radio_values[RadioValue.SPAM])
        self.radiobutton_4.pack()

        self.checkbutton.config(textvariable=self.breakfast)

        self.button = ttk.Button(
            master, text=button_texts[Button.LOG_SETTINGS], command=self.print_settings)
        self.button.pack()

    def print_settings(self):
        print(self.spam_setting.get())
        print(self.breakfast.get())


def main():

    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
