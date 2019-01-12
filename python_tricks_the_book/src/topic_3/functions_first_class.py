def yell(text):
    return text.upper() + '!'

print(yell('PARROT'))

##### functions are objects

another_yell_reference = yell

print(another_yell_reference('PARROT'))

del yell

# print(yell('PARROT')) # <- NameError: name 'yell' is not defined
print(another_yell_reference('PARROT'))
print(another_yell_reference.__name__) # it returns yell

##### functions can be stored in data structures

funcs = [another_yell_reference, str.lower, str.capitalize]

print(funcs) # [<function yell at 0x7f6e4a01f1e0>, <method 'lower' of 'str' objects>, <method 'capitalize' of 'str' objects>]

for f in funcs:
    print(f, f('hey there'))

''' The statement above will print...
<function yell at 0x7fac0478f1e0> HEY THERE!
<method 'lower' of 'str' objects> hey there
<method 'capitalize' of 'str' objects> Hey ther
'''
print(funcs[0]('heyho'))
