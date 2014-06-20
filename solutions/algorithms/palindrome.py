'''
Problem:
Return the longest palindrome in string.
'''


def palindrome(target):
    reverse = target[::-1]
    length = len(target)
    result = ''

    # Shift across a window.
    for shift in range(-length+2, length-1):
        # Get the window.
        left = target[:length+shift] if shift < 0 else target[shift:]
        right = reverse[-shift:] if shift < 0 else reverse[:length-shift]

        # Find the longest palindrome.
        hit = ''
        for index in range(len(left)):
            # Check for a hit.
            if left[index] == right[index]:
                hit += left[index]

            # Terminate a current hit.
            elif hit:
                if len(hit) > len(result):
                    result = hit
                hit = ''

        # Terminate a hit.
        if hit and len(hit) > len(result):
            result = hit

    return result


test = 'amoreroma palindrome'
print(palindrome(test))
