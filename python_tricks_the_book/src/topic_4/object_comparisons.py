### `==` checks equality... it evaluates to True if the objects referred to by the variables are equal (have the same contents)
### `is` checks identity... It evaluates to True if two variables point to the same object
import datetime
import os

a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True

c = list(a)  # in order to create a copy

print(a == c)  # True
print(a is c)  # False


##### String conversion (every class needs a __repr__)
### https://docs.python.org/3.6/reference/datamodel.html#object.__repr__


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


# By default you get the class name and the id of the object instace (which is the object's memory address in CPython)
my_car = Car('red', 37281)
print(my_car)  # <__main__.Car object at 0x7fb5fa091748>


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'


my_car = Car('red', 37281)
print(my_car)  # a red car
my_car  # if you do it in a console, you'll get something like <__main__.Car object at 0x7fb5fa091748>


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return f'a {self.color} car'


my_car = Car('red', 37281)
print(my_car)  # a red car
my_car  # if you do it in a console, you'll get `__repr__ for Car`

print(f'.{os.linesep}.{os.linesep}.{os.linesep}.')

### Containers like lists and dicts always use the result of __repr__ to represent the objects they contain
### It's best to use the built-in str() and repr() functions instead of the dunders

# Bad
print(my_car.__str__())
print(my_car.__repr__())
# Good
print(str(my_car))  # a red car
print(repr(my_car))  # __repr__ for Car

today = datetime.date.today()
print(str(today))  # 2019-01-13
# Rule of thumb: make __repr__ strings unambiguous and helpful for developers
print(repr(today))  # datetime.date(2019, 1, 13)


### Why every class needs a __repr__
### If you don't add __str__, Python falls back on the result of __repr__ when looking for __str__

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # Almost good
    def __repr__(self):
        # !r conversion flag is used to make sure the output string uses repr(self.color) instead of str(self.color)
        return f'Car({self.color!r}, {self.mileage!r})'
    # Good
    def __repr__(self):
        # !r conversion flag is used to make sure the output string uses repr(self.color) instead of str(self.color)
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

    def __str__(self):
        return f'a {self.color} car'


my_car = Car('red', 37281)
print(my_car)  # a red car
print(str(my_car))  # a red car
print(repr(my_car))  # Car('red', 37281)
