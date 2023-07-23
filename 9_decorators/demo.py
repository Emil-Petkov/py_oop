def uppercase(func_to_decorate):
    result = func_to_decorate()
    return result.upper()


def get_shopping_list():
    return "Eggs, Milk, Bread"


def get_name():
    return "Emil Petkov"


print(uppercase(get_shopping_list))
print(uppercase(get_name))

# EGGS, MILK, BREAD
# EMIL PETKOV
