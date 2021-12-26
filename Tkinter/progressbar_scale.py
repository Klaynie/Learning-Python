from tkinter import *
from tkinter import ttk
from enum import IntEnum


class Button(IntEnum):
    TOGGLE = 0
    STEP = 1
    START = 2
    STOP = 3
    RESET = 4
    PRINT = 5

class Dimension(IntEnum):
    PROGRESSBAR = 0
    SCALE =1

button_texts = [
    'Toggle',
    'Step',
    'Start',
    'Stop',
    'Reset',
    'Print'
]

dimensions = [
    200,
    400
]

class App:

    def __init__(self, parent):
        self.toggle = False
        self.progress = DoubleVar()

        # Progressbar
        self.progressbar = ttk.Progressbar(parent, orient=HORIZONTAL, length=dimensions[Dimension.PROGRESSBAR], maximum=100.0, variable=self.progress)
        self.progressbar.pack()

        # Start button
        self.start_button = ttk.Button(parent, text=button_texts[Button.START], command=self.progressbar.start)
        self.start_button.pack()
        
        # Stop button
        self.stop_button = ttk.Button(parent, text=button_texts[Button.STOP], command=self.progressbar.stop)
        self.stop_button.pack()

        # Toggle button
        self.toggle_button = ttk.Button(parent, text=button_texts[Button.TOGGLE], command=self.toggle_progressbar)
        self.toggle_button.pack()
        
        # Step button
        self.clear_button = ttk.Button(parent, text=button_texts[Button.STEP], command=self.add_progress)
        self.clear_button.pack()

        # Reset button
        self.reset_button = ttk.Button(parent, text=button_texts[Button.RESET], command=self.reset_progress)
        self.reset_button.pack()

        # Print button
        self.print_button = ttk.Button(parent, text=button_texts[Button.PRINT], command=self.print_progress)
        self.print_button.pack()

        # Scale
        self.scale = ttk.Scale(parent, orient=HORIZONTAL, length=dimensions[Dimension.SCALE], variable=self.progress, from_=0.0, to=100.0)
        self.scale.pack()
        

    def toggle_progressbar(self):
        if self.toggle:
            self.scale.set(0.0)
            self.progressbar.config(mode='indeterminate')
            self.toggle = False
        else:
            self.scale.set(0.0)
            self.progressbar.config(mode='determinate')
            self.toggle = True


    def add_progress(self):
        self.progressbar.step(25.0)

    def reset_progress(self):
        self.scale.set(0.0)
    
    def print_progress(self):
        print(self.scale.get())

def main():

    root = Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()