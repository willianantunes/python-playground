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
