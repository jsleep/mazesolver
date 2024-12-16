from line import *
from point import *

class Cell:
    def __init__(self, point1,point2, win):
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
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            lines.append(Line(p1, p2))
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            lines.append(Line(p1, p2))
        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            lines.append(Line(p1, p2))
        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            lines.append(Line(p1, p2))
        
        for line in lines:
            self._win.draw_line(line, "black")
