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
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        if self.win:
            self._cells[0][0].draw()
            self._cells[-1][-1].draw()
            self._animate()
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        while True:

            directions = [] 

            if i > 0 and not self._cells[i-1][j].visited:
                directions.append('left')
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                directions.append('right')
            if j > 0 and not self._cells[i][j-1].visited:
                directions.append('top')
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                directions.append('bottom')
            
            if not directions:
                return
            
            next_direction = random.choice(directions)
            # print(f'{i,j}: breaking {next_direction}')
            match next_direction:
                case 'top':
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                    next = i, j-1
                case 'bottom':
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                    next = i, j+1
                case 'left':
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                    next = i-1,j
                case 'right':
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                    next = i+1,j

            if self.win:
                self._cells[i][j].draw()
                self._cells[next[0]][next[1]].draw()
                self._animate()
            self._break_walls_r(*next)
                
    def solve(self) -> bool:
        return self._solve_r(0,0)
            
    def _solve_r(self, i ,j) -> bool:
        self._animate()
        self._cells[i][j].visited = True

        # end cell reached
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True


        directions = [] 

        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall:
            directions.append('left')
        if i < self.num_cols-1 and not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
            directions.append('right')
        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            directions.append('top')
        if j < self.num_rows-1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
            directions.append('bottom')
        
        while directions:
            next_direction = directions.pop()
            c1 = self._cells[i][j]
            match next_direction:
                case 'left':
                    c2 = self._cells[i-1][j]
                    next = i-1, j
                case 'right':
                    c2 = self._cells[i+1][j]
                    next = i+1, j
                case 'top':
                    c2 = self._cells[i][j-1]
                    next = i, j-1
                case 'bottom':
                    c2 = self._cells[i][j+1]
                    next = i, j+1
            c1.draw_move(c2)
            if self._solve_r(next[0], next[1]):
                return True
            else:
                c1.draw_move(c2, undo=True)
        
        return False