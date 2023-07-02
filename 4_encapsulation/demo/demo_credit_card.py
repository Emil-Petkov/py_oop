class CreditCards:
    def __init__(self, number: int, name: str, cvv: int, expectations_date: str, pin: int):
        self.number = number
        self.name = name
        self.cvv = cvv
        self.expectations_date = expectations_date
        self.pin = pin
        # self.__pin = pin  # private


visa = CreditCards(1237811172330094, "Nadezhda Petkova", 579, "23/07", 9945)

print(visa.pin)  # pin 9945
# print(visa._CreditCards__pin)  # show pin 9945
