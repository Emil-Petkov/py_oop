class Cat:
    def sound(self):
        print("Meow!")


class Train:
    def sound(self):
        print("Sound of wheels")


for any_type in Cat(), Train():
    any_type.sound()

# Meow!
# Sound of wheels

