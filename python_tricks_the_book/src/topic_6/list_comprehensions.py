squares = [x * x for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
''' 
value = [expression for item in collection]

value = []
for item in collection:
    values.append(expression)

The `squares = [x * x for x in range(10)]` is translated to the following:

squares = []
for x in range(10):
    squares.append(x * x)
'''

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
'''Translating:
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)
'''

##### It supports sets and dictionaries as well

my_set = {x * x for x in range(-9, 10)}  # {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}
my_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

print(my_set)
print(my_dict)
