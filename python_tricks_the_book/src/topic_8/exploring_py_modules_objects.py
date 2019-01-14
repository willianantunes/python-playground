import datetime

details = dir(datetime)

print(details)
'''
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
'''

details = dir(datetime.date)

print(details)
'''
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', 
'__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', 'ctime', 'day', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'isocalendar', 
'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 
'today', 'toordinal', 'weekday', 'year']
'''

details = [_ for _ in dir(datetime) if 'date' in _.lower()]
print(details)  # ['date', 'datetime', 'datetime_CAPI']

''' They're too big... That's why the're commented out...
help(datetime)
help(datetime.date)
help(datetime.date.fromtimestamp)
'''

