"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/18/21
"""

# coding: utf-8
import datetime


class DocumentEditor:
    def __init__(self):
        self.__product_name = "Jet's document editor"
        self.__doc_ls = list()
        self.__doc_pointer = None

    def new_doc(self):
        doc = Document()
        doc.new_page()
        self.__doc_ls.append(doc)
        self.__doc_pointer = len(self.__doc_ls) - 1

    def switch_doc(self, doc_idx):
        self.__doc_pointer = doc_idx

    def edit_doc(self):
        selected_doc = self.__doc_ls[self.__doc_pointer]
        print(f"prepare to edit {selected_doc} with {self.__product_name}")
        selected_doc.edit_page()  # for demo
        # logic for editing


class Document:
    __doc_idx = 0

    def __init__(self):
        Document.__doc_idx += 1
        self.__id = f"Doc-{Document.__doc_idx}"
        self.__created_date = datetime.datetime.now()
        self.__updated_date = datetime.datetime.now()
        self.__page_pointer = None
        self.__page_ls = list()

    def __repr__(self):
        return self.__id

    def new_page(self):
        self.__page_ls.append(Page())
        self.__page_pointer = len(self.__page_ls) - 1

    def switch_page(self, page_index):
        self.__page_pointer = page_index

    def edit_page(self):
        selected_page = self.__page_ls[self.__page_pointer]
        print(f"prepare to edit {selected_page} in {self.__id}")
        selected_page.edit()

    def discard(self):
        print(f"prepare to delete {self.__id}")


class Page:
    __page_idx = 0

    def __init__(self):
        Page.__page_idx += 1
        self.__id = f"Page-{Page.__page_idx}"

    def __repr__(self):
        return self.__id

    def edit(self):
        print(f"prepare to edit {self.__id}")
        toolkit = Toolkit()

    def copy(self):
        print(f"prepare to copy {self.__id}")

    def delete(self):
        print(f"prepare to delete page {self.__id}")


class Toolkit:
    def __init__(self):
        self.__name = ''

        self.__text = TextObject()
        self.__geo_obj = GeometricalObject()

    def create_circle(self):
        pass

    def create_rectangle(self):
        pass

    def create_line(self):
        pass

    def create_text(self):
        pass


class TextObject:
    def __init__(self):
        self.__font = 'arial'
        self.__size = 12

    def add(self):
        pass

    def remove(self):
        pass

    def change_font(self):
        pass

    def change_size(self):
        pass


class GeometricalObject:
    @staticmethod
    def create_obj(obj_type: str):
        if obj_type == 'circle':
            return Circle()

        elif obj_type == 'rectangle':
            return Rectangle()

        elif obj_type == 'line':
            return Line()

    def __init__(self):
        self.name = ''

    def rotate(self):
        pass

    def transform(self):
        pass

    def set_position(self):
        pass

    def remove(self):
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
    de = DocumentEditor()
    de.new_doc()
    de.edit_doc()
    print(dir())
