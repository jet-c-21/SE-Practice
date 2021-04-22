"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/18/21
"""

# coding: utf-8
import datetime
from abc import ABCMeta


class Toolkit:
    def __init__(self):
        self.__id = ''
        self.__name = ''

        self.__text = TextObject()
        self.__line = Line()
        self.__circle = Circle()
        self.__rectangle = Rectangle()

    def get_circle(self):
        pass


class TextObject:
    def __init__(self):
        self.__font = 'arial'
        self.__size = 12

    def add(self):
        pass

    def change_font(self):
        pass

    def change_size(self):
        pass


class GeometricalObject:
    object_idx = 0

    def __init__(self):
        self.__class__.object_idx += 1
        self.name = f'GeoObj-{self.__class__.object_idx}'

    def create(self):
        pass

    def rotate(self):
        pass

    def transform(self):
        pass

    def set_position(self):
        pass


class Circle(GeometricalObject):
    def __init__(self):
        super().__init__()

    def set_area(self):
        pass


class Rectangle(GeometricalObject):
    def __init__(self):
        super().__init__()

    def set_area(self):
        pass


class Line(GeometricalObject):
    def __init__(self):
        super().__init__()

    def set_length(self):
        pass


if __name__ == '__main__':
    # tool = Toolkit()

    a = Circle()
    print(a.name)

    b = Line()
    print(b.name)

    c = Rectangle()
    print(c.name)

    d = Circle()
    print(d.name)


