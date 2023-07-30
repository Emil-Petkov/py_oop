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

class Person():
    def __init__(self, first_name, last_name, age, gender, town="Sofia"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.town = town

    def text(self):
        print(f"My name is {self.first_name} and {self.last_name}. I'm a {self.gender} {self.age} " \
              f"years old from {self.town}.")


person_one = Person("Emil", "Petkov", 31, "Men") 

person_one.text() # My name is Emil and Petkov. I'm a Men 31 years old from Sofia.
print(person_one.__class__.__name__) # Person

#################################################################################













