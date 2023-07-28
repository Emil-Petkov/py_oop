# def uppercase(func_to_decorate):
#     result = func_to_decorate()
#     return result.upper()
#
#
# def get_shopping_list():
#     return "Eggs, Milk, Bread"
#
#
# def get_name():
#     return "Emil Petkov"
#
#
# print(uppercase(get_shopping_list))
# print(uppercase(get_name))


# EGGS, MILK, BREAD
# EMIL PETKOV


################################################################


# def uppercase(func_to_decorate):  # The **Decorator**
#     def func_wrapper():
#         result = func_to_decorate()
#         return result.upper()
#
#     return func_wrapper
#
#
# def get_shopping_list():
#     return "Eggs, Milk, Bread"
#
#
# def get_name():
#     return "Emil Petkov"
#
#
# get_name = uppercase(get_name)  # The **Decorating** of `get_name`
# get_shopping_list = uppercase(get_shopping_list)  # The **Decorating** of `get_shopping_list`
#
# print(f"My name is {get_name()}")
# print(f"I have to buy: {get_shopping_list()}")


# My name is EMIL PETKOV
# I have to buy: EGGS, MILK, BREAD

################################################################
from functools import wraps


def aaa(func):  # The **Decorator**
    @wraps(func)
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@aaa  # Name of the function => syntax sugar for `get_shopping_list = uppercase(get_shopping_list)`
def get_shopping_list():
    return "Eggs, Milk, Bread"


@aaa  # Name of the function => syntax sugar for `get_name = uppercase(get_name)`
def get_name():
    return "Emil Petkov"


print(get_name)  # <function aaa.<locals>.wrapper at 0x7fa1c05159e0>
print(get_name.__name__)  # `wrapper` вместо `get_name`, което `get_name` е името на декорираната функция
print(get_name.__name__)  # След прилагането на @wraps(func) вече излиза името на декорираната функция => `get_name`
print(f"My name is {get_name()}")
print(f"I have to buy: {get_shopping_list()}")

# My name is EMIL PETKOV
# I have to buy: EGGS, MILK, BREAD


# 1. Прави се функция, която искаме да декорираме която обицновенно се казва `func`
# 2. Вътрешно има друга функция, която обикновенно се казва `wrapper` в която е логиката за декоратора
# и тази функция връща `wrapper`
# 3. Декоратора се прилага с @ и името на функцията която играе ролята на декоратор.

# Декоратора е функция с един параметър `func` и връща друга функция `wrapper`
# Декоратора може да е в друг файл и трябва просто да се импортне

# !!! Трябва да декорираме `wrapper` функцията с @wraps за да виждам името на функцията.


