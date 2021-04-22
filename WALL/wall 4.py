class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

    def hi(self):
        print('hi')

class Concrete(Base):
    def foo(self):
        return 'foo() called'

b = Base()
# b.foo()
c = Concrete()
# c.bar()
assert issubclass(Concrete, Base)
