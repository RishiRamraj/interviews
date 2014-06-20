'''
Problem:
Implement a binary search.
'''


def search(target, items, start, end):
    # Exit early.
    if start >= end:
        return None

    # Check the midpoint.
    index = (end - start)/2 + start

    if target > items[index]:
        return search(target, items, index, end)

    elif target < items[index]:
        return search(target, items, start, index)

    return index


items = [0, 1, 2, 3, 4]
test = 3
print(search(test, items, 0, len(items)))
