'''
Problem:
Implement a trie.
'''


def search(target, dictionary):
    # If we're at the end of the tree, return all potential items.
    if not target:
        return dictionary.keys()

    # Check each term in the dictionary.
    result = []
    for term, next in dictionary.items():
        # Check for a hit.
        if target.startswith(term):
            if next:
                # If there is a sub dictionary, keep searching.
                results = search(target[len(term):], next)
                result += [term + item for item in results]

            else:
                # If there is no nesting, return.
                result += [term]

    return result


dictionary = {
    't': {
        'o': None,
        'e': {
            'a': None,
            'd': None,
            'n': None,
        },
    },
    'A': None,
    'i': {
        'n': {
            'n': None,
        },
    },
}
test = 'in'
print(search(test, dictionary))
