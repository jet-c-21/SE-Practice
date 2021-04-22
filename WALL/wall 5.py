from abc import ABCMeta, abstractmethod, ABC


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class SC(Base):
    def foo(self):
        pass




# assert issubclass(Concrete, Base)

# c = SC()

print(issubclass(SC, Base))
