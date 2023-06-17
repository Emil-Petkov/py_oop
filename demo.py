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
