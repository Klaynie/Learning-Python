from Gui import *

def draw_circle():
    item = canvas.circle([0,0], 100, fill='red')

g = Gui()
g.title('Gui')
button = g.bu(text='Draw a Circle.', command=draw_circle)
canvas = g.ca(width=500, height=500)
canvas.config(bg='white')
g.mainloop()