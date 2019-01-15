xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

zs = {}
zs.update(xs)
zs.update(ys)  # the last update wins regarding conflict issues
print(zs)  # {'a': 1, 'b': 3, 'c': 4}


# Naive implementation of update()
def update(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value


# Another way of merging with ** operator for unpacking objects
zs = dict(xs, **ys)
print(zs)  # {'a': 1, 'b': 3, 'c': 4}

# Better way
zs = {**xs, **ys}
print(zs)  # {'a': 1, 'b': 3, 'c': 4}
