"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/22/21
"""


# coding: utf-8

class Geo:
    obj_count = 0

    def __init__(self):
        print(f'prepare to add ({Geo.obj_count})')
        Geo.obj_count += 1
        self.name = f"G-{Geo.obj_count}"


class Circle(Geo):
    def __init__(self):
        super().__init__()


class Line(Geo):
    def __init__(self):
        super().__init__()


class Rect(Geo):
    def __init__(self):
        super().__init__()


circle = Circle()
line = Line()
rectangle = Rect()

print(circle.name)
print(line.name)
print(rectangle.name)
print(Geo.obj_count)
