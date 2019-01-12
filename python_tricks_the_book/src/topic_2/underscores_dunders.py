class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 12  # single leading underscore is a hint to tell another programmer that a variable or method is intended for internal use (see PEP 8)


def external_func():
    return 24


def _internal_only_if_it_is_imported_with_wildcard():  # Try it: from python_tricks_the_book.src.topic_2.underscores_dunders import *
    return 48
# you can only use if if specify the functions, sample: from python_tricks_the_book.src.topic_2.underscores_dunders import _internal_only_if_it_is_imported_with_wildcard

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 12
        self.__baz = 42

# Test().__baz # <- You should get an error because of name mangling

print(dir(Test()))
'''
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']
'''

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overriden'
        self._bar = 'overriden'
        self.__baz = 'overriden'

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
# print(t2.__baz) # <- AttributeError: 'ExtendedTest' object has no attribute '__baz'
print(dir(t2))
'''
['_ExtendedTest__baz', '_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', '_bar', 'foo']
'''
# Now if you try applying name mangling logic...
print(t2._ExtendedTest__baz)


class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

print(ManglingTest().get_mangled())
# print(ManglingTest().__mangled) # <- AttributeError: 'ManglingTest' object has no attribute '__mangled'


_MangledGlobal__mangled = 23
class MangledGlobal:
    def test(self):
        return __mangled
print(MangledGlobal().test()) # you will get 23

for _ in range (32):
    print('print it 32 times')


car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car

print(f"{color} - {mileage}") # red - 3812.4
