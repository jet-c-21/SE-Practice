class Yeah:
    def __init__(self, name):
        self.name = name

    # Gets called when an attribute is accessed
    def __getattribute__(self, item):
        print('__getattribute__ ', item)
        # Calling the super class to avoid recursion
        return super().__getattribute__(item)

    # Gets called when the item is not found via __getattribute__
    def __getattr__(self, item):
        print('__getattr__ ', item)
        return super().__setattr__(item, 'orphan')


y1 = Yeah('yes')
print(y1.name)


print(y1.foo)
print(y1.foo)
print(y1.goo)
print(y1.__dict__)

