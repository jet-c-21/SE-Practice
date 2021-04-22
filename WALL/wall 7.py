"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/21/21
"""


# coding: utf-8
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'



mc = MyClass()
print(mc)

print(mc.method())
print(mc.classmethod())
print(mc.staticmethod())