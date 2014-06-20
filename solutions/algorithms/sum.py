'''
Problem:
Given an array A of n integers, in sorted order, and an integer x,
design an O(n)-time complexity algorithm to determine whether there
are 2 integers in A whose sum is exactly x.
'''


def sum(target, x):
    lookup = set()

    # Build a lookup table.
    for item in target:
        lookup.add(x - item)

    # Check for a hit.
    for item in target:
        if item in lookup:
            return '%d + %d' % (item, x - item)

    return None


x = 7
test = [1, 2, 3, 4, 5]
print(sum(test, x))

x = 15
print(sum(test, x))
