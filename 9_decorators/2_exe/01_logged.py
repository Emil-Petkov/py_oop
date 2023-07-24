def logged(func):
    def wrapper(*args):
        result = func(*args)

        return f"you called {func.__name__}{args}\nit returned {result}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
# you called func(4, 4, 4)
# it returned 6


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
# you called sum_func(1, 4)
# it returned 5
