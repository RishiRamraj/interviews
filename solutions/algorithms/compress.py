'''
Problem:
Compress a string.
'''

def compress(string):
    encoding = []
    value = None
    count = 0

    # Build the run length encoding.
    for index, next in enumerate(string):
        # Check for a change.
        if value != next:
            # Check for a new encoding.
            if count:
                encoding.append((value, count))

            # Switch to the new character.
            value = next 
            count = 0

        # Increment the count.
        count += 1

    # Add the last character.
    encoding.append((value, count))

    # Render the encoding.
    result = ''
    for value, count in encoding:
        result += '%d%s' % (count, value) if count > 1 else value

    return result

print(compress('mississippi'))
