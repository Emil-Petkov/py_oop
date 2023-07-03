class Person:
    def __init__(self, name):
        self.name = name


p = Person("Emil")
print(getattr(p, 'name', ))     # Emil
# print(getattr(p, 'age',))     # AttributeError: 'Person' object has no attribute 'age'
print(getattr(p, 'age', None))  # None


########################################################################

class Phone:
    def __getattr__(self, attr):
        return attr


phone = Phone()
print(phone.color)             # color
print(getattr(phone, "size"))  # None
