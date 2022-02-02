from tkinter import *
from tkinter import ttk


class HelloApp:

    def __init__(self, master):

        self.frame = ttk.Frame(master)
        self.frame.pack()
        self.frame.config(height=100, width=200)
        self.frame.config(relief=RIDGE)
        ttk.Button(self.frame, text='Click Me').grid()
        self.frame.config(padding=(30, 15))

        ttk.LabelFrame(master, height=100, width=200, text='My Frame').pack()

def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
