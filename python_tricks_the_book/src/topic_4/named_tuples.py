import json
from collections import namedtuple

tup = ('iago', 'jafar', 'jasmine')
print(tup)
print(tup[2])
# tup[2] = 23 # <- TypeError: 'tuple' object does not support item assignment

Car = namedtuple('Car', 'color mileage')  # shorthand to namedtuple('Car', ['color', 'mileage'])
my_car = Car('red', 3812.4)
print(my_car.color)  # red
print(my_car[0])  # red
print(my_car.mileage)  # 3812.4
print(my_car[1])  # 3812.4
print(my_car)  # Car(color='red', mileage=3812.4)
print(*my_car)  # red 3812.4
# my_car.color = 'blue' # <- AttributeError: can't set attribute


##### subclassing namedtuples

Car = namedtuple('Car', 'color mileage')


class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('red', 1234)
print(c.hexcolor())  # #ff0000

print(Car._fields)  # ('color', 'mileage')
print(Car._fields + ('charge',))  # ('color', 'mileage', 'charge')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
print(ElectricCar('red', 1234, 45.0))  # ElectricCar(color='red', mileage=1234, charge=45.0)

print(my_car._asdict())  # OrderedDict([('color', 'red'), ('mileage', 3812.4)])

print(json.dumps(my_car._asdict()))  # {"color": "red", "mileage": 3812.4}
# _replace creates a shallow copy
print(my_car._replace(color='blue'))  # Car(color='blue', mileage=3812.4)
# _make is used to create new instances
print(Car._make(['red', 999]))  # Car(color='red', mileage=999)
