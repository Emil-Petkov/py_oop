def squares(n):
    value = 1

    while value <= n:
        yield value * value
        value += 1


print(*squares(5))
