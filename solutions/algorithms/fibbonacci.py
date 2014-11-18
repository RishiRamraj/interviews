'''
Problem:
Generate the nth Fibonacci number without using recursion.
'''


def fibonacci(n):
    result = [1, 1]
    for index in range(2, n):
        result.append(result[index-1] + result[index-2])
    return result[-1]


test = 8
print(fibonacci(test))
