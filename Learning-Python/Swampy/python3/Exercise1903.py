from Gui import *

g = Gui()
g.title('Circle Demo')
circle = None
canvas = g.ca(width=500, height=500)
canvas.config(bg='white')

def draw_circle():
    global circle
    circle = canvas.circle([0,0], 100)

def update_circle():
    try:
        circle.config(fill=entry.get())
    except AttributeError:
        g.la(text='Draw a Circle first.')
    except:
        g.la(text='Color not defined.')


button = g.bu(text='Draw a Circle.', command=draw_circle)
button = g.bu(text='Update Color.', command=update_circle)
entry = g.en()

g.mainloop()