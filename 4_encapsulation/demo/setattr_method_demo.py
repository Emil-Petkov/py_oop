class Person:
    def __init__(self, name):
        self.name = name


p = Person("Emil")
print(setattr(p, "name", "Hello"))  # None
print(setattr(p, "age", "Emil"))    # None
print(setattr(p, "name", "Emil"))   # None
print(p.name)                       # Emil
