def printing_list(list):
    [print(x) for x in list if x is not None]


print("first list")
first_list = [1, 2, None, 4, 5, 6, None]
printing_list(first_list)

print("second list")
second_list = [8, 9, 10, None, 12, 13, 14]
printing_list(second_list)

# first list
# 1
# 2
# 4
# 5
# 6
# second list
# 8
# 9
# 10
# 12
# 13
# 14


#########################################################################################

def get_name(numbers):
    if numbers == 7:
        return "seven"
    elif numbers == 11:
        return "eleven"
    elif numbers == 5:
        return "five"
    else:
        return numbers


def printing_list(list):
    for x in list:
        if x is None:
            continue
        print(get_name(x))


print("first list")
first_list = [1, 2, None, 4, 5, 6, None, 7]
printing_list(first_list)

print("second list")
second_list = [8, 9, 10, 11, None, 12, 13, 14]
printing_list(second_list)

# first list
# 1
# 2
# 4
# five
# 6
# seven
# second list
# 8
# 9
# 10
# eleven
# 12
# 13
# 14

#################################################################################