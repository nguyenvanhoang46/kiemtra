import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Shape at {self.x}, {self.y}"

    def __repr__(self):
        return f"Shape at {self.x}, {self.y}"

    def area(self):
        return 0

    def perimeter(self):
        return 0

