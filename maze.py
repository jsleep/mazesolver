from point import *
from cell import *
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None
    ):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._create_cells()

        if seed:
            random.seed(seed)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            col = []
            self._cells.append(col)
            for j in range(self.num_rows):
                p1 = Point(self.x1+i*self.cell_size_x, self.y1+j*self.cell_size_y)
                p2 = Point(self.x1+i*self.cell_size_x+self.cell_size_x, self.y1+j*self.cell_size_y+self.cell_size_y)
                cell = Cell(p1, p2, self.win)
                col.append(cell)
        
        if self.win:
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    self._draw_cell(i,j)
        
    def _draw_cell(self,i,j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        if self.win:
            self._cells[0][0].draw()
            self._cells[-1][-1].draw()
    
    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        while True:

            directions = [] 

            if i > 0 and not self._cells[i-1][j].visited:
                directions.append('top')
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                directions.append('bottom')
            if j > 0 and not self._cells[i][j-1].visited:
                directions.append('left')
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                directions.append('right')
            
            if not directions:
                return
            
            next_direction = random.choice(directions)
            match next_direction:
                case 'top':
                    self._cells[i][j].has_top_wall = False
                    self._cells[i-1][j].has_bottom_wall = False
                    if self.win:
                        self._cells[i][j].draw()
                        self._cells[i-1][j].draw()
                        self._animate()
                    self._break_walls_r(i-1,j)
                case 'bottom':
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i+1][j].has_top_wall = False
                    if self.win:
                        self._cells[i][j].draw()
                        self._cells[i+1][j].draw()
                        self._animate()
                    self._break_walls_r(i+1,j)
                case 'left':
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][j-1].has_right_wall = False
                    if self.win:
                        self._cells[i][j].draw()
                        self._cells[i][j-1].draw()
                        self._animate()
                    self._break_walls_r(i,j-1)
                case 'right':
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][j+1].has_left_wall = False
                    if self.win:
                        self._cells[i][j].draw()
                        self._cells[i][j+1].draw()
                        self._animate()
                    self._break_walls_r(i,j+1)
            
                