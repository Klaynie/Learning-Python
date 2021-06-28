from tkinter import *
from tkinter import ttk
import os


class HelloApp:

    def __init__(self, master):
        # Initial label
        label = ttk.Label(master, text="Hello, Tkinter!")
        label.pack()

        # Update label
        label.config(
            text="Howdy Tkinter! It's been a while since we last met. Great to see you again!")
        label.config(wraplength=200)
        label.config(justify=CENTER)
        label.config(foreground='blue', background='yellow')
        label.config(font=('Courier', 18, 'bold'))

        # Set image path
        f_path = os.path.dirname(__file__)
        f_name = 'python_logo.gif'
        image_filepath = os.path.join(f_path, f_name)

        # Bind label to image and display it
        logo = PhotoImage(file=image_filepath)
        label.img = logo
        label.config(image=label.img)
        label.config(compound='left')


def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
