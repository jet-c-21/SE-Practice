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

    def switch_doc(self, doc_idx):
        self.__focus_doc = self.__docList[doc_idx]

    def modify_doc(self):
        print(self.__focus_doc)
        # self.__focus_doc.modify_page()


class Document:
    def __init__(self):
        self.__doc_id = ''
        self.__name = ''
        self.__created_date = datetime.datetime.now()
        self.__updated_date = datetime.datetime.now()
        self.__focus_page = None
        self.__page_ls = list()

    def switch_page(self, page_idx):
        self.__focus_page = self.__page_ls[page_idx]

    def modify_page(self):
        self.__focus_page.edit()

    def new_page(self):
        self.__page_ls

    def save(self):
        pass

    def print(self):
        pass


class Page:
    def __init__(self):
        self.__id = id(self)
        self.__id = ''
        self.__name = ''

    def edit(self):
        toolkit = Toolkit()
        # do edition
        print(f"do edition ... on page-{self.__id}")

    def copy(self):
        pass

    def delete(self):
        pass


class Toolkit:
    def __init__(self):
        self.__id = ''
        self.__name = ''

        self.__text = TextObject()
        self.__geom = GeometricalObject()


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
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    de = DocumentEditor()
    de.new_doc()
    de.new_doc()
    de.print_doc_num()
    de.switch_doc(1)
    de.modify_doc()
