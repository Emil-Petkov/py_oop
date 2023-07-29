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
import unittest


class WorkerTest(TestCase):

    def test_worker_is_initialized_correct(self):
        # Act
        worker = Worker("Emil", 2023, 60)

        # Assert
        self.assertEqual("Emil", worker.name)
        self.assertEqual(2023, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        # Arrange
        worker = Worker("Emil", 2023, 60)
        self.assertEqual(0, worker.money)
        self.assertEqual(60, worker.energy)

        # Act
        worker.work()

        # Assert
        current_expected_money = 2023
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1
        self.assertEqual(expected_energy, worker.energy)

        # Workers work again
        worker.work()

        current_expected_money = 2023 + 2023
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 59 - 1
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_has_no_energy_can_not_work(self):
        worker = Worker("Test Testov", 760, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception.args[0]))

    def test_worker_can_not_work_negative_energy(self):
        worker = Worker("Test Testov", 760, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception.args[0]))

    def test_worker_energy_is_increase_when_worker_rests(self):
        # Arrange
        worker = Worker("Test Testov2", 760, 17)
        self.assertEqual(17, worker.energy)

        # Act
        worker.rest()
        self.assertEqual(18, worker.energy)

        worker.rest()
        self.assertEqual(19, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test Testov3", 999, 34)

        # Act
        result = worker.get_info()

        # Assert
        expected_result = 'Test Testov3 has saved 0 money.'
        self.assertEqual(expected_result, result)

        # Work again
        worker.work()
        result = worker.get_info()

        # Assert
        expected_result = 'Test Testov3 has saved 999 money.'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
