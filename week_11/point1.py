from __future__ import annotations
from math import hypot

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def translate(self, dx:int, dy:int):
        self.x += dx
        self.y += dy
    
    def distance(self, other: Point) -> float:
        return(hypot(other.x - self.x, other.y - self.y))
    
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'
    
    def __lt__(self, other: Point) -> bool:
        return isinstance(other, Point) and self.x < other.x and self.y < other.y

#Main 
p1 = Point(2,2)
print(p1)
p1.translate(2,2)
print(p1)
print(p1.distance(Point(2,2)))