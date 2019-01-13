def yell(text):
    return text.upper() + '!'


print(yell('PARROT'))

##### functions are objects

another_yell_reference = yell

print(another_yell_reference('PARROT'))

del yell

# print(yell('PARROT')) # <- NameError: name 'yell' is not defined
print(another_yell_reference('PARROT'))
print(another_yell_reference.__name__)  # it returns yell

##### functions can be stored in data structures

funcs = [another_yell_reference, str.lower, str.capitalize]

print(
    funcs)  # [<function yell at 0x7f6e4a01f1e0>, <method 'lower' of 'str' objects>, <method 'capitalize' of 'str' objects>]

for f in funcs:
    print(f, f('hey there'))

''' The statement above will print...
<function yell at 0x7fac0478f1e0> HEY THERE!
<method 'lower' of 'str' objects> hey there
<method 'capitalize' of 'str' objects> Hey ther
'''
print(funcs[0]('heyho'))


##### Functions can be passed to other functions

def greet(func):
    greeting = func('hi, I am  a Python program')
    print(greeting)


greet(another_yell_reference)


def whisper(text):
    return text.lower() + '...'


greet(whisper)

print(list(map(another_yell_reference, ['hello', 'hey', 'hi'])))  # It prints ['HELLO!', 'HEY!', 'HI!']


##### Functions can be nested

def speak(text):
    def whisper(t):
        return t.lower() + '...'

    return whisper(text)


print(speak('Hello, World'))  # hello, world...


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func(0.3))  # <function get_speak_func.<locals>.whisper at 0x7f55d5972268>
print(get_speak_func(0.7))  # <function get_speak_func.<locals>.yell at 0x7f6a49b922f0>

speak_func = get_speak_func(0.7)
print(speak_func('Hello'))


##### Functions can capture local state

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func('Hello, World', 0.7)())  # HELLO, WORLD!


##### Objects can behave like Functions

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
print(plus_3(4))  # it returns 7
