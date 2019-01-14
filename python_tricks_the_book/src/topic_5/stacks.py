######## LIFOS
##### list: Simple, built-in stacks

s = []
s.append('eat')
s.append('sleep')
s.append('code')

print(s)  # ['eat', 'sleep', 'code']
print(s.pop())  # code
print(s.pop())  # sleep
print(s.pop())  # eat
print(s)  # []
# print(s.pop())  # <- IndexError: pop from empty list


##### collections.deque: Fast & robust stacks
## It can serve both as queues and as stacks

from collections import deque

s = deque()
s.append('eat')
s.append('sleep')
s.append('code')

print(s)  # deque(['eat', 'sleep', 'code'])
print(s.pop())  # code
print(s.pop())  # sleep
print(s.pop())  # eat
print(s)  # deque([])
# print(s.pop())  # <- IndexError: pop from an empty deque


##### queue.LifoQueue: Locking Semantics for Parallel computing

from queue import LifoQueue

s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')

print(s)  # <queue.LifoQueue object at 0x7f1ae8b269e8>
print(s.get())  # code
print(s.get())  # sleep
print(s.get())  # eat
# print(s.get_nowait())  # <- raise Empty
