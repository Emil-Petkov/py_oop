def first_part(n):
    for i in range(n):
        spaces = n - i - 1
        stars = i + 1

        line = " " * spaces + "* " * stars
        print(line.rstrip())


def second_part(n):
    for j in range(n - 1, 0, - 1):
        spaces = n - j
        stars = j

        line = " " * spaces + "* " * stars
        print(line.rstrip())


def draw_rhombus(n):
    first_part(n)
    second_part(n)


draw_rhombus(int(input()))



################################################################################

def get_line(i, n):
    spaces = n - 1 - i
    stars = i + 1
    return " " * spaces + ("* " * stars).strip()  # strip() removed last space on the line


def draw_rhombus(n):
    for i in range(0, n, 1):
        print(get_line(i, n))
    for j in range(n - 2, -1, -1):
        print(get_line(j, n))


draw_rhombus(int(input())) # 5

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

#########################################################################
