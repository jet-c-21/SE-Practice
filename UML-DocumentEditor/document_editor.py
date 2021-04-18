"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/18/21
"""

# coding: utf-8
import datetime


class DocumentEditor:
    def __init__(self):
        self.__docList = list()
        self.__focus_doc = None

    def new_doc(self):
        self.__docList.append(Document())
        self.__focus_doc = self.__docList[-1]

    def print_doc_num(self):
        print(len(self.__docList))


class Document:
    def __init__(self):
        self.__doc_id = ''
        self.__name = ''
        self.__created_date = datetime.datetime.now()
        self.__updated_date = datetime.datetime.now()
        self.__focus_page = None
        self.__page_ls = list()

    def new_page(self):
        pass

    def save(self):
        pass

    def print(self):
        pass


class Page:
    def __init__(self):
        self.__id = ''
        self.__name = ''

    def copy(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass


class Toolkit:
    def __init__(self):
        self.__id = ''
        self.__name = ''


class TextObject:
    def __init__(self):
        self.font = 'arial'
        self.size = 12

    def add(self):
        pass

    def change_font(self):
        pass

    def change_size(self):
        pass


class GeometricalObject:
    def __init__(self):
        self.__name = ''

    def rotate(self):
        pass

    def transform(self):
        pass


class Circle(GeometricalObject):
    def __init__(self, start_point: tuple, radius: int):
        super().__init__()
        self.start_point = start_point
        self.radius = radius

    def get_area(self):
        pass


class Rectangle(GeometricalObject):
    def __init__(self, start_point: tuple, width: int, length: int):
        super().__init__()
        self.start_point = start_point
        self.width = width
        self.length = length

    def get_area(self):
        pass

class Line(GeometricalObject):
    def __init__(self, ):


if __name__ == '__main__':
    de = DocumentEditor()
