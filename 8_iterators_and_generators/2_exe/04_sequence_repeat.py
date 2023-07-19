class sequence_repeat:
    def __init__(self, text, n_repeat):
        self.text = text
        self.n_repeat = n_repeat
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.n_repeat:
            raise StopIteration

        result = self.text[self.index % len(self.text)]
        self.index += 1
        return result


result = sequence_repeat('abc', 5)

for item in result:
    print(item, end='')

# abcab
