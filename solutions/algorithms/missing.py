'''
Problem:
Given an array of size n - 2. It contains numbers in the range 1 to n. Each
number is present at least once except for 2 numbers. Find the missing numbers.
'''


def missing(target):
    present = set(target)
    return [item for item in range(1, len(target) + 3) if item not in present]


test = [2, 1, 3, 6]
print(missing(test))
