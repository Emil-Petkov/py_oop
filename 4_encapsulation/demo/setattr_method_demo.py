class Person:
    def __init__(self, name):
        self.name = name


p = Person("Emil")
print(setattr(p, "name", "Hello"))  # None
print(setattr(p, "age", "Emil"))  # None
print(setattr(p, "name", "Emil"))  # None
print(p.name)  # Emil


################################################################


class Phone:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value.upper()


phone = Phone()
phone.color = "black"
print(phone.color)   # BLACK
