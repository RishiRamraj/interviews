'''
Problem:
Given a large array of int return the length of the longest
increasing(non-necessarily-adjacent) sub-sequence.
'''


def permute(index, lookup):
    results = []
    for value in lookup[index]:
        if value in lookup:
            results += permute(value, lookup)

        else:
            results.append([value])

    return [[index] + result for result in results]


def longest(target):
    # Create a lookup table.
    lookup = {}
    for index, item in enumerate(target):
        for o_index, other in enumerate(target):
            # Sort the other value.
            if o_index > index and other > item:
                lookup.setdefault(index, [])
                lookup[index].append(o_index)

    # Permute the results.
    results = []
    for value in lookup.keys():
        results += permute(value, lookup)

    # Sort the results and take the largest list.
    result = sorted(results, key=len)[-1]

    # Resolve the values and return.
    return [target[index] for index in result]


test = [1, -1, 0, 2, 5, 3, 4, 5]
print(longest(test))
