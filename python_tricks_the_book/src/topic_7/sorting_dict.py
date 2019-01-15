import operator

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
sorted_xs = sorted(xs.items())
print(sorted_xs)  # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

sorted_xs = sorted(xs.items(), key=lambda x: x[1])
print(sorted_xs)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# You can write the line 5 as the following...
sorted_xs = sorted(xs.items(), key=operator.itemgetter(1))  # it might communicate your code's intent more clearly
print(sorted_xs)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

sorted_xs = sorted(xs.items(),key=lambda x: x[1], reverse=True)
print(sorted_xs)  # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
