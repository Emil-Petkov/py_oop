class Person:
    def __init__(self, name):
        self.name = name


p = Person("Emil")

print(p.name)              # Emil
print(delattr(p, "name"))  # None
print(p.name)              # AttributeError: 'Person' object has no attribute 'name'
