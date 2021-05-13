class Borg1:
    __shared_state = {'y': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state  # x will be removed (override)


b1 = Borg1()
b2 = Borg1()
b1.z = 4

print("Borg Object 'b1': ", b1)  # b and b1 are distinct objects
print("Borg Object 'b2': ", b2)
print("Object State 'b1':", b1.__dict__)  # b and b1 share same state
print("Object State 'b2':", b2.__dict__)


class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
