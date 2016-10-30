'''
Problem:
Compress a string.
'''


def compress(result, next):
    # Get last and count.
    count = int(result[-1]) if result[-1].isdigit() else 1
    last = result[-1] if count == 1 else result[-2]

    # Update the encoding.
    if next == last:
        index = None if count == 1 else -1
        result = result[:index] + str(count+1)

    else:
        result += next

    return result


print(reduce(compress, 'mississippi'))
