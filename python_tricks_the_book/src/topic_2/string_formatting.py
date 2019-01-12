import dis
from string import Template

errno = 50159747054
name = 'Iago'

print('Hello, %s' % name)
# %x convert an int value to a string and to represent it as a hexadecimal number
print('%x' % errno)

print('Hey %s, there is a 0x%x error!' % (name, errno))
print('Hey %(name)s, there is a 0x%(errno)x error!' % {'name': name, 'errno': errno})

###### https://docs.python.org/3/library/string.html#string-formatting

print('Hello, {}'.format(name))
print('Hello, {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))

###### Literal String Interpolation (Python 3.6)

print(f'Hello, {name}')

a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}')


def greet(name, question):
    return f'Hello, {name}! How\'s it {question}?'

print(greet('Iago', 'going'))
dis.dis(greet)
''' dis.dis(greet) prints:
 0 LOAD_CONST               1 ('Hello, ')
 2 LOAD_FAST                0 (name)
 4 FORMAT_VALUE             0
 6 LOAD_CONST               2 ("! How's it ")
 8 LOAD_FAST                1 (question)
10 FORMAT_VALUE             0
12 LOAD_CONST               3 ('?')
14 BUILD_STRING             5
16 RETURN_VALU
'''

print(f'Hey {name}, there\'s a {errno:x} error!')

###### Template Strings

t = Template('Hey, $name')
print(t.substitute(name=name))
templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))
