def integer():
    for i in range(1, 9):
        yield i

print(list(integer()))  # [1, 2, 3, 4, 5, 6, 7, 8]

def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integer())
print(list(chain))  # [1, 4, 9, 16, 25, 36, 49, 64]

def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integer()))
print(list(chain))  # [-1, -4, -9, -16, -25, -36, -49, -64]


