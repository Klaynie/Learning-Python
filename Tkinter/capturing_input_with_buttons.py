from tkinter import *
from tkinter import ttk
import os
from enum import IntEnum


class Button(IntEnum):
    CLICK_ME = 0


class Message(IntEnum):
    CLICKED = 0


button_texts = [
    'Click Me'
]

messages = [
    'Clicked!'
]


class App:

    def __init__(self, master):

        self.button = ttk.Button(
            master, text=button_texts[Button.CLICK_ME], command=self.callback)
        self.button.pack()
        self.button.state(['disabled'])
        print(self.button.instate(['disabled']))
        self.button.state(['!disabled'])

        # Set image path
        self.f_path = os.path.dirname(__file__)
        self.f_name = 'python_logo.gif'
        self.image_filepath = os.path.join(self.f_path, self.f_name)

        # Bind label to image and display it
        self.logo = PhotoImage(file=self.image_filepath)
        self.logo = self.logo.subsample(5, 5)
        self.logo.img = self.logo
        self.button.config(image=self.logo.img)
        self.button.config(compound='left')

    def callback(self):
        print(messages[Message.CLICKED])


def main():

    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
