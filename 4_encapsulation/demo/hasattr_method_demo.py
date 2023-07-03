class Person:
    def __init__(self, name):
        self.name = name


p = Person("Emil")
print(hasattr(p, "name"))  # True
print(hasattr(p, "age"))  # False
