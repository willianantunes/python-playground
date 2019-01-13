import copy

original_list = [1, 2, 3]
original_dict = {'v1': 1, 'v2': 2, 'v3': 3}
original_set = {'1', '2', '3'}

# Shallow copies: a reference of object is copied in other object
# It means that any changes made to a copy of object do reflect in the original object.
# In essence shallow copy is only one level deep
new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # make a shallow copy

# copy.copy() function creates shallow copies of objects

print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ys)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

xs.append(['new sublist'])
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
print(ys)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

xs[1][0] = 'X'
print(xs)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
print(ys)  # YEAH: [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]

##### Deep copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(zs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

xs[1][0] = 'X'
print(xs)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
print(zs)  # OK: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


a = Point(23, 42)
b = copy.copy(a)

print(a)  # Point(23, 42)
print(b)  # Point(23, 42)
print(a is b)  # False


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

print(rect)  # Rectangle(Point(0, 1), Point(5, 6))
print(srect)  # Rectangle(Point(0, 1), Point(5, 6))
print(rect is srect)  # False

rect.topleft.x = 999
print(rect)  # Rectangle(Point(999, 1), Point(5, 6))
print(srect)  # Rectangle(Point(999, 1), Point(5, 6))

drect = copy.deepcopy(srect)
drect.topleft.x = 222

print(drect)  # Rectangle(Point(222, 1), Point(5, 6))
print(rect)  # Rectangle(Point(999, 1), Point(5, 6))
print(srect)  # Rectangle(Point(999, 1), Point(5, 6))
