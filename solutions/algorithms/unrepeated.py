'''
Problem:
Given a string, find the first un-repeated character in it.
'''


def unrepeated(target):
    lookup = {}

    # Build a lookup table.
    for item in target:
        lookup.setdefault(item, 0)
        lookup[item] += 1

    # Find the first non-repeated character.
    for item in target:
        if lookup[item] == 1:
            return item

    return None


test = 'unrepeated undermined'
print(unrepeated(test))
