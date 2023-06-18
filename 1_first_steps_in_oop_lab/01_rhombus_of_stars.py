def get_line(i, n):
    spaces = n - 1 - i
    stars = i + 1
    return " " * spaces + "* " * stars


def draw_rhombus(n):
    for i in range(0, n, 1):
        print(get_line(i, n))
    for j in range(n - 2, -1, -1):
        print(get_line(j, n))


draw_rhombus(int(input()))
