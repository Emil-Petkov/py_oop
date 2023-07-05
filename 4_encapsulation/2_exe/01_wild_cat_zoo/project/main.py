from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo

zoo = Zoo("Sofia Zoo", 1000, 5, 3)

# adding animals
lion = Lion("Simba", "male", 2)
tiger = Tiger("Rajah", "male", 3)
cheetah = Cheetah("Cheetara", "female", 1)

print(zoo.add_animal(lion, 200)) # should print "Simba the Lion added to the zoo"
print(zoo.add_animal(tiger, 150)) # should print "Rajah the Tiger added to the zoo"
print(zoo.add_animal(cheetah, 170)) # should print "Cheetara the Cheetah added to the zoo"

# hiring workers
keeper = Keeper("John", 30, 100)
caretaker = Caretaker("Anna", 25, 80)
vet = Vet("Sam", 40, 150)

print(zoo.hire_worker(keeper)) # should print "John the Keeper hired successfully"
print(zoo.hire_worker(caretaker)) # should print "Anna the Caretaker hired successfully"
print(zoo.hire_worker(vet)) # should print "Sam the Vet hired successfully"
