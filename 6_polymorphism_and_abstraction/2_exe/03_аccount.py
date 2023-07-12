class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, amount_to_add):
        if self.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(amount_to_add)
            return f"New balance: {self.balance}"

    @staticmethod
    def validate_transaction(account, amount_to_add):
        return account.handle_transaction(amount_to_add)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError(f"please use int for amount")
        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __getitem__(self, index):
        return self._transactions[index]

    def __add__(self, other):
        new_owner = self.owner + "&" + other.owner
        new_amount = self.amount + other.amount
        new_account = Account(new_owner, new_amount)

        [new_account.add_transaction(t) for t in self]
        [new_account.add_transaction(t) for t in other]

        return new_account
