from unittest import TestCase


class MyFirstTestEver(TestCase):

    # Mетодите трябва да започват с test_

    def test_expect_one_to_equal_one(self):
        self.assertEquals(1, 1)
        # Ran 1 test in 0.001s
        # OK

    def test_expect_one_to_equal_two(self):
        self.assertEquals(1, 2)
        # FAILED (failures=1)
        # AssertionError: 1 != 2

    def test_expect_one_to_equal_two(self):
        self.assertNotEquals(1, 2)
        # Ran 1 test in 0.001s
        # OK
