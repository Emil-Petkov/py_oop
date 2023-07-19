class dictionary_iter:
    def __init__(self, data):
        self.items = list(data.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        #try:

        if self.idx >= len(self.items):
            raise StopIteration

        result = self.items[self.idx]
        self.idx += 1
        return result

        # except IndexError:
        #     raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# (1, '1')
# (2, '2')
