class MyClass:
    def method(self):
        # instance methods can modify the class itself through the self.__class__ attribute.
        # this means instance methods can also modify class state beyond object state
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        # can only modify class state, not object state
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        # this one can do nothing to class and object state
        return 'static method called'


obj = MyClass()
print(obj.method())  # ('instance method called', <__main__.MyClass object at 0x7fe09ae71710>)
print(MyClass.method(obj))  # ('instance method called', <__main__.MyClass object at 0x7f6d91191710>)
# Note the difference between them
print(obj.classmethod())  # ('class method called', <class '__main__.MyClass'>)
print(obj.staticmethod())  # static method called

print(MyClass.classmethod())  # ('class method called', <class '__main__.MyClass'>)
print(MyClass.staticmethod())  # static method called


# print(MyClass.method())  # <- TypeError: method() missing 1 required positional argument: 'self'

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        # If we decide to rename this class at some point, we won't have to remember to update here and there
        return cls(['mozzarela', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarela', 'tomatoes', 'ham'])


print(Pizza.margherita())  # Pizza(['mozzarela', 'tomatoes'])
print(Pizza.prosciutto())  # Pizza(['mozzarela', 'tomatoes', 'ham'])
