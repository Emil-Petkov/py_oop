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


def uppercase(func_to_decorate):
    def func_wrapper():
        result = func_to_decorate()
        return result.upper()

    return func_wrapper


def get_shopping_list():
    return "Eggs, Milk, Bread"


def get_name():
    return "Emil Petkov"


get_name = uppercase(get_name)
get_shopping_list = uppercase(get_shopping_list)

print(f"My name is {get_name()}")
print(f"I have to buy: {get_shopping_list()}")





################################################################
