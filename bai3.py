from shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle at {self.x}, {self.y} with width {self.width} and height {self.height}"

    def __repr__(self):
        return f"Rectangle at {self.x}, {self.y} with width {self.width} and height {self.height}"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle at {self.x}, {self.y} with radius {self.radius}"

    def __repr__(self):
        return f"Circle at {self.x}, {self.y} with radius {self.radius}"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, x, y, side1, side2, side3):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return f"Triangle at {self.x}, {self.y} with sides {self.side1}, {self.side2}, {self.side3}"

    def __repr__(self):
        return f"Triangle at {self.x}, {self.y} with sides {self.side1}, {self.side2}, {self.side3}"

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        if s <= self.side1 or s <= self.side2 or s <= self.side3:
            print("Error: invalid triangle")
            return None
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
