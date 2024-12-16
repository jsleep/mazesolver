from point import *
from cell import *
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._create_cells()
    
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
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        if self.win:
            self._cells[0][0].draw()
            self._cells[-1][-1].draw()