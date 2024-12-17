from window import *
from cell import *
from point import *
from maze import *

import random

width = 800
height = 600
win = Window(width, height)

cell_width = 50
cell_height = 50
maze = Maze(
    0,
    0,
    num_rows=height//cell_height,
    num_cols=width//cell_width,
    cell_size_x=cell_width,
    cell_size_y=cell_height,
    win=win,
    seed=42
)

maze._break_entrance_and_exit()
maze._break_walls_r(0,0)

# i1 = random.randint(0, height//cell_height-1)
# j1 = random.randint(0, width//cell_width-1)
# c1 = maze._cells[i1][j1]
# i2 = random.randint(0, height//cell_height-1)
# j2 = random.randint(0, width//cell_width-1)
# c2 = maze._cells[i2][j2]
# c1.draw_move(c2)

win.wait_for_close()