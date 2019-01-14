######## FIFOs
##### list: Terribly sloooooooooow queues

q = []
q.append('eat')
q.append('sleep')
q.append('code')

print(q)  # ['eat', 'sleep', 'code']
print(q.pop(0))  # eat
print(q)  # ['sleep', 'code']

##### collections.deque: Fast & robust queues

from collections import deque

q = deque()
q.append('eat')
q.append('sleep')
q.append('code')

print(q)  # deque(['eat', 'sleep', 'code'])
print(q.popleft())  # eat
print(q.popleft())  # sleep
print(q.popleft())  # code
print(q)  # deque([])

##### queue.Queue: Locking semantics for parallel computing

from queue import Queue

q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')

print(q)  # <queue.Queue object at 0x7faf4f2c5a90>
print(q.get())  # eat
print(q.get())  # sleep
print(q.get())  # code
# print(q.get_nowait())  # <- raise Empty

##### multiprocessing.Queue: Shared jobs queues

from multiprocessing import Queue

q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')

print(q)  # <multiprocessing.queues.Queue object at 0x7f6fd02f60b8>
print(q.get())  # eat
print(q.get())  # sleep
print(q.get())  # code
