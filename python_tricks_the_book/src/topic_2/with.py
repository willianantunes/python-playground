import os
import threading
from contextlib import contextmanager

with open('hello.txt', 'w') as myFile:
    myFile.write('iago parrot')

'''
# The above is the same as:
f = open('hello.txt', 'w')
try:
    f.write('iago parrot')
finally:
    f.close()
'''

some_lock = threading.Lock()

some_lock.acquire()

# Harmful way:
try:
    pass  # do something
finally:
    some_lock.release()

# Better
with some_lock:
    pass  # do something


######
###### Supporting with our own objects


class MyManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with MyManagedFile('iago.txt') as f:
    f.write('jafar')
    f.write(os.linesep + 'jasmine')


# https://docs.python.org/3/library/contextlib.html

@contextmanager
def my_managed_file_with_context_manager(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with my_managed_file_with_context_manager('iago-context-manager.txt') as f:
    f.write('aladdin')


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('\t' * self.level + text)


with Indenter() as indent:
    indent.print('n1')
    with indent:
        indent.print('n2')
        with indent:
            indent.print('n3')
    indent.print('OK!')
