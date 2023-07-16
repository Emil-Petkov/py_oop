ll = [1, 2, 3, 4, 5]

ll_iter1 = iter(ll)
ll_iter2 = iter(ll)

print("iter1", next(ll_iter1))  # iter1 1 <<< call iter1

print("iter2", next(ll_iter2))  # iter2 1 <<< call iter2
print("iter2", next(ll_iter2))  # iter2 2 <<< call iter2

print("iter1", next(ll_iter1))  # iter1 2 <<< call iter1
print("iter1", next(ll_iter1))  # iter1 3 <<< call iter1
print("iter1", next(ll_iter1))  # iter1 4 <<< call iter1

print("iter2", next(ll_iter2))  # iter2 3 <<< call iter2

print("iter1", next(ll_iter1))  # iter1 5 <<< call iter1
