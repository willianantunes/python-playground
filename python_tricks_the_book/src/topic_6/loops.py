## very... VERY unpythonic

my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

print(range(len(my_items)))  # range(0, 3)

for i in range(len(my_items)):
    print(my_items[i])

## quite pythonic
for item in my_items:
    print(item)

for i, item in enumerate(my_items):
    print(f'{i}: {item}')
'''
0: a
1: b
2: c
'''

emails = {
    'Jafar': 'jafar@example.com',
    'Iago': 'iago@example.com',
}

for name, email in emails.items():
    print(f'{name} -> {email}')
'''
Jafar -> jafar@example.com
Iago -> iago@example.com
'''
