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


def aaa(func_to_decorate):  # The **Decorator**
    def func_wrapper():
        result = func_to_decorate()
        return result.upper()

    return func_wrapper


@aaa  # Name of the function => syntax sugar for `get_shopping_list = uppercase(get_shopping_list)`
def get_shopping_list():
    return "Eggs, Milk, Bread"


@aaa  # Name of the function => syntax sugar for `get_name = uppercase(get_name)`
def get_name():
    return "Emil Petkov"


print(f"My name is {get_name()}")
print(f"I have to buy: {get_shopping_list()}")

# My name is EMIL PETKOV
# I have to buy: EGGS, MILK, BREAD


# 1. Прави се функция, която искаме да декорираме която обицновенно се казва `func`
# 2. Вътрешно има друга функция, която обикновенно се казва `wrapper` в която е логиката за декоратора
# и тази функция връща `wrapper`
# 3. Декоратора се прилага с @ и името на функцията която играе ролята на декоратор.

# Декоратора е функция с един параметър `func` и връща друга функция `wrapper`
