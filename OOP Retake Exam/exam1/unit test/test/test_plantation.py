from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test_constructor(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_is_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker(self):
        self.assertEqual([], self.plantation.workers)
        # self.assertEqual(0, len(self.plantation.workers))

        result = self.plantation.hire_worker("Test Testov")

        self.assertEqual(["Test Testov"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        self.assertEqual("Test Testov successfully hired.", result)

    def test_hire_worker_already_hired_raises(self):
        self.plantation.hire_worker("Test Testov")
        self.assertEqual(["Test Testov"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Test Testov")
        self.assertEqual("Worker already hired!", str(ex.exception))

        self.assertEqual(["Test Testov"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_length(self):
        self.plantation.size = 3

        self.plantation.hire_worker("Test Testov")
        self.plantation.planting("Test Testov", "Rose")
        self.assertEqual(1, len(self.plantation))

        self.plantation.planting("Test Testov", "Tulip")
        self.assertEqual(2, len(self.plantation))

        self.plantation.hire_worker("Test Testov2")
        self.plantation.planting("Test Testov2", "Rose2")

        self.assertEqual({"Test Testov": ["Rose", "Tulip"], "Test Testov2": ["Rose2"]}, self.plantation.plants)
        self.assertEqual(3, len(self.plantation))

    def test_planting_worker_does_exist_raises(self):
        self.plantation.hire_worker("Test Testov")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Not existing", "Rose")
        self.assertEqual(f"Worker with name Not existing is not hired!", str(ex.exception))

    def test_planting_is_full_raises(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Batman")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Batman", "Bat Rose")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting(self):
        self.assertEqual({}, self.plantation.plants)

        self.plantation.hire_worker("Test Testov")
        result = self.plantation.planting("Test Testov", "Rose")
        self.assertEqual({"Test Testov": ["Rose"]}, self.plantation.plants)
        self.assertEqual("Test Testov planted it's first Rose.", result)

        result = self.plantation.planting("Test Testov", "Tulip")
        self.assertEqual({"Test Testov": ["Rose", "Tulip"]}, self.plantation.plants)
        self.assertEqual("Test Testov planted Tulip.", result)

    def test_str(self):
        self.plantation.hire_worker("Test Testov")
        self.plantation.hire_worker("Test Testov2")

        self.plantation.planting("Test Testov", "Rose")
        self.plantation.planting("Test Testov2", "Rose2")

        result = str(self.plantation)

        expected_result = "Plantation size: 2\nTest Testov, Test Testov2\nTest Testov planted: Rose\nTest Testov2 planted: Rose2"
        self.assertEqual(expected_result, result)

    def test_repr(self):
        self.plantation.hire_worker("Test Testov")
        self.plantation.hire_worker("Test Testov2")

        result = repr(self.plantation)

        expected_result = "Size: 2\nWorkers: Test Testov, Test Testov2"

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
