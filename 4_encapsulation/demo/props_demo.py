class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value


red_car = Car(200)
red_car.drive()  # driving max speed 200
red_car.max_speed = 512  # changes the speed to 447
red_car.drive()  # driving max speed 447


# driving max speed 200
# driving max speed 447


###################################################################

class Person:
    def __init__(self, name: str, age=0):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            self.__age = 18
        else:
            self.__age = value


p = Person("Emil", 31)
print(p.name)  # Emil
print(p.age)   # 31
