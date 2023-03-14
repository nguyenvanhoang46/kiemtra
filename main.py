import math

import pandas as pd
import random

from bai3 import Rectangle, Circle, Triangle
from bai4 import  bai4b

def rectangle(num_rectangles):
    rectangles = []
    for i in range(num_rectangles):
        # generate random width and height
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        # generate random coordinates
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        rectangles.append(('Rect', width, height, x, y))
    df = pd.DataFrame(rectangles, columns=["shape", "width", "height", "x", "y"])
    return df


def circle(num_circles):
    circles = []
    for i in range(num_circles):
        # generate random radius
        radius = random.randint(1, 10)
        # generate random coordinates
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        circles.append(('circle', radius, x, y))
    df = pd.DataFrame(circles, columns=["shape", "radius", "x", "y"])
    return df


def triangle(num_triangles):
    triangles = []
    for i in range(num_triangles):
        # generate random lengths of sides
        while True:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            if a + b > c and a + c > b and b + c > a:
                break
        # calculate the area of the triangle using Heron's formula
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # generate random coordinates
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        triangles.append(('triangle', a, b, c, area, x, y))
    df = pd.DataFrame(triangles, columns=["shape", "side1", "side2", "side3", "area", "x", "y"])
    return df


def read_data():
    df = pd.read_excel("shapes.xlsx")
    for index, row in df.iterrows():
        if row["shape"] == "rectangle":
            print(f"#Rect\n{row['width']} - {row['height']}\n{row['x']} - {row['y']}")
        elif row["shape"] == "circle":
            print(f"#Circle\n{row['radius']}\n{row['x']} - {row['y']}")
        elif row["shape"] == "triangle":
            print(f"#Triangle\n{row['side1']} - {row['side2']} - {row['side3']}\n{row['x']} - {row['y']}")
    else:
        print("Error")




if __name__ == '__main__':
    print('Export data')
    rectangles = rectangle(10)
    circles = circle(10)
    triangles = triangle(10)
    df = pd.concat([rectangles, circles, triangles], ignore_index=True)
    df.to_excel("shapes.xlsx", index=False)
    # read_data()
    bai4b()
