from pprint import pp


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
print(s1 is s2)




