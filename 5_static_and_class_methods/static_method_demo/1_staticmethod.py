class AlaBala:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def just_func(self):
        return f"Hello my name is {self.name} and my age is {self.age}."

    @staticmethod
    def other_func():  # self already is a just parameter name!
        return "Hi Mom!"

    """
    now other_func works as a regular function 
    in the AlaBala class that is not related to self
    """


p = AlaBala("Emil", 101)
print(p.just_func())  # Hello my name is Emil and my age is 101.

# print(AlaBala.other_func()) # TypeError: AlaBala.other_func() missing 1 required positional argument: 'self'

print(p.other_func())  # Hi Mom!
