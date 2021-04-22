"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/22/21
"""


# coding: utf-8
class A:
    def __init__(self):
        print(self.__class__)
        print(A)
        print(self.__class__ is A)


class B:
    def __init__(self):
        print('self.__class__ :', self.__class__)
        print(B)
        print(self.__class__ is B)
        self.increase()

    @classmethod
    def increase(cls):
        print('cls :', cls)

    def greet(self):
        print('hi')


class C(B):
    def __init__(self):
        # super().__init__()
        super().__init__()


# A()
c = C()
# print(c)
# C.new_var = 777
# print(c.new_var)
# print(dir())
