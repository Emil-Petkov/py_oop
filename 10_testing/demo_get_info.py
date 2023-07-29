import unittest
from unittest import TestCase


# Triple `A` rule:
# Arrange ->  Подготви си данните
# Act -> Нещо което искаш да тестваш
# Assert -> Проверка дали резултата е правилен

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_name}"
    #
    # def get_info(self):
    #     return f"{self.first_name} {self.last_name} is {self.age}"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        return f"My name is {self.first_name} {self.last_name} and i'm {self.age} years-old."


if __name__ == '__main__':
    unittest.main()


class TestPerson(TestCase):
    def test_fullname__expect_to_be_correct(self):  # __ две долни черти разделят смислово теста

        # Arrange
        person = Person("Emil", "Petkov", 23)

        # Act
        actual_fullname = person.fullname

        # Assert
        expected_fullname = "Emil Petkov"

        self.assertEquals(expected_fullname, actual_fullname)

        # Ran 1 test in 0.001s
        # OK

    def test_get_info__expect_to_be_correct(self):
        person = Person("Ivan", "Ivanov", 30)

        actual_info = person.get_info()
        expected_info = "My name is Ivan Ivanov and i'm 30 years-old."

        self.assertEquals(expected_info, actual_info)
