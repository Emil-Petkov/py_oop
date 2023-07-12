class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


p1 = Person("aaa", "bbb")
p2 = Person("ccc", "DDD")

print(p1 + p2) # aaa DDD
