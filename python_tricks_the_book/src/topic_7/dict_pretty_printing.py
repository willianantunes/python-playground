mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(str(mapping))  # {'a': 23, 'b': 42, 'c': 12648430}

import json

value = json.dumps(mapping, indent=4, sort_keys=True)
print(value)
'''
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
'''

import pprint

pprint.pprint(mapping) # {'a': 23, 'b': 42, 'c': 12648430}

