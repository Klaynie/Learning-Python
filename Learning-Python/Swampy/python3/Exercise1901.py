from Gui import *
def make_label():
    g.la(text='Nice job!')

def create_new_button():
    g.bu(text='No, press me!', command=make_label)

g = Gui()
g.title('Gui')
button = g.bu(text='Press me.', command=create_new_button)
g.mainloop()