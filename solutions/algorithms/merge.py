'''
Problem:
Implement a merge sort.
'''

import itertools


def merge(input):
    '''
    Sorts from least to greatest.
    '''
    length = len(input)

    # Base case.
    if length <= 1:
        yield from iter(input)
        return

    # Sort left and right.
    half = int(length/2)
    left = merge(input[:half]) 
    right = merge(input[half:]) 

    # Merge.
    for a, b in itertools.zip_longest(left, right):
        if a is None:
            yield b

        elif b is None:
            yield a

        elif a < b:
            yield a
            yield b

        else:
            yield b
            yield a


test = [3, 5, 9, 2, -4]
print(list(merge(test)))
