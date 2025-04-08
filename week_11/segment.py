from point1 import Point
from __future__ import annotations

class Segment:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2
    
    def translate(self, p1: Point, p2:Point, dx, dy):
        p1.translate(dx,dy)
        p2.translate(dx,dy)
    
    def length(self) -> float:
        return self.p1.distance(self.p2)
    
    def __lt__(self, other: Segment) -> bool:
        return isinstance(other, Segment) and \
            self.length() < other.length()
