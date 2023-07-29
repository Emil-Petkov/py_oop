import unittest
from unittest import TestCase


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


class WorkerTest(TestCase):
    NAME = "Test Worker"
    SALARY = 2023
    ENERGY = 1

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

        # -----Act------Arrange------------Assert----------

    def test__init__when_valid_props__expect_correct_values(self):
        self.assertEquals(self.NAME, self.worker.name)
        self.assertEquals(self.SALARY, self.worker.salary)
        self.assertEquals(self.ENERGY, self.worker.energy)
        self.assertEquals(0, self.worker.money)

    def test__rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEquals(self.ENERGY + 1, self.worker.energy)

    def test__work__when_energy_is_0__expect_to_raise(self):
        worker = Worker(self.NAME, self.SALARY, 0)  # 0 ENERGY

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertIsNotNone(ex)

    def test__work__when_enough_energy__expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.assertEquals(self.SALARY, self.worker.money)

    def test__work__when_enough_energy__expect_energy_to_decrement(self):
        self.worker.work()
        self.assertEquals(self.ENERGY - 1, self.worker.energy)

    def test__get_info__expect_correct_result(self):
        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {self.worker.money} money.'

        self.assertEquals(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
