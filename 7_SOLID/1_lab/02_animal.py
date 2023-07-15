# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
################################################################################


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass


class Cat(Animal):

    def __init__(self):
        super().__init__("Cat")

    def make_sound(self):
        return "meow"


class Dog(Animal):

    def __init__(self):
        super().__init__("Dog")

    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):

    def __init__(self):
        super().__init__("Chicken")

    def make_sound(self):
        return "cluck"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)

# meow
# woof-woof
# cluck
