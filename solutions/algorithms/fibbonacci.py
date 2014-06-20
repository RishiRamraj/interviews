'''
Problem:
Generate the nth Fibonacci number without using recursion.
'''


def fibonacci(n):
    # Exit early.
    if n < 3:
        return 1

    # Iteratively build a cache.
    cache = [1, 1]
    for index in range(1, n-1):
        cache.append(cache[index] + cache[index-1])

    # Return the result.
    return cache[-1]


test = 8
print(fibonacci(test))
