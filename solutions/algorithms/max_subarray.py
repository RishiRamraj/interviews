'''
Problem:
Given [int], find a non-empty sub-array with the max sum.
'''


def subarray(target):
    # Exit early.
    if all(item >= 0 for item in target):
        return target

    if all(item <= 0 for item in target):
        return [max(target)]


    # Build an incremental sum lookup.
    lookup = {}
    sum = 0
    for index, item in enumerate(target):
        sum += item
        lookup[index] = sum

    # Find all points that cross 0. The start and end of target
    # should also be included.
    ups = [0]
    downs = []
    last = None

    # Build the cross lookup.
    for index, item in enumerate(target):
        # Set last.
        if last is None:
            last = item
            continue

        # Check for a hit; we only care about positives.
        if last <= 0 and item > 0:
            ups.append(index)

        elif last > 0 and item <= 0:
            downs.append(index-1)

        # Update last.
        last = item

    # Add the end.
    downs.append(len(target)-1)

    # Permute the cross points of interest.
    max = None
    result = None
    for start in ups:
        for end in downs:
            if end <= start:
                continue

            # Find the integral.
            sum = lookup[end] - lookup[start] + target[start]

            # Set max.
            if not max:
                max = sum
                result = (start, end)
                continue
                
            # Check for a hit.
            if sum > max:
                max = sum
                result = (start, end)

    # Return result.
    start, end = result
    return target[start: end+1]


test = [13, -3, -25, -20, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(test)
print(subarray(test))
