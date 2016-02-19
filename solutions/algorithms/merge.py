'''
Problem:
Implement a merge sort.
'''


def merge(target):
    '''
    Recursively sort target.
    '''
    # Base case.
    if len(target) == 1:
        return target

    # Split and sort the sublists.
    mid = len(target)/2
    left = merge(target[:mid])
    right = merge(target[mid:])

    # Merge and return.
    result = []
    a, b = None, None
    while True:
        # Get a and b.
        if a is None and len(left):
            a = left.pop(0)

        if b is None and len(right):
            b = right.pop(0)

        # Keep going until nothing left.
        if a is None and b is None:
            break

        elif a is None:
            result.append(b)
            b = None

        elif b is None:
            result.append(a)
            a = None

        elif a < b:
            result.append(a)
            a = None

        else:
            result.append(b)
            b = None

    return result


test = [-1, 5, 4, 3, 2, 1]
print merge(test)
