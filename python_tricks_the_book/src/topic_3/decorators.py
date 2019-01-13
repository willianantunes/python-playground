# decorator is a callable that takes a callable as input and returns another callable
import os


def null_decorator(func):
    return func


def greet():
    return 'Hello!'


greet = null_decorator(greet)

print(greet())


# Python way...


@null_decorator
def greet():
    return "Hello!"


print(greet())


##### Decorators can modify behavior

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet():
    return "Hello!"


print(greet())  # HELLO!

print(greet)  # <function uppercase.<locals>.wrapper at 0x7ffb317df2f0>


##### Applying multiple decorators to a function

def strong(func):
    def wrapper():
        return f'<strong>{func()}</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'

    return wrapper


@strong
@emphasis
def greet():
    return 'Hello!'


print(greet())  # <strong><em>Hello!</em></strong>

# If you want to avoid decorator stacking, you can do something like...

decorated_greet = strong(emphasis(greet))

print(decorated_greet())  # <strong><em><strong><em>Hello!</em></strong></em></strong>


##### Decorating functions that accept arguments

def proxy(func):
    def wrapper(*args, **kwargs):  # collect all positional and keywords arguments and stores them in args and kwargs
        return func(*args, **kwargs)  # * and ** are overloaded operators, so their meaning can vary

    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: calling {func.__name__}() '
              f'returned {original_result!r}')

        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say('Iago', 'Parrot'))
''' the above will print
TRACE: calling say() with ('Iago', 'Parrot'), {}
TRACE: calling say() returned 'Iago: Parrot'
Iago: Parrot

'''


def uppercase(func):
    import functools

    @functools.wraps(
        func)  # in order to copy over the lost metadata from the undecorated function to the decorator closure
    def wrapper():
        return func().upper()

    return wrapper


@uppercase
def greet():
    """Return a friendly greeting"""
    return 'Hello!'


print(greet.__name__)  # greet
print(greet.__doc__)  # Return a friendly greeting


##### Fun with *args and **kwargs
## Meaning: They allow a function to accept optional arguments
## They are known as 'argument-unpacking operators'


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# foo() # <- TypeError: foo() missing 1 required positional argument: 'required'
foo('Hello')
print('...')
foo('Hello', 1, 2, 3, 'iago')
''' the above will print
Hello
(1, 2, 3, 'iago')
'''
foo('Hello', 1, 2, 3, 'iago', key1='value', key2=999)
''' the above will print
Hello
(1, 2, 3, 'iago')
{'key1': 'value', 'key2': 999}
'''

### Forwarding Optional or keyword arguments
'''
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Iago'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)
'''


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


print(AlwaysBlueCar('green', 48392).color)  # blue
print(f'.{os.linesep}.{os.linesep}.{os.linesep}.')


def trace(f):
    import functools

    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)

    return decorated_function


@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)


print(greet('Hello', 'Iago'))
''' the above will return .... None is 'because decorated_function' returns nothing
<function greet at 0x7f13a5804598> ('Hello', 'Iago') {}
Hello, Iago!
None
'''

print(f'.{os.linesep}.{os.linesep}.{os.linesep}.')


##### Function argument unpacking

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(0, 1, 0)  # <0, 1, 0>

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

# Bad...
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])  # <1, 0, 1>
# Good
print_vector(*tuple_vec)  # <1, 0, 1>
## Putting a * before an iterable in a function call will unpack it
print_vector(*list_vec)

genexpr = (x * x for x in range(3))
print_vector(*genexpr)  # <0, 1, 4>

dict_vec = {'y': 0, 'z': 1, 'x': 1}
## ** operator for unpacking keyword arguments from dictionaries
print_vector(**dict_vec)  # <1, 0, 1>
print_vector(*dict_vec)  # <y, z, x>


##### Nothing to return here
### Pythona adds an implicit return None statement to the end of any function


def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value


print(type(foo1(0)))  # <class 'NoneType'>
print(type(foo2(0)))  # <class 'NoneType'>
print(type(foo3(0)))  # <class 'NoneType'>
