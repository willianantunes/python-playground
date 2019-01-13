arr = ['one', 'two', 'three']
print(arr[0])
print(arr)  # nice repr: ['one', 'two', 'three']
arr[1] = 'hello'  # lists are mutable
del arr[1]
print(arr)  # ['one', 'three']
arr.append(23)  # lists can hold arbitrary data types
print(arr)  # ['one', 'three', 23]

##### Tuple: immutable containers

arr = 'one', 'two', 'three'
print(arr[0])
print(arr)  # nice repr: ('one', 'two', 'three')
# arr[1] = 'will get error'  # <- TypeError: 'tuple' object does not support item assignment
# del arr[1]  # <- TypeError: 'tuple' object doesn't support item deletion
# Tuples can hold arbitrary data types
print(arr + (23, ))  # ('one', 'two', 'three', 23)
