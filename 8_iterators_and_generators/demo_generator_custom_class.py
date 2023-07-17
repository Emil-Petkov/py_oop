class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return (pair for pair in self.__dict__.items())
        ## yield ("name", self.name)
        ## yield ("age", self.age)
        # for pair in self.__dict__.items():
        #     yield pair


emil = Person("Emil", 101)

for x in emil:
    print(x)


# ('name', 'Emil')
# ('age', 101)

#######################################################################

def deep_loop(ll):
    for value in ll:
        for x in value:
            yield x


people = [
    Person("Emil", 101),
    Person("Ivan", 1)
]

[print(x) for x in deep_loop(people)]

# ('name', 'Emil')
# ('age', 101)
# ('name', 'Ivan')
# ('age', 1)
