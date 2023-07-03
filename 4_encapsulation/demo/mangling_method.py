class Person:
    def __init__(self):
        self.first_name = "Emil"
        self.last_name = "Petkov"

    def __full_name(self):
        return f"{self.first_name} {self.last_name}"

    def info(self):
        return self.__full_name()


p = Person()
print(p.info())                # Emil Petkov
print(p.__full_name())         # AttributeError: 'Person' object has no attribute '__full_name'
print(p._Person__full_name())  # Emil Petkov
