from tkinter import *

def main():

    root = Tk()
    window = Toplevel(root)
    window.title('New Window')
    window.lower()
    window.state('zoomed')
    window.state('withdrawn')
    window.state('iconic')
    window.iconify()
    window.deiconify()
    window.resizable(False, False)
    window.geometry('640x480+50+100')
    root.mainloop()


if __name__ == "__main__":
    main()
