##### set: Your go-to set

vowels = {'a', 'e', 'i', 'o', 'u'}
print('e' in vowels)  # True

letter = set('alice')
print(letter.intersection(vowels))  # {'a', 'i', 'e'}

vowels.add('x')
print(vowels)  # {'o', 'u', 'e', 'i', 'x', 'a'}
print(len(vowels))  # 6

##### frozenset: Immutable sets

vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# vowels.add('p')  # <- AttributeError: 'frozenset' object has no attribute 'add'
# Frozensets are hashable and can be used as dictionary keys
d = {frozenset({1, 2, 3}): 'hello'}
print(d[frozenset({1, 2, 3})])  # hello

##### collections.Counter: Multisets
## This is useful if your need to keep track  of not only if an element is part of a set,
## but also how many times it is included in the set

from collections import Counter

inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)  # Counter({'bread': 3, 'sword': 1})

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)  # Counter({'bread': 3, 'sword': 2, 'apple': 1})

print(len(inventory))  # 3 unique elements
print(sum(inventory.values()))  # 6 total no. of elements
