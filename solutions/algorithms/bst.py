'''
Problem:
Find the kth smallest element in a bst without using static/global variables.
'''

def find(node, k, items=0):
    # Base case.
    if not node:
        return items, None

    # Decode the node.
    left, value, right = node

    # Check left.
    index, result = find(left, k, items)

    # Exit early.
    if result:
        return index, result

    # Check this node.
    next = index + 1
    if next == k:
        return next, value

    # Check the right.
    return find(right, k, next)


test = (((None, 1, None), 2, (None, 3, None)), 4, ((None, 5, None), 5, (None, 6, None)))
#test = ((None, 1, None), 2, (None, 3, None))
print(find(test, 11))
