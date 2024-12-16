from window import *
from cell import *
from point import *
import random

win = Window(800, 600)
cell_width = 50
cell_height = 50
for i in range(0, 800, cell_width):
    for j in range(0,600, cell_height):
        p1 = Point(i, j)
        p2 = Point(i+cell_width, j+cell_height)
        cell = Cell(p1, p2, win)
        cell.has_bottom_wall = bool(random.getrandbits(1))
        cell.has_top_wall = bool(random.getrandbits(1))
        cell.has_left_wall = bool(random.getrandbits(1))
        cell.has_right_wall = bool(random.getrandbits(1))
        cell.draw()

win.wait_for_close()