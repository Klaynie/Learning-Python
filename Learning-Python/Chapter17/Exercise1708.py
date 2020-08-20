from vpython import *
import sys  
sys.path.append('color_list')
from color_list import *

"""
t = range(0, 256, 51)
for x in t:
    for y in t:
        for z in t:
            pos = vector(x, y, z)
            color = vector(x/255, y/255, z/255)
            sphere(pos=pos, radius=10, color=color)
"""

color_dict = make_color_dict()
for name, rgb in color_dict.items():
        pos = vector(rgb[0], rgb[1], rgb[2])
        print(rgb)
        color = pos = vector(rgb[0]/255, rgb[1]/255, rgb[2]/255)
        sphere(pos=pos, radius=10, color=color)