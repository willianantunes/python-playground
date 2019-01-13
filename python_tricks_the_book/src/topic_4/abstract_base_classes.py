# Abstract Base Classes ensure that derived classes implement particular methods from the base class
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # bar() is missing

assert issubclass(Concrete, Base)

# c = Concrete() # <- TypeError: Can't instantiate abstract class Concrete with abstract methods bar


