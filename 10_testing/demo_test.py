import unittest
from unittest import TestCase


class MyFirstTestEver(TestCase):

    # Mетодите трябва да започват с test_

    def test_expect_one_to_equal_one(self):  # TasteCase
        self.assertEquals(1, 1)
        # Ran 1 test in 0.001s
        # OK

    def test_expect_one_to_equal_two(self):  # TasteCase
        self.assertEquals(1, 2)
        # FAILED (failures=1)
        # AssertionError: 1 != 2

    def test_expect_one_to_equal_two(self):  # TasteCase
        self.assertNotEquals(1, 2)
        # Ran 1 test in 0.001s
        # OK


#  Ако няма __main__ тестовете няма до могат да се пуснат от конзолата, ако средата е различна от текущата

if __name__ == '__main__':
    unittest.main()

# (venv) hellhound@emil-VivoBook-ASUS:~/PycharmProjects/oop$ python 10_testing/demo_test.py
# /home/hellhound/PycharmProjects/oop/10_testing/demo_test.py:10: DeprecationWarning: Please use assertEqual instead.
#   self.assertEquals(1, 1)
# ./home/hellhound/PycharmProjects/oop/10_testing/demo_test.py:20: DeprecationWarning: Please use assertNotEqual instead.
#   self.assertNotEquals(1, 2)
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
