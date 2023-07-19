class countdown_iterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration

        current_n = self.n
        self.n -= 1
        return current_n


iterator = countdown_iterator(10)

for item in iterator:
    print(item, end=" ")

# 10 9 8 7 6 5 4 3 2 1 0
