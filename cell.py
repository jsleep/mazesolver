from line import *
from point import *

class Cell:
    def __init__(self, point1,point2, win=None):
        self._win = win
        self._x1, self._y1 = point1.x, point1.y
        self._x2, self._y2 = point2.x, point2.y

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self):
        lines = []
        if self.has_left_wall:
            color = "black"
        else:
            color= "white"
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x1, self._y2)
        lines.append((Line(p1, p2), color))

        if self.has_right_wall:
            color = "black"
        else:
            color= "white"
        p1 = Point(self._x2, self._y1)
        p2 = Point(self._x2, self._y2)
        lines.append((Line(p1, p2), color))    
        
        if self.has_top_wall:
            color = "black"
        else:
            color= "white"
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x2, self._y1)
        lines.append((Line(p1, p2), color))

        if self.has_bottom_wall:
            color = "black"
        else:
            color= "white"
        p1 = Point(self._x1, self._y2)
        p2 = Point(self._x2, self._y2)
        lines.append((Line(p1, p2), color))
        
        for line,color in lines:
            self._win.draw_line(line, color)
    
    def draw_move(self, to_cell, undo=False):
        curr_cell_center = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        line = Line(curr_cell_center, to_cell_center)

        if undo:
            color = "gray"
        else:
            color = "red"
        
        self._win.draw_line(line, color)
        
