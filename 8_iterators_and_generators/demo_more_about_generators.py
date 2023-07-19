def gen_func(n):
    print("The start")

    for x in range(n):
        yield x


def normal_func(n):
    for x in range(n):
        return x


print(normal_func(5))
# 0
print(next(gen_func(5)))
# The start
# 0


################################################################

"""
Generator expressions
Generators are syntax sugar for iterators
Generator expressions are syntax sugar for generators
"""


def print_from_iter(values_iter):
    for value in values_iter:
        print(value)


def gen_func(n):
    for x in range(n):
        yield x


# [ -> literal for list comprehension
# { -> literal for set or dict comprehension
# ( -> literal for generator expression

print_from_iter(gen_func(5))
# 0
# 1
# 2
# 3
# 4

print_from_iter(
    (x for x in range(5))
)
# 0
# 1
# 2
# 3
# 4





