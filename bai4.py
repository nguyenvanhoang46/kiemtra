import math

import pandas as pd
import random

def bai4b():
    df = pd.read_excel("shapes.xlsx")
    max_area = 0
    max_perimeter = 0
    for index, row in df.iterrows():
        if row["shape"] == "rectangle":
            Shape = Rectangle(row['width'], row['height'], row['x'], row['y'])
            if Shape.area() > max_area:
                max_area = Shape.area()
            if Shape.perimeter() > max_perimeter:
                max_perimeter = Shape.perimeter()
        elif row["shape"] == "circle":
            Shape = Circle(row['radius'], row['x'], row['y'])
            if Shape.area() > max_area:                 
                max_area = Shape.area()
            if Shape.perimeter() > max_perimeter:
                max_perimeter = Shape.perimeter()
        elif row["shape"] == "triangle":
            Shape = Triangle(row['side1'], row['side2'], row['side3'], row['x'], row['y'])
            if Shape.area() > max_area:
                max_area = Shape.area()
            if Shape.perimeter() > max_perimeter:
                max_perimeter = Shape.perimeter()
    print(f"Max area: {max_area}\nMax perimeter: {max_perimeter}")