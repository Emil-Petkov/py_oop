class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value > self.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1

        return value_to_return


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

########################################################################

class custom_range_iterator:
    def __init__(self, cr):
        self.cr = cr
        self.next_value = self.cr.start

    def __next__(self):
        if self.next_value > self.cr.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1

        return value_to_return


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iterator(self)


cr = custom_range(1, 10)

ll = [1, 2, 3, 4, 5]

cr_iter = iter(cr)
ll_iter = iter(ll)

print(cr_iter)
print(ll_iter)
