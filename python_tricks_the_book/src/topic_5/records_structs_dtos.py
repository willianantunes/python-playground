##### dict: Simple data objects

car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True
}

car2 = {
    'color': 'blue',
    'mileage': 40231,
    'automatic': False
}

print(car1)  # {'color': 'red', 'mileage': 3812.4, 'automatic': True}
print(car2['mileage'])  # 40231

# Dicts are mutable
car2['mileage'] = 12
car2['windshield'] = 'broken'
print(car2)  # {'color': 'blue', 'mileage': 12, 'automatic': False, 'windshield': 'broken'}

# No protection against wrong field names or missing/extra fields
car3 = {
    'colr': 'green',
    'automatic': False,
    'windshield': 'broken'
}

##### tuple: immutable group of objects

# Performance-wise, tuples take up slightly less memory than lists in CPython
import dis

dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))
'''
  1           0 LOAD_CONST               0 ((23, 'a', 'b', 'c'))
              2 RETURN_VALUE
'''
dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))
'''
  1           0 LOAD_CONST               0 (23)
              2 LOAD_CONST               1 ('a')
              4 LOAD_CONST               2 ('b')
              6 LOAD_CONST               3 ('c')
              8 BUILD_LIST               4
             10 RETURN_VALUE
'''

car1 = ('red', 3812.4, True)
car2 = ('blue', 40231.0, False)
print(car2[2])  # False
# print(car2[3])  # <- IndexError: tuple index out of range


##### collections.namedtuple: Convenient Data

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)
print(getsizeof(p1))  # 72 bytes
print(getsizeof(p2))  # 72 bytes

Car = namedtuple('Car', 'color mileage automatic')
car1 = Car('red', 3812.4, True)
print(car1.mileage)  # 3812.4
# car1.mileage = 12  # fields are immutable <- AttributeError: can't set attribute

##### typing.NamedTuple: Improved Namedtuples
## This class was added in Python 3.6. The difference between traditional namedtuple is that you have
## updated syntax for defining new record types and added support for type hints.

from typing import NamedTuple


class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


# type annotations are not enforced without a separate type checking tool like mypy
car1 = Car('red', 3812.4, True)

##### struct.Struct - Serialized C Struts

from struct import Struct

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data
print(data)  # b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'

# Data blobs can que unpacked again
print(MyStruct.unpack(data))  # (23, False, 42.0)


##### types.SimpleNamespace: Fancy attribute accesss

from types import SimpleNamespace
car1 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)
print(car1)  # namespace(automatic=True, color='red', mileage=3812.4)
# Instances support attribute access and are mutable
print(car1.mileage)
car1.windshield = 'broken'
print(car1)  # namespace(automatic=True, color='red', mileage=3812.4, windshield='broken')
del car1.automatic
print(car1)  # namespace(color='red', mileage=3812.4, windshield='broken')

'''
---- You need immutable fields
ANSWER: collections.namedtuple, typing.NamedTuple
---- You need to lock down field names to avoid typos
ANSWER: collections.namedtuple, typing.NamedTuple
---- You need to keep things simple
ANSWER: a plain dictionary
---- You need full control over your data structure
ANSWER: write custom class with @property
---- You need to add behavior (methods) to the object
ANSWER: custom class, either from scratch or by extends collections.namedtuple or typing.NamedTuple
---- Your need to pack data tighly to serialize it to disk or to send it over the network
ANSWER: struct.Struct or typing.NamedTuple
'''
