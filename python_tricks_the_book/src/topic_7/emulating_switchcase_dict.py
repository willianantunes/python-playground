# Python doesn't have switch/case statements, so it's necessary to write long if..elif..else chains as workaround
# But you can emulate switch/case with dictionaries and first-class functions...

def myfunc(a, b):
    return a + b


funcs = [myfunc]
print(funcs[0])  # <function myfunc at 0x7f69276131e0>

print(funcs[0](2, 3))  # 5


def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    if operator == 'sub':
        return x - y
    if operator == 'mul':
        return x * y
    if operator == 'div':
        return x / y


print(dispatch_if('mul', 2, 8))  # 16
print(dispatch_if('sub', 8, 6))  # 2
print(dispatch_if('unknown', 2, 8))  # None


def dispatch_if(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_if('mul', 2, 8))  # 16
print(dispatch_if('sub', 8, 6))  # 2
print(dispatch_if('unknown', 2, 8))  # None
