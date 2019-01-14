## Python iterator protocol: __iter__ and __next__ dunder methods
numbers = [1, 2, 3]
for n in numbers:
    print(n)


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


''' INFINITE LOOP
repeater = Repeater('Hello')
for item in repeater:
    print(item)
'''

my_list = [1, 2, 3]
iterator = iter(my_list)
next(iterator)
next(iterator)
next(iterator)
# next(iterator)  # <- StopIteration


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundedRepeater('Hello', 3)
for item in repeater:
    print(item)
