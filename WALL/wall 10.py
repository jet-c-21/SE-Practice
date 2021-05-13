from pprint import pp


class A:
    def __init__(self):
        self.x = 10
        self.__dict__ = {}


a1 = A()
pp(a1.__dict__)
a1.y = 10
pp(a1.__dict__)
