'''
Problem:
Generate the first "n" prime numbers.
'''


def primes(n):
    primes = []
    index = 1

    # Keep going until there are n primes.
    while len(primes) < n:
        # Start at 2.
        index += 1

        # Find the next prime.
        if any((index % prime == 0 for prime in primes)):
            continue

        # Add the prime.
        primes.append(index)

    return primes


test = 15
print(primes(test))
