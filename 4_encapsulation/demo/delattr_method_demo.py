class Person:
    def __init__(self, name):
        self.name = name


p = Person("Emil")

print(p.name)              # Emil
print(delattr(p, "name"))  # None
print(p.name)              # AttributeError: 'Person' object has no attribute 'name'


################################################################

class Phone:
    def __delattr__(self, item):
        del self.__dict__[item]
        print(f"'{str(item)}' was deleted")


phone = Phone()
phone.color = "black"
del phone.color        # 'color' was deleted
