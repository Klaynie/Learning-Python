
from tkinter import *
from tkinter import ttk
from enum import IntEnum

class ButtonName(IntEnum):
    TEXAS = 0
    HAWAII = 1

class Greeting(IntEnum):
    TEXAS = 0
    HAWAII = 1

button_names = [
    'Texas',
    'Hawaii'
]

greetings = [
    'Howdy, Tkinter!',
    'Aloha, Tkinter'
]

class HelloApp:
    
    def __init__(self, master):
        
        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row=0, column=0, columnspan=2)
        
        ttk.Button(master, text=button_names[ButtonName.TEXAS], command=self.texas_hello).grid(row=1, column=0)
        ttk.Button(master, text=button_names[ButtonName.HAWAII], command=self.hawaii_hello).grid(row=1,  column=1)
        
    def texas_hello(self):
        self.label.config(text=greetings[Greeting.TEXAS])
        
    def hawaii_hello(self):
        self.label.config(text=greetings[Greeting.HAWAII])

def main():
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()