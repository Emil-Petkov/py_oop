def genrange(start, end):
    value = start

    while value <= end:
        yield value
        value += 1


print(list(genrange(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
