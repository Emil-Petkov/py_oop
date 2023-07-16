"""
__iter__() - internal dunder method in class
iter() - external from the class function, that calls __iter__()
"""

print("--'for' loop--")
ll = [1, 2, 3, 4, 5]

for x in ll:
    print(x)

print("--Manual--")
ll_iter = iter(ll)  # create an iterator object for 'll'

print(ll_iter)
# 1
# 2
# 3
# 4
# 5
# <list_iterator object at 0x7fa162592830>

"""
__next__() gets the next element in iterator 'll_iter'
"""
print(next(ll_iter))  # 1
print(next(ll_iter))  # 2
print(next(ll_iter))  # 3
print(next(ll_iter))  # 4
print(next(ll_iter))  # 5

# print("--'while' loop")
#
# ll_iter = iter(ll)
# while True:
#     print(next(ll_iter))

# 1
# 2
# 3
# 4
# 5
# print(next(ll_iter))
#       ^^^^^^^^^^^^
# StopIteration

print("--'while' loop. Fix 'StopIteration' Error")

ll_iter = iter(ll)
while True:
    try:
        print(next(ll_iter))
    except StopIteration:
        break
