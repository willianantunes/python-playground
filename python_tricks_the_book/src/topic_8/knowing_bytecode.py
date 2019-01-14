'''
When the CPython interpreter executes your program, it first translates it into a sequence of bytecode instructions.

The bytecode resulting from the compilation step is cached on disk in .pyc and .pyo files, so that executing
the same Python file is faster the second time around.
'''


def greet(name):
    return f'Hello, {name}!'


print(greet.__code__)
'''
<code object greet at 0x7f067ca07c00, file "/home/wantunes/Development/git-work/python-playground/python_tricks_the_book/src/topic_8/knowing_bytecode.py", line 8>
'''
print(greet.__code__.co_code)
'''
b'd\x01|\x00\x9b\x00d\x02\x9d\x03S\x00'
'''
print(greet.__code__.co_consts)
'''
(None, 'Hello, ', '!')
'''
print(greet.__code__.co_varnames)
'''
('name',)
'''

import dis

dis.dis(greet)  # disassembler to make inspecting the bytecode easier
'''
 10           0 LOAD_CONST               1 ('Hello, ')
              2 LOAD_FAST                0 (name)
              4 FORMAT_VALUE             0
              6 LOAD_CONST               2 ('!')
              8 BUILD_STRING             3
             10 RETURN_VALUE
'''


