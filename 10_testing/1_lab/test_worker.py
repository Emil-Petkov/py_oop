import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


"""
• Test if the worker is initialized with the correct name, salary, and energy
• Test if the worker's energy is incremented after the rest method is called
• Test if an error is raised if the worker tries to work with negative energy or equal to 0
• Test if the worker's money is increased by his salary correctly after the work method is called
• Test if the worker's energy is decreased after the work method is called
• Test if the get_info method returns the proper string with correct values
"""

from unittest import TestCase


class WorkerTest(TestCase):

    def test_worker_is_initialized_correct(self):

        # Act
        worker = Worker("Emil", 2023, 60)

        # Assert
        self.assertEqual("Emil", worker.name)
        self.assertEqual(2023, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)


if __name__ == '__main__':
    unittest.main()
