add = lambda x, y: x + y
result = add(5, 3)
print(result)

''' The lambda function above is the same as:
def add(x, y):
    return x + y
'''

print((lambda x, y: x + y)(5, 10))

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))  # [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

print(sorted(range(-5, 6), key=lambda x: x * x))  # [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]


def make_adder(n):
    return lambda x: x + n


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))  # 7
print(plus_5(4))  # 9


###########

# HARMFUL
class Car:
    # PEP 8: Do not assign a lambda expression, use a def
    rev = lambda self: print('Wroom!')
    crash = lambda self: print('Boom!')


my_car = Car()
my_car.crash()

# HARMFUL
print(list(filter(lambda x: x % 2 == 0, range(16))))  # [0, 2, 4, 6, 8, 10, 12, 14]
# Better
print([x for x in range(16) if x % 2 == 0])
