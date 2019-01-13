# There are only TWO kinds of data attributes on Python objects: class variables and instance variables
# Class variables: declared inside the class definition (but outside of any instance methods)
# Instance variables: tied to a particular object instance

class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')
print(jack.num_legs)  # 4
print(jill.num_legs)  # 4
Dog.num_legs = 2
print(jack.num_legs)  # 2
print(jill.num_legs)  # 2
jack.num_legs = 4
print(jack.num_legs)  # 4: the above statemente created an instance variable with the same name =]
print(jill.num_legs)  # 2


class CountedObjecT:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


print(CountedObjecT.num_instances)  # 0
print(CountedObjecT().num_instances)  # 1
print(CountedObjecT().num_instances)  # 2
print(CountedObjecT().num_instances)  # 3
print(CountedObjecT.num_instances)  # 3
