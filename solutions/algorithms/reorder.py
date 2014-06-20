'''
Problem:
Given a string, reorder the characters in priority order:

Example:
string: bananas
priority: can
result: aaannbs
'''


def reorder(target, priority):
    # Create a priority lookup.
    lookup = {value: index for index, value in enumerate(priority)}
    result = {}
    residual = ''

    # Generate the result.
    for item in target:
        if item in lookup:
            # Add the item.
            key = lookup[item]
            result.setdefault(key, '')
            result[key] += item

        else:
            # Store as a postfix.
            residual += item

    # Format the result.
    keys = range(len(priority))
    result = ''.join((result.get(index, '') for index in keys))
    return result + residual


test = 'bananas'
priority = 'can'
print(reorder(test, priority))
