from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__worker_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary_sum = sum(w.salary for w in self.workers)
        if self.__budget >= workers_salary_sum:
            self.__budget -= workers_salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money_for_care_animals = sum(a.money_for_care for a in self.animals)
        if self.__budget >= needed_money_for_care_animals:
            self.__budget -= needed_money_for_care_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + "\n".join(lions) + "\n"

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(tigers) + "\n"

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetahs)

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(k) for k in self.workers if isinstance(k, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"

        caretakers = [repr(c) for c in self.workers if isinstance(c, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"

        vets = [repr(v) for v in self.workers if isinstance(v, Vet)]
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets)

        return result.strip()
