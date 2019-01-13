# Dictionaries are also often called maps, hashmaps, lookup tables or associative arrays
# https://docs.python.org/3/glossary.html#term-hashable
import collections
from types import MappingProxyType

phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052,
}

squares = {x: x * x for x in range(6)}

print(phonebook)  # {'bob': 7387, 'alice': 3719, 'jack': 7052}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

### collections.OrderedDict => Remember the Insertion Order of Keys
d = collections.OrderedDict(one=1, two=2, three=3)
print(d)  # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
d['four'] = 4
print(d)  # OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d.keys())  # odict_keys(['one', 'two', 'three', 'four'])

### collections.defaultdict => Return default values for Missing Keys
# Accesing a missing key creates it  and initializes it using the default factory, in our example: list
dd = collections.defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Castor')
dd['dogs'].append('Chaves')
print(dd)  # defaultdict(<class 'list'>, {'dogs': ['Rufus', 'Castor', 'Chaves']})

### collections.ChainMap => Search Multiple Dictionaries as a Single Mapping

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = collections.ChainMap(dict1, dict2)
print(chain)  # ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
print(chain['three'])
print(chain['one'])
# print(chain['missing'])  # <- KeyError: 'missing'


### types.MappingProxyType => A wrapper for making read-only dictionaries

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
print(read_only['one'])
# read_only['one'] = 23  # <- TypeError: 'mappingproxy' object does not support item assignment
