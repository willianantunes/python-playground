name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}

def greeting(userid):
    return 'Hi %s!' % name_for_userid[userid]

print(greeting(382))
# print(greeting(696969))  # <- KeyError: 696969

def greeting(userid):
    # It's inefficient because it queries the dictionary twice
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'

print(greeting(382))
print(greeting(696969))

def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there!'

print(greeting(382))
print(greeting(696969))

def greeting(userid):
    return 'Hi %s' % name_for_userid.get(userid, 'there!')

print(greeting(382))
print(greeting(696969))
