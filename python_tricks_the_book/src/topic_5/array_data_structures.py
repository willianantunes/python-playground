##### list: Mutable dynamic arrays

arr = ['one', 'two', 'three']
print(arr[0])
print(arr)  # nice repr: ['one', 'two', 'three']
arr[1] = 'hello'  # lists are mutable
del arr[1]
print(arr)  # ['one', 'three']
arr.append(23)  # lists can hold arbitrary data types
print(arr)  # ['one', 'three', 23]

##### tuple: Immutable containers

arr = 'one', 'two', 'three'
print(arr[0])
print(arr)  # nice repr: ('one', 'two', 'three')
# arr[1] = 'will get error'  # <- TypeError: 'tuple' object does not support item assignment
# del arr[1]  # <- TypeError: 'tuple' object doesn't support item deletion
# Tuples can hold arbitrary data types
print(arr + (23,))  # ('one', 'two', 'three', 23)

##### array.array: Basic typed arrays

import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])  # 1.5
print(arr)  # array('f', [1.0, 1.5, 2.0, 2.5])
del arr[1]
print(arr)  # array('f', [1.0, 2.0, 2.5])
arr.append(42.0)
# arr[1] = 'hello' # Arrays are typed <- TypeError: must be real number, not str

##### str: Immutable Arrays of Unicode characters

arr = 'abcd'
print(arr[1])  # b

##### bytes: Immutable Arrays of single bytes

arr = bytes((0, 1, 2, 3))
print(arr[1])  # 1
print(arr)  # b'\x00\x01\x02\x03'
# bytes((0, 300)) # only valid bytes are allowed <- ValueError: bytes must be in range(0, 256)

##### bytearray: Mutable Arrays of single bytes

arr = bytearray((0,1,2,3))
print(arr[1])  # 1
print(arr)  # bytearray(b'\x00\x01\x02\x03')

'''
---- You need to store arbitrary objects, potentially with mixed data types?
ANSWER: list or tuple, depending on whether you want an immutable data structure or not
---- You have numeric (integer or floating point) data and tight packing and performance is important?
ANSWER: array.array... Consider going beyond standard library and try out packages like NumPy or Pandas.
---- You have textual data represented as Unicode characters?
ANSWER: Use str, if you need a "mutable string", use a list of characters
---- U want to store a contiguous block of bytes?
ANSWER: use the immutable bytes type, or bytearray if you need a mutable data structure
'''
